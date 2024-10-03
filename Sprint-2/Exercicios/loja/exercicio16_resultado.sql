INSERT INTO "SELECT
	tbvendas.estado,
	tbvendas.nmpro,
	ROUND(AVG(tbvendas.qtd),4) AS quantidade_media
FROM tbvendas
WHERE tbvendas.status = ''Concluído''
GROUP BY estado, nmpro
ORDER BY estado, nmpro" (estado,nmpro,quantidade_media) VALUES
	 ('Alagoas','Produto A',20500.0),
	 ('Bahia','Produto A',13590.9091),
	 ('Ceará','Produto A',11772.7273),
	 ('Ceará','Produto C',14666.6667),
	 ('Goiás','Produto A',12500.0),
	 ('Mato Grosso do Sul','Produto E',9639.0909),
	 ('Minas Gerais','Produto A',10050.0),
	 ('Paraíba','Produto A',23250.0),
	 ('Piauí','Produto SL',12916.6667),
	 ('Rio Grande do Norte','Produto A',12107.1429);
INSERT INTO "SELECT
	tbvendas.estado,
	tbvendas.nmpro,
	ROUND(AVG(tbvendas.qtd),4) AS quantidade_media
FROM tbvendas
WHERE tbvendas.status = ''Concluído''
GROUP BY estado, nmpro
ORDER BY estado, nmpro" (estado,nmpro,quantidade_media) VALUES
	 ('Rio Grande do Sul','Produto CH',13363.3333),
	 ('Rio de Janeiro','Produto C',25250.0),
	 ('Santa Catarina','Produto A',14000.0),
	 ('São Paulo','Produto C',15250.0),
	 ('Tocantins','Produto TN  ',33178.5714);
