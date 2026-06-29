import socket
import threading
from queue import Queue

target = input("Introduce la IP o dominio: ")
queue = Queue()

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Puerto {port} abierto")

        sock.close()
    except:
        pass

def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()

for port in range(1, 1025):
    queue.put(port)

threads = []

for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

queue.join()

print("Escaneo completado.")