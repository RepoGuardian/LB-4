import socket

# Задаємо хост та порт
HOST = '127.0.0.1'
PORT = 1024

# Створюємо сокет (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Прив'язуємо сокет до адреси та порту
    s.bind((HOST, PORT))

    # Запускаємо прослуховування (черга до 1 з'єднання)
    s.listen()
    print(f"Echo Server running on {HOST}:{PORT}")

    # Запускаємо нескінченний цикл для постійної роботи сервера (Завдання 2)
    while True:
        # Приймаємо з'єднання від клієнта
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                # Отримуємо дані (порціями по 1024 байти)
                data = conn.recv(1024)
                if not data:
                    break
                # Відправляємо отримані дані назад клієнту (Echo)
                conn.sendall(data)