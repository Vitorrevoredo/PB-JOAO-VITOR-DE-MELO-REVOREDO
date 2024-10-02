-- Dimensão Fatos
CREATE VIEW vw_fatos_locacao AS
SELECT 
    tb_locacao.idLocacao,    -- Identificador da locação
    vw_dim_datas.idData,      -- Chave da dimensão Tempo
    vw_dim_cliente.idCliente,  -- Chave estrangeira da dimensão Cliente
    vw_dim_carro.idCarro,     -- Chave estrangeira da dimensão Carro
    vw_dim_combustivel.idcombustivel,  -- Chave estrangeira da dimensão Combustível
    vw_dim_vendedor.idVendedor,         -- Chave estrangeira da dimensão Vendedor
    SUM(tb_locacao.qtdDiaria) AS qtdDiaria,  -- Fato: Quantidade diária
    SUM(tb_locacao.vlrDiaria) AS vlrDiaria,  -- Fato: Valor diário
    SUM(tb_locacao.qtdDiaria * tb_locacao.vlrDiaria) AS vlrTotal  -- Fato: Valor total
FROM
    tb_locacao
INNER JOIN
    vw_dim_datas ON tb_locacao.idLocacao = vw_dim_datas.idLocacao -- Juntando com a dimensão Tempo
INNER JOIN
    vw_dim_cliente ON tb_locacao.idCliente = vw_dim_cliente.idCliente   -- Juntando com a dimensão Cliente
INNER JOIN
    vw_dim_carro ON tb_locacao.idCarro = vw_dim_carro.idCarro         -- Juntando com a dimensão Carro
INNER JOIN
    vw_dim_combustivel ON tb_locacao.idcombustivel = vw_dim_combustivel.idcombustivel -- Juntando com a dimensão Combustível
INNER JOIN
    vw_dim_vendedor ON tb_locacao.idVendedor = vw_dim_vendedor.idVendedor      -- Juntando com a dimensão Vendedor
GROUP BY 
    tb_locacao.idLocacao,
    vw_dim_datas.idData,                      
    vw_dim_cliente.idCliente,        
    vw_dim_carro.idCarro,                        
    vw_dim_combustivel.idcombustivel,                  
    vw_dim_vendedor.idVendedor;
