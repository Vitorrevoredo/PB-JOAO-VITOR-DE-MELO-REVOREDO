#!/bin/bash
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce
data_sistema=$(date +"%Y%m%d")
quantidade_produtos=$(awk -F ',' 'END {print $1}' dados_de_vendas.csv)
ultima_data=$(awk -F ',' 'END {print $5}' dados_de_vendas.csv)

cp dados_de_vendas.csv ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas
cp dados_de_vendas.csv ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
mv dados_de_vendas.csv backup-dados-${data_sistema}.csv

echo relatorio.txt-${data_sistema}
echo "Data do Sistema: $(date +"%Y/%m/%d %H:%M")" >> relatorio.txt-${data_sistema}
echo "Data do Primeiro Registro: 01/01/2023" >> relatorio.txt-${data_sistema}
echo "Data do Último Registro: ${ultima_data}" >> relatorio.txt-${data_sistema}
echo "Quantidade Total de Itens Diferentes Vendidos: ${quantidade_produtos}" >> relatorio.txt-${data_sistema}
head -n 11 backup-dados-${data_sistema}.csv >> relatorio.txt-${data_sistema}

cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
zip -r backup-dados-${data_sistema}.zip backup-dados-${data_sistema}.csv
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas
rm -rf dados_de_vendas.csv 
cd ~/PB-JOAO-VITOR-DE-MELO-REVOREDO/Sprint-1/Desafio/ecommerce/vendas/backup
rm -rf backup-dados-${data_sistema}.csv