INSERT INTO "SELECT 
	tbdependente.cddep,
	tbdependente.nmdep,
	tbdependente.dtnasc,
	SUM(tbvendas.qtd*tbvendas.vrunt) as valor_total_vendas
FROM tbvendas
JOIN tbvendedor ON tbvendedor.cdvdd = tbvendas.cdvdd 
JOIN tbdependente ON tbdependente.cdvdd = tbvendas.cdvdd
WHERE tbvendas.status = ''Concluído''
GROUP BY tbvendas.cdvdd
ORDER BY cddep DESC
LIMIT 1
" (cddep,nmdep,dtnasc,valor_total_vendas) VALUES
	 (6,'Dependente 6','2018-03-02 00:00:00',39100.0);
