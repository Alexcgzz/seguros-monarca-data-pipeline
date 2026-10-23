WITH polizas as (
    select c.estado, count(*) as ppe
    from fact_polizas f
    join dim_clientes c on f.customer_id = c.customer_id
    group by c.estado
),
siniestros as (
    select c.estado, count(*) as spe
    from fact_siniestros f
    join dim_clientes c on f.customer_id = c.customer_id
    group by c.estado
)

select p.estado as Estado, p.ppe as Polizas ,s.spe as Siniestros
from polizas p
left join siniestros s on p.estado = s.estado
order by p.ppe desc;