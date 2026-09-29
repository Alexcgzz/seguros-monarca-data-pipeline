SELECT categoria,
       count(*) as num_siniestros,
       ROUND(AVG(monto_mxn),2) as monto_promedio,
       ROUND(SUM(monto_mxn),2) as monto_total
FROM siniestros
GROUP BY categoria
ORDER BY monto_promedio DESC;