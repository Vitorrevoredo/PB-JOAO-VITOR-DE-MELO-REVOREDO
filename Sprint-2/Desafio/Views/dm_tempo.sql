SELECT
    vw_dim_carro.marcaCarro,
    AVG(vw_fatos_locacao.vlrDiaria) AS valorMedioDiaria
FROM
    vw_fatos_locacao
INNER JOIN
    vw_dim_carro ON vw_fatos_locacao.idCarro = vw_dim_carro.idCarro
WHERE
    vw_dim_carro.marcaCarro = 'Toyota'
GROUP BY
    vw_dim_carro.marcaCarro;
