INSERT INTO "SELECT 
	tbvendedor.cdvdd, tbvendedor.nmvdd
FROM tbvendedor
LEFT JOIN tbvendas ON tbvendas.cdvdd = tbvendedor.cdvdd
GROUP BY tbvendas.cdvdd, tbvendedor.nmvdd
ORDER BY COUNT(tbvendas.cdven) DESC
LIMIT 1" (cdvdd,nmvdd) VALUES
	 (2,'Vendedor 2  ');
