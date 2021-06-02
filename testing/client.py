import socket
import time

s = socket.socket()

port = 1446

s.connect(('127.0.0.1', port))

print(s.recv(1024))

s.close()

time.sleep(60)