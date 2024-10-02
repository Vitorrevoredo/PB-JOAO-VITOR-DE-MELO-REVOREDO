
-- Dimensional Datas

CREATE VIEW vw_dim_datas AS
SELECT
    ROW_NUMBER() OVER (ORDER BY tl.dataLocacao) AS idData,  -- Gera um ID incremental
    tl.idLocacao,
    tl.dataLocacao,
    tl.horaLocacao,
    tl.dataEntrega,
    tl.horaEntrega,
    substr(tl.dataLocacao, 1, 2) AS dia,   -- Dia
    substr(tl.dataLocacao, 4, 2) AS mes,   -- Mês
    substr(tl.dataLocacao, 7, 2) AS ano    -- Ano
FROM
    tb_locacao tl;
