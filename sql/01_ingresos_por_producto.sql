SELECT producto, 
       count(*) as num_polizas, 
       ROUND(SUM(prima_mxn), 2) AS ingreso_total,
       ROUND(AVG(prima_mxn), 2) AS prima_promedio
FROM polizas
GROUP BY producto
ORDER BY ingreso_total desc