INSERT INTO "SELECT 
    tbvendedor.nmvdd AS vendedor,
    SUM(tbvendas.qtd * tbvendas.vrunt) AS valor_total_vendas,
    ROUND(SUM(tbvendas.qtd * tbvendas.vrunt) * (tbvendedor.perccomissao)/100,2) AS comissao
FROM tbvendas
JOIN tbvendedor ON tbvendas.cdvdd = tbvendedor.cdvdd
WHERE tbvendas.status = ''Concluído''
GROUP BY tbvendedor.nmvdd
ORDER BY comissao DESC" (vendedor,valor_total_vendas,comissao) VALUES
	 ('Vendedor 2  ',2472020.0,24720.2),
	 ('Vendedor 8',1237250,6186.25),
	 ('Vendedor 10',747250,3736.25),
	 ('Vendedor 5',270122.5,1350.61),
	 ('Vendedor 1',121530.0,1215.3),
	 ('Vendedor 3',57630.0,576.3),
	 ('Vendedor 7',69700.0,348.5),
	 ('Vendedor 6  ',50830.0,254.15),
	 ('Vendedor 4',42908.0,214.54),
	 ('Vendedor 9',39100.0,195.5);
