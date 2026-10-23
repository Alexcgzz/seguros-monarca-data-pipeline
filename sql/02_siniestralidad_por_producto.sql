WITH primas AS (
    select producto_key, SUM(prima_mxn) as total_primas
    from fact_polizas
    group by producto_key
),
siniestros AS (
    select producto_key, SUM(monto_mxn) as total_siniestros
    from fact_siniestros
    group by producto_key
)

select 
    d.producto,
    ROUND(p.total_primas,2) as prima,
    ROUND(s.total_siniestros,2) as siniestro,
    ROUND(s.total_siniestros / p.total_primas * 100 ,2) as siniestralidad
from dim_producto d
join primas p on d.producto_key = p.producto_key
join siniestros s on s.producto_key = p.producto_key
order by siniestralidad desc;