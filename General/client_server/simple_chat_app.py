import socket

def start_server(host='127.0.0.1', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Server started at {host}:{port}')
    conn, addr = server_socket.accept()
    print(f'Connection from {addr}')
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f'Client: {data.decode()}')
        message = input('You: ')
        conn.sendall(message.encode())

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    start_server()


