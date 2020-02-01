import pyscreenshot as ImageGrab
import base64
import os

class Screenshot:

    def __init__(self):
        imagem = ImageGrab.grab()
        imagem.save('screenShot.jpg', 'jpeg')
        with open("screenShot.jpg", "rb") as imageFile:
            self.img = base64.b64encode(imageFile.read())
        os.remove("screenShot.jpg")

    def img_base64(self):
        return self.img