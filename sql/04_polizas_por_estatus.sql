SELECT estatus,
       count(*) as num_polizas,
       ROUND(SUM(prima_mxn),2) as primas_totales
FROM polizas
GROUP BY estatus
ORDER BY num_polizas DESC;