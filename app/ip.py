import getpass
from requests import get

class Ip:

    def __init__(self):
        self.user = getpass.getuser()

        try:
            self.ip = get('https://api.ipify.org').text
        except:
            self.ip = ""
    
    def get_ip(self):
        return self.ip

    def get_user(self):
        return self.user
    