import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))  # Привязываем сокет к адресу и порту
server_socket.listen(5) 

print("Сервер запущен. Ожидание клиентских подключений...")

while True:
    client_socket, addr = server_socket.accept()  # Принимаем соединение от клиента
    print("Подключено:", addr)

    data = client_socket.recv(1024).decode()  # Получаем данные от клиента (максимум 1024 байта)
    
    try:
        json_data = json.loads(data)
        is_valid_json = True
    except json.JSONDecodeError:
        is_valid_json = False

    # Отправляем ответ клиенту 
    client_socket.send(str(is_valid_json).encode())

    client_socket.close()  # Закрываем соединение с клиентом
