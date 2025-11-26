import socket

HOST = '127.0.0.1'
PORT = 5001
FILENAME = 'File.txt'

# Створюємо файл для тесту та записуємо в нього текст "Success"
with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write("Success")

print(f"Preparing to send file: {FILENAME}")

# Створюємо сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Підключаємось до сервера
    s.connect((HOST, PORT))
    print("Connected to server.")

    # Відкриваємо файл у бінарному режимі читання
    with open(FILENAME, 'rb') as f:
        # Відправляємо весь файл через сокет
        s.sendfile(f)

# Виводимо повідомлення про успішне виконання
print("Sending successful")