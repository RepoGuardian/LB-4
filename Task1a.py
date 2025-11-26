import socket

# Задаємо адресу сервера
HOST = '127.0.0.1'
PORT = 1024

# Створюємо сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Встановлюємо з'єднання
    s.connect((HOST, PORT))

    # Формуємо тестове повідомлення
    message = "Testing Socket API."
    print(f"Sending: {message}")

    # Відправляємо закодовані дані
    s.sendall(message.encode())

    # Отримуємо відповідь від сервера
    data = s.recv(1024)

# Виводимо отриману відповідь
print(f"Received: {data.decode()}")