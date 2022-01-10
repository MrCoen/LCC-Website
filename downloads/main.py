import socket
import time
import threading
import termcolor
from termcolor import colored
from pyfiglet import Figlet
from queue import Queue
from colorama import Fore, Back
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

f = Figlet(font='standard')
print(colored(f.renderText('TJs Port Scanner'),'cyan'))

target = input(Fore.MAGENTA + 'Enter the host to be scanned: ' + Fore.RESET)
t_IP = socket.gethostbyname(target)
print('Starting scan on host: ', t_IP)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 65000):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)