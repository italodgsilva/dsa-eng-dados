# 1. Carregar somente registros com quantidade produzida superior a 10
# 2. Remover ponto na última coluna para evitar valores truncados.
# 3. Enriquecer os dados adicionando no destino uma coluna com a margem de
# lucro de cada produto.

import csv
import sqlite3


# Abre o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r', encoding='utf-8') as file:

    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta no banco de dados
    conn = sqlite3.connect('dsabd.db')

    conn.execute('DROP TABLE IF EXISTS producao')

    # Cria uma tabela para armazenar os dados de produção dos alimentos
    conn.execute('''
        CREATE TABLE producao (
            produto TEXT,
            quantidade INTEGER,
            preco_medio REAL,
            receita_total INTEGER,
            margem_lucro REAL
        );
    '''
    )

    # Insere cada linha do arquivo na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:

            # Remove o ponto do valor da última coluna
            row[3] = int(row[3].replace('.', ''))

            # Calcula a margem de lucro bruta com bade no valor médio de
            # venda e na receita total
            margem_lucro = (row[3] / float(row[1])) - float(row[2])

            conn.execute('''
                INSERT INTO producao (
                    produto, quantidade, preco_medio, 
                    receita_total, margem_lucro
                )
                VALUES (?, ?, ?, ?, ?);
            ''', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()
