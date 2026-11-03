import socket

choice = input("Enter 's' for Server or 'c' for Client: ")

if choice == 's':
    results = {
        "101": "PASS - 85%",
        "102": "PASS - 78%",
        "103": "FAIL",
        "104": "PASS - 91%"
    }

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)

    print("Server waiting for connection...")

    conn, addr = server.accept()
    print("Connected:", addr)

    reg_no = conn.recv(1024).decode()

    result = results.get(reg_no, "Register Number Not Found")

    conn.send(result.encode())

    conn.close()
    server.close()

elif choice == 'c':

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(("localhost", 5000))

    reg_no = input("Enter Register Number: ")

    client.send(reg_no.encode())

    result = client.recv(1024).decode()

    print("Result:", result)

    client.close()
