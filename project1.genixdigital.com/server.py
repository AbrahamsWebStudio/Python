import socket 

s = socket.socket()
print("Socket successfully created")

s.bind(('localhost', 31001))

s.listen(3)
print("Waiting fo connections...")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('Got connection from', addr, name)

    c.send(bytes('W3LC0ME. Thank you for connecting', 'utf-8'))
    
    c.close()