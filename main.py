import sqlite3

# Função para conectar ao banco de dados
def connect():
    conn = sqlite3.connect('pessoas.db')
    return conn

# Função para criar uma tabela
def create_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        ''')

# Função para inserir dados
def insert_person(conn, name, age):
    with conn:
        conn.execute('''
            INSERT INTO person (name, age) VALUES (?, ?)
        ''', (name, age))

# Função para ler dados
def read_people(conn):
    with conn:
        cursor = conn.execute('SELECT * FROM person')
        for row in cursor:
            print(row)

# Função para atualizar dados
def update_person(conn, person_id, name, age):
    with conn:
        conn.execute('''
            UPDATE person SET name = ?, age = ? WHERE id = ?
        ''', (name, age, person_id))

# Função para deletar dados
def delete_person(conn, person_id):
    with conn:
        conn.execute('''
            DELETE FROM person WHERE id = ?
        ''', (person_id,))

# Função principal
def main():
    conn = connect()
    create_table(conn)

    # Inserir algumas pessoas
    insert_person(conn, 'Alice', 30)
    insert_person(conn, 'Bob', 25)

    # Ler e imprimir todas as pessoas
    print('Pessoas antes da atualização:')
    read_people(conn)

    # Atualizar uma pessoa
    update_person(conn, 1, 'Alice', 31)

    # Ler e imprimir todas as pessoas após a atualização
    print('Pessoas após a atualização:')
    read_people(conn)

    # Deletar uma pessoa
    delete_person(conn, 2)

    # Ler e imprimir todas as pessoas após a exclusão
    print('Pessoas após a exclusão:')
    read_people(conn)

    # Fechar a conexão
    conn.close()

if __name__ == '__main__':
    main()
