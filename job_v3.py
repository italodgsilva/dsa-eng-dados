# Carregar somente registros com quantidade produzida superior a 10
# Remover ponto na última coluna para evitar valores truncados.

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
            receita_total INTEGER
        );
    '''
    )

    # Insere cada linha do arquivo na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            row[3] = row[3].replace('.', '')
            conn.execute('''
                INSERT INTO producao (produto, quantidade, preco_medio, receita_total)
                VALUES (?, ?, ?, ?);
            ''', row)

    conn.commit()
    conn.close()
