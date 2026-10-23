SELECT p.producto,
       ROUND(SUM(p.prima_mxn),2) as total_primas,
       ROUND(SUM(s.monto_mxn),2) as total_siniestros,
       ROUND(SUM(s.monto_mxn) / SUM(p.prima_mxn) * 100,2) as siniestralidad_pct
FROM polizas p
LEFT JOIN siniestros s ON p.policy_id = s.policy_id
GROUP BY p.producto
ORDER BY siniestralidad_pct desc