import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))  # Подключаемся к серверу

# Получаем строку от пользователя
json_string = input("Введите JSON-строку для валидации: ")
#json_string = '{"name": "Андрей", "age": 22, "city": "NN"}'
# Отправляем строку на сервер
client_socket.send(json_string.encode())

# Получаем ответ от сервера
response = client_socket.recv(1024).decode()

if response == 'True':
    print("Строка является валидным JSON.")
else:
    print("Строка не является валидным JSON.")

client_socket.close()  # Закрываем соединение с сервером
