INSERT INTO "SELECT 
	tbvendas.cdpro, 
	tbvendas.nmpro
FROM tbvendas
WHERE tbvendas.dtven BETWEEN ''2014-02-03'' AND ''2018-02-02''
GROUP BY cdpro, nmpro
ORDER BY COUNT(cdven) DESC
LIMIT 1" (cdpro,nmpro) VALUES
	 (1,'Produto A');
