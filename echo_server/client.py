import socket

SERVER = '127.0.0.1'
PORT = 1488

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    out_data = input("Введите текст: ")
    client.sendall(bytes(out_data, 'UTF-8'))
    print('Отправлено: ' + str(out_data))
    in_data = client.recv(4096)
    print("Возвращено: " + in_data.decode())
