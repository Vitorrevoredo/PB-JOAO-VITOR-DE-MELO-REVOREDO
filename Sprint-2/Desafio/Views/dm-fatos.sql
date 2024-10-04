-- Dimensão Fatos
CREATE VIEW vw_fatos_locacao AS
SELECT 
    locacao.idLocacao,    -- Identificador da locação
    vw_dim_datas.idData,      -- Chave da dimensão Tempo
    vw_dim_cliente.idCliente,  -- Chave estrangeira da dimensão Cliente
    vw_dim_carro.idCarro,     -- Chave estrangeira da dimensão Carro
    vw_dim_combustivel.idcombustivel,  -- Chave estrangeira da dimensão Combustível
    vw_dim_vendedor.idVendedor,         -- Chave estrangeira da dimensão Vendedor
    locacao.qtdDiaria AS qtdDiaria,  -- Fato: Quantidade diária
    locacao.vlrDiaria AS vlrDiaria,  -- Fato: Valor diário
    SUM(locacao.qtdDiaria * locacao.vlrDiaria) AS vlrTotal  -- Fato: Valor total
FROM
    locacao
INNER JOIN
    vw_dim_datas ON locacao.dataLocacao = vw_dim_datas.data -- Correção do join com dimensão de datas
INNER JOIN
    vw_dim_cliente ON locacao.idCliente = vw_dim_cliente.idCliente   -- Juntando com a dimensão Cliente
INNER JOIN
    vw_dim_carro ON locacao.idCarro = vw_dim_carro.idCarro         -- Juntando com a dimensão Carro
INNER JOIN
    vw_dim_combustivel ON locacao.idcombustivel = vw_dim_combustivel.idcombustivel -- Juntando com a dimensão Combustível
INNER JOIN
    vw_dim_vendedor ON locacao.idVendedor = vw_dim_vendedor.idVendedor      -- Juntando com a dimensão Vendedor
GROUP BY 
    locacao.idLocacao,
    vw_dim_datas.idData,                      
    vw_dim_cliente.idCliente,        
    vw_dim_carro.idCarro,                        
    vw_dim_combustivel.idcombustivel,                  
    vw_dim_vendedor.idVendedor;
