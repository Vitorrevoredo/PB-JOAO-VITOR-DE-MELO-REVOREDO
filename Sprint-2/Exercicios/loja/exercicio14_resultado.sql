INSERT INTO "SELECT
    tbvendas.estado,
    ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) AS gastomedio
FROM tbvendas
WHERE tbvendas.status = ''Concluído''
GROUP BY tbvendas.estado
ORDER BY gastomedio DESC" (estado,gastomedio) VALUES
	 ('Rio de Janeiro',176750.0),
	 ('Rio Grande do Sul',120270.0),
	 ('São Paulo',106750.0),
	 ('Ceará',55479.57),
	 ('Mato Grosso do Sul',19278.18),
	 ('Tocantins',8294.64),
	 ('Paraíba',7905.0),
	 ('Alagoas',6970.0),
	 ('Piauí',6458.33),
	 ('Santa Catarina',4760.0);
INSERT INTO "SELECT
    tbvendas.estado,
    ROUND(AVG(tbvendas.qtd * tbvendas.vrunt), 2) AS gastomedio
FROM tbvendas
WHERE tbvendas.status = ''Concluído''
GROUP BY tbvendas.estado
ORDER BY gastomedio DESC" (estado,gastomedio) VALUES
	 ('Bahia',4620.91),
	 ('Goiás',4250.0),
	 ('Rio Grande do Norte',4116.43),
	 ('Minas Gerais',3417.0);
