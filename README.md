# Seguros Monarca - Data Pipeline

Pipeline de datos de punta a punta para una aseguradora ficticia:
ingesta de datos crudos -> limpieza -> modelado -> data lake (s3) -> consultas (Athena) -> dashboard

## Problema
El cliente (gerente de datos de Seguros Monarca) busca limpiar distinta informacion que tiene regada por diferentes sistemas los cuales cada uno exporta de diferente manera. 

## Objetivo de negocio
Nos solicita llegar a una conclusion y visualizacion leve de los datos. Asi mismo, se busca resolver 5 incognitas:
1. Ingreso de primas por producto y mes
2. Siniestralidad (siniestros ÷ primas) por producto
3. Concentracion de polizas y siniestros por estado
4. Polizas activas vs vencidas/canceladas e ingreso en riesgo
5. Monto promedio de siniestro por categoria

## Arquitectura
CSV crudos -> pandas (realizamos la limpieza) -> esquema estrella (Parquet) -> Amazon S3 -> Amazon Athena (SQL) -> dashboard

## Stack
Python | pandas | SQL | AWS S3 | AWS Athena | Git