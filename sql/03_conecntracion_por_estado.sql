SELECT c.estado,
       COUNT(DISTINCT p.policy_id) AS num_polizas,
       COUNT(DISTINCT s.claim_id) AS num_siniestros,
       ROUND(SUM(p.prima_mxn),2) AS primas_estado
FROM clientes c
JOIN polizas p ON c.customer_id = p.customer_id
LEFT JOIN siniestros s ON p.policy_id = s.policy_id
GROUP BY c.estado
ORDER BY num_polizas DESC;
