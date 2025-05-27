import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # создание сокета с протоколом и типом подключения
    host = '127.0.0.1'
    port = 5000
    s.bind((host, port)) # Связывание с адресом
    print(f'server {host} runer')
    s.listen() #Прослушивание и установление соединения
    conn, address = s.accept() # Клиент инициирует соединение с сервером
    while True:
        date = conn.recv(1024)
        if date == False:
            break
        conn.sendall(date)

    

