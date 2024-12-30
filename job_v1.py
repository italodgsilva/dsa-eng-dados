import csv
import sqlite3

# Cria um novo banco de dados
conn=sqlite3.connect('dsabd.db')

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

# Grava e fecha a conexão
conn.commit()
conn.close()

# Abre o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r', encoding='utf-8') as file:

    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta no banco de dados
    conn = sqlite3.connect('dsabd.db')

    # Insere cada linha do arquivo na tabela do banco de dados
    for row in reader:
        conn.execute('''
            INSERT INTO producao (produto, quantidade, preco_medio, receita_total)
            VALUES (?, ?, ?, ?);
        ''', row)

    conn.commit()
    conn.close()
