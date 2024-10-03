INSERT INTO "SELECT 
	tbvendas.cdcli,
	tbvendas.nmcli,
	SUM(tbvendas.vrunt*tbvendas.qtd) AS gasto
FROM tbvendas
WHERE tbvendas.status = ''Concluído''
GROUP BY tbvendas.cdcli
ORDER BY gasto DESC
LIMIT 1" (cdcli,nmcli,gasto) VALUES
	 (9,'Cliente BCA',1237250);
