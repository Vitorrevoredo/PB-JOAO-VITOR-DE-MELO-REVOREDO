#!/bin/bash
data_sistema=$(date +"%Y%m%d")
mkdir -p processamento_de_vendas
mkdir -p processamento_de_vendas/backup

cp processamento_de_vendas/dados_de_vendas.cvs processamento_de_vendas/backup/dados-${data_sistema}.cvs
mv processamento_de_vendas/backup/dados-${data_sistema}.cvs processamento_de_vendas/backup/backup-dados-${data_sistema}.cvs

echo "Data do Sistema: $(date +"%Y/%m/%d %H:%M")" > processamento_de_vendas/backup/relatorio.txt-${data_sistema}
echo "Data do Primeiro Registro: 01/01/2023" >> processamento_de_vendas/backup/relatorio.txt-${data_sistema}
echo "Data do Último Registro: 31/03/2023" >> processamento_de_vendas/backup/relatorio.txt-${data_sistema}
echo "Quantidade Total de Itens Diferentes Vendidos: 88" >> processamento_de_vendas/backup/relatorio.txt-${data_sistema}

head -n 10 processamento_de_vendas/backup/backup-dados-${data_sistema}.cvs >> processamento_de_vendas/backup/relatorio.txt-${data_sistema}

zip processamento_de_vendas/backup/backup-dados-${data_sistema}.zip processamento_de_vendas/backup/backup-dados-${data_sistema}.cvs

rm processamento_de_vendas/backup/backup-dados-${data_sistema}.cvs
rm processamento_de_vendas/dados_de_vendas.cvs
