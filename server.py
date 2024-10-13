# server.py
import socket
import random

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(2)  # Listen for up to 2 connections

connections = []

while len(connections) < 2:
    conn, addr = sock.accept()
    connections.append(conn)
    print('Connected:', addr)
    if len(connections) == 1:
        connections[0].send(b'wait')  # Tell the first client to wait


# Randomly assign X and O
random.shuffle(connections)
connections[0].send(b'start_X')
connections[1].send(b'start_O')


def handle_client(conn, opponent):
    while True:
        try:
            data = conn.recv(1024).decode()
            print(data)  # Debug output (optional)
            opponent.send(data.encode())  # Forward data to the opponent
            if 'gamover' in data or 'won' in data or 'nichya' in data:  # Basic game-end check
                break 
        except (ConnectionResetError, ConnectionAbortedError, OSError):
             break  # handle disconnect



# Use threads to manage players concurrently
import threading

t1 = threading.Thread(target=handle_client, args=(connections[0], connections[1]))
t2 = threading.Thread(target=handle_client, args=(connections[1], connections[0]))
t1.start()
t2.start()

t1.join()
t2.join()

print("Game over. Closing server.") # Close connections when threads are finished
for conn in connections:
    conn.close()

sock.close()



