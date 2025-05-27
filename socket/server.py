#Реализуйте клиент — серверное приложение, позволяющее обмениваться сообщениями в формате один к
#одному. Для начала общения необходимо установить
#соединение. После соединение используется текстовый
#формат. В беседе участвуют только два человека. После
#завершения беседы сервер переходит к ожиданию нового
#участника разговора.

import socket
def handle_client(conn, address):
    print(f'Connect client {address}')
    conn.sendall('Hello!'.encode())
    while True:
        date = conn.recv(1024).decode(encoding='utf-8')
        if date == False:
            print('Disconnect')
            break
        print(f'Messag from {address}: {date}')
        response = input('Input response to client')
        conn.sendall((response + '\n').encode())



host = '127.0.0.1'
port = 3000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print(f'server {host} runer')
    s.listen(3)
    while True:
        conn, address = s.accept()
        handle_client(conn, address)
        print('Ожидание следующего клиента')

