import socket
import random

sock = socket.socket()
sock.bind(('', 9090))
sock.listen()

players = []
users = []
for i in range(2):
    conn, addr = sock.accept()
    users.append(conn)
    print ('connected:', addr)
    if len(users) == 1:
        users[0].send(b'wait')
    else:
        r = random.randint(0,1)
        if r == 0:
            users[0].send(b'start_X')
            users[1].send(b'start_O')
            i=0
        else:
            users[1].send(b'start_X')
            users[0].send(b'start_O')
            i=1

    
while True:
    
    
    if i % 2 == 0:
        data = users[0].recv(1024).decode()
        
        print(str(data) + ' ot 1')
        users[1].send(data.encode())
    else:
        data = users[1].recv(1024).decode()
        print(str(data) + ' ot 2')
        users[0].send(data.encode())
    i += 1



        
conn.close()
