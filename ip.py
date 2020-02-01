import getpass
from requests import get

class Ip:

    def __init__(self):
        self.user = getpass.getuser()
        try:
            self.ip = get('https://api.ipify.org').text
        except:
            self.ip = ""
    
    def ip(self):
        return self.ip

    def user(self):
        return self.user
    