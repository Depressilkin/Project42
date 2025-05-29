import socket

host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    welcom = s.recv(1024).decode(encoding='utf-8')
    print(welcom)
    while True:
        message = input('Input city')
        s.sendall(message.encode())
        if message == False:
            break
        response = s.recv(1024).decode(encoding='utf-8')
        print(response)
    print('Disconnect')
