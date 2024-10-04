-- Dimensão Datas
CREATE VIEW vw_dim_datas AS
SELECT
    ROW_NUMBER() OVER (ORDER BY l.dataLocacao) AS idData,  -- Gera um ID incremental
    l.dataLocacao,       -- Data da locação (chave de ligação)
    l.horaLocacao,
    l.dataEntrega,
    l.horaEntrega,
    substr(l.dataLocacao, 1, 2) AS dia,   -- Dia
    substr(l.dataLocacao, 4, 2) AS mes,   -- Mês
    substr(l.dataLocacao, 7, 2) AS ano    -- Ano
FROM
    locacao l;
