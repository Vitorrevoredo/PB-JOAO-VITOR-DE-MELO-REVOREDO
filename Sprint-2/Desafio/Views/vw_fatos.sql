-- vw_fatos_locacao fonte

ALTER VIEW vw_fatos_locacao AS
SELECT 
    tl.idLocacao AS idFatoLocacao,    -- Identificador da Fato
    tl.idCliente,                     -- Chave estrangeira da Dimensão Cliente
    tl.idCarro,                       -- Chave estrangeira da Dimensão Carro
    tl.idcombustivel,                 -- Chave estrangeira da Dimensão Combustível
    tl.idVendedor,                    -- Chave estrangeira da Dimensão Vendedor
    tl.dataLocacao,                   -- Data da Locação
    tl.horaLocacao,                   -- Hora da Locação
    tl.qtdDiaria,                     -- Quantidade de Diárias
    tl.vlrDiaria,                     -- Valor da Diária
    tl.dataEntrega,                   -- Data de Entrega
    tl.horaEntrega,                   -- Hora de Entrega
    (tl.qtdDiaria * tl.vlrDiaria) AS vlrTotal -- Cálculo do Valor Total da Locação
FROM
    tb_locacao tl
JOIN clientes c ON tl.idCliente = c.idCliente
JOIN carros ca ON tl.idCarro = ca.idCarro
JOIN combustivel cb ON tl.idcombustivel = cb.idcombustivel
JOIN vendedores v ON tl.idVendedor = v.idVendedor;
