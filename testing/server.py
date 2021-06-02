import socket
import time

s = socket.socket()
print("Server socket created")

port = 1446

s.bind(('', port))
print("Server bound to %s" %(port))

s.listen(5)
print("Server now listening")

while True:
    c, addr = s.accept()
    print('Started a connection with ', addr)
    c.send(b'This is the result of your connection.')
    c.close()
    time.sleep(60)