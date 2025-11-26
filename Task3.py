import socket

# Задаємо хост та порт (відмінний від Echo-сервера)
HOST = '127.0.0.1'
PORT = 5001

# Створюємо сокет (IPv4, TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Прив'язуємо сокет до адреси та порту
    s.bind((HOST, PORT))
    # Запускаємо прослуховування вхідних з'єднань
    s.listen()
    print(f"File Server running on {HOST}:{PORT}")

    while True:
        # Приймаємо з'єднання від клієнта
        conn, addr = s.accept()
        with conn:
            print(f"Client connected: {addr}")

            # Відкриваємо файл для запису байтів (створюється новий файл)
            with open('File_received.txt', 'wb') as f:
                while True:
                    # Отримуємо дані з потоку (порціями по 1024 байти)
                    data = conn.recv(1024)
                    if not data:
                        # Перериваємо цикл, якщо дані закінчилися
                        break
                    # Записуємо отримані дані у файл
                    f.write(data)

            print("File received and saved as 'File_received.txt'.")