#Реализуйте клиент — серверное приложение, позволяющее обмениваться сообщениями в формате один к
#одному. Для начала общения необходимо установить
#соединение. После соединение используется текстовый
#формат. В беседе участвуют только два человека. После
#завершения беседы сервер переходит к ожиданию нового
#участника разговора.

import socket
import threading
def handle_client(conn, address):
    print(f'Connect client {address}')
    while True:
        date = conn.recv(1024).decode(encoding='utf-8')
        if date == False:
            break
        print(f'Messag from {address}: {date}')
        for client in clients_list:
            if client != conn:
                client.sendall((date + '\n').encode())

host = '127.0.0.1'
port = 3000
clients_list = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    print(f'server {host} runer')
    s.listen(5)
    while True:
        conn, address = s.accept()
        clients_list.append(conn)
        threading.Thread(target=handle_client, args=(conn, address)).start()
        print('Ожидание следующего клиента')

