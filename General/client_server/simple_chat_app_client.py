import socket

def start_client(host='127.0.0.1', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f'Connected to server at {host}:{port}')
    
    while True:
        message = input('You: ')
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Server: {data.decode()}')

    client_socket.close()

if __name__ == '__main__':
    start_client()
