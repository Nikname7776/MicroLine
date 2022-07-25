import socket

LOCALHOST = '127.0.0.1'
PORT = 1488

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Connect...")
    s.bind((LOCALHOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(4096)
            res = data.decode("utf-8").upper()
            print("Принято к обработке: " + res)
            conn.sendall(bytes(res, "utf-8"))
