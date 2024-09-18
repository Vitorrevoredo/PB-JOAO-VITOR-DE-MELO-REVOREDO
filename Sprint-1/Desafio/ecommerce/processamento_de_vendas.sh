#!/bin/bash
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce
data_sistema=$(date +"%Y%m%d")
primeira_data=$(sort -t"," -k5 ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/dados_de_vendas.csv | head -n 1 | cut -d"," -f5)
ultima_data=$(sort -t"," -k5 -r ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/dados_de_vendas.csv | tail -n +2 | head -n 1 | cut -d"," -f5)

mkdir -p vendas
cp dados_de_vendas.csv ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas
cd vendas
mkdir -p backup
cp dados_de_vendas.csv ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
mv dados_de_vendas.csv backup-dados-${data_sistema}.csv
quantidade_produtos=$(cat backup-dados-${data_sistema}.csv | cut -d"," -f1| tail -n 1)

echo relatorio.txt-${data_sistema}
echo \ >> relatorio.txt-${data_sistema}
echo "Data do Sistema: $(date +"%Y/%m/%d %H:%M")" >> relatorio.txt-${data_sistema}
echo \ >> relatorio.txt-${data_sistema}
echo "Data do Primeiro Registro: ${primeira_data}" >> relatorio.txt-${data_sistema}
echo "Data do Último Registro: ${ultima_data}" >> relatorio.txt-${data_sistema}
echo "Total de Itens Diferentes Vendidos: ${quantidade_produtos}" >> relatorio.txt-${data_sistema}
echo \ >> relatorio.txt-${data_sistema}
head -n 11 backup-dados-${data_sistema}.csv >> relatorio.txt-${data_sistema}

cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
zip -r backup-dados-${data_sistema}.zip backup-dados-${data_sistema}.csv
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas
rm -rf dados_de_vendas.csv 
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
rm -rf backup-dados-${data_sistema}.csv