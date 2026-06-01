import mysql.connector
from mysql.connector import Error

def conectar_banco():
    #Estabelece conexão
    try: #tentar conectar
        conexao = mysql.connector.connect (
            host="localhost",
            user="root",
            password="root",
            database="parque_diversoes"
        )
        if conexao.is_connected():
            print("Conectou")
            return conexao
    except Error as erro:
        print(f'Error ao conectar: {erro}')
        return None
    
    def cadastrar_atracao():
        #Inserir novas atrações no parque
        conexao_aberta = conectar_banco()
        if conexao_aberta:
            cursor= conexao_aberta.cursor()
            nome= input("Nome da Atraçao: ")
            status= input("Status (Funcionando/Manutenção)")
            sql = "INSET INTO atracoes (nome, status) VALUES (%s, %s)"
            dados = (nome, status)
            try:
                cursor.execute(sql, dados)
                conexao_aberta.commit()
                print(f'{nome} cadastrado com sucesso!')
            except Error as erro:
                print(f"Erro ao cadastrar: {erro}")
            finally:
                cursor.close()
                conexao_aberta.close()
        conexao_aberta.close()

cadastrar_atracao()