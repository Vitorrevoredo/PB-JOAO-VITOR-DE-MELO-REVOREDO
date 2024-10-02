-- Dimensão tempo
CREATE VIEW dm_datas AS
SELECT
	vw_fatos_locacao.idFatoLocacao,
	tb_locacao.dataLocacao,
	tb_locacao.horaLocacao,
	tb_locacao.dataEntrega,
	tb_locacao.horaEntrega
FROM vw_fatos_locacao
INNER JOIN tb_locacao ON vw_fatos_locacao.idFatoLocacao = tb_locacao.idLocacao;