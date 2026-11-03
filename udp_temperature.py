import socket

choice = input("Enter 's' for Server or 'c' for Client: ")

if choice == 's':

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 6000))

    print("UDP Server Listening...")

    while True:
        data, addr = server.recvfrom(1024)
        print("Temperature Received:", data.decode())

elif choice == 'c':

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    temp = input("Enter Temperature Reading: ")

    client.sendto(temp.encode(), ("localhost", 6000))

    print("Temperature Sent")

    client.close()
