"""
Generador de datos sintéticos — Seguros Monarca (proyecto de práctica).

Crea datasets ficticios de una aseguradora (clientes, pólizas, siniestros
y pagos) con imperfecciones realistas —nulos, formatos de fecha mezclados,
categorías inconsistentes, duplicados y valores inválidos— para simular
datos de origen "sucios" y practicar el pipeline de limpieza y modelado.

Uso: python generar_datos.py
Salida: data/raw/ (completo, ignorado por git) y data/sample/ (muestra de 100 filas).

Ultimo cambio: 2026-09-24
"""

import csv, random, os
from datetime import date, timedelta
from faker import Faker

fake = Faker('es_MX') 
Faker.seed(42); random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, 'data', 'raw')
SAMPLE = os.path.join(BASE, 'data', 'sample')
os.makedirs(RAW, exist_ok=True)
os.makedirs(SAMPLE, exist_ok=True)

N_CUST, N_POL, N_CLAIM, N_PAY = 5000, 8000, 4000, 20000

estados = ['Nuevo León','CDMX','Jalisco','Puebla','Yucatán','Coahuila',
           'Guanajuato','Querétaro','Baja California','Sonora']

producto_variants = {
    'Auto':['Auto','auto','AUTO','Automóvil'],
    'Hogar':['Hogar','hogar','Casa','HOGAR'],
    'Vida':['Vida','vida','VIDA','Seguro de Vida'],
    'Gastos Médicos':['Gastos Médicos','Gastos medicos','GMM','gastos médicos'],
}

status_variants = {
    'active':['active','Activo','ACTIVE','activa','Vigente'],
    'lapsed':['lapsed','Vencida','LAPSED','vencido'],
    'cancelled':['cancelled','Cancelada','CANCELLED','cancelado'],
}

claim_status = ['open','approved','rejected','paid','En revisión','Pagado','Rechazado']
pay_methods  = ['tarjeta','TARJETA','Transferencia','domiciliación','SPEI','oxxo','']

def maybe_null(val, p=0.07): return '' if random.random()<p else val
def rand_date(y0,y1):
    s,e=date(y0,1,1),date(y1,9,1); return s+timedelta(days=random.randint(0,(e-s).days))
def fmt_date(d):
    return d.strftime(random.choice(['%Y-%m-%d','%d/%m/%Y','%m-%d-%Y']))
def w(name, header, rows):
    with open(os.path.join(RAW,name),'w',newline='',encoding='utf-8') as f:
        wr=csv.writer(f); wr.writerow(header); wr.writerows(rows)
    with open(os.path.join(SAMPLE,name),'w',newline='',encoding='utf-8') as f:
        wr=csv.writer(f); wr.writerow(header); wr.writerows(rows[:100])
    print(f'{name}: {len(rows)} filas (muestra: 100)')

customers=[]
for i in range(1,N_CUST+1):
    bd=rand_date(1955,2005)
    bd_s=bd.strftime('%Y-%m-%d') if random.random()>0.1 else bd.strftime('%d/%m/%Y')
    city=fake.city(); city=random.choice([city,city.lower(),city.upper(),' '+city+' '])
    customers.append([f'C{i:05d}',fake.name(),maybe_null(fake.email(),0.05),bd_s,
        random.choice(['M','F','Masculino','Femenino','m','f','']),city,
        random.choice(estados),fmt_date(rand_date(2021,2026))])
for _ in range(40): customers.append(list(random.choice(customers)))
w('customers.csv',['customer_id','nombre','email','fecha_nacimiento','genero','ciudad','estado','fecha_alta'],customers)

cust_ids=[c[0] for c in customers]; policies=[]
for i in range(1,N_POL+1):
    pc=random.choice(list(producto_variants)); st=rand_date(2021,2026)
    prem=round(random.uniform(2000,60000),2)
    if random.random()<0.02: prem=-prem
    if random.random()<0.02: prem=''
    sc=random.choices(['active','lapsed','cancelled'],weights=[0.6,0.25,0.15])[0]
    policies.append([f'P{i:06d}',random.choice(cust_ids),random.choice(producto_variants[pc]),
        fmt_date(st),fmt_date(st+timedelta(days=365)),prem,random.choice(status_variants[sc])])
w('policies.csv',['policy_id','customer_id','producto','fecha_inicio','fecha_fin','prima_mxn','estatus'],policies)

pol_ids=[p[0] for p in policies]; claims=[]
for i in range(1,N_CLAIM+1):
    amt=round(random.uniform(1000,500000),2)
    if random.random()<0.04: amt=''
    claims.append([f'CL{i:06d}',random.choice(pol_ids),fmt_date(rand_date(2022,2026)),amt,
        random.choice(claim_status),
        random.choice(['Colisión','Robo','Incendio','Daños a terceros','Hospitalización','Fallecimiento','Otro',''])])
w('claims.csv',['claim_id','policy_id','fecha_siniestro','monto_mxn','estatus','categoria'],claims)

payments=[]
for i in range(1,N_PAY+1):
    payments.append([f'PAY{i:07d}',random.choice(pol_ids),fmt_date(rand_date(2021,2026)),
        round(random.uniform(500,6000),2),random.choice(pay_methods)])
w('payments.csv',['payment_id','policy_id','fecha_pago','monto_mxn','metodo'],payments)
print('\nListo. Datos en data/raw/ y muestras en data/sample/')