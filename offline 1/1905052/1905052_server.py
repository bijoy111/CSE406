import socket
import threading

s = socket.socket() # a socket object is created
port = 12345 # a port is created on which incoming connections will be listened
s.bind(('', port)) # Bind to the port
s.listen(5) # the socket is in now into listening mode
connected_clients = [] # a list to hold connected clients

# a function is created below to handle each client separately
def handle_client(client_socket, client_address):
    connected_clients.append(client_socket)
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print("Received from", client_address, ":", data)
        # Send received message to all other connected clients except the sender
        for client in connected_clients:
            if client != client_socket:
                client.send(data.encode())
    client_socket.close()
    connected_clients.remove(client_socket)

# a function is created below to accept incoming connections
def accept_connections():
    while True:
        client, addr = s.accept()
        print('Got connection from', addr)
        client_handler = threading.Thread(target=handle_client, args=(client, addr))
        client_handler.start()

# start accepting connections
accept_connections()