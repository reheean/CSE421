import socket
format ='utf-8'
port = 5050
data = 16
hostname = socket.gethostname()
host_address = socket.gethostbyname(hostname)
server_socket_address = (host_address, port)
disconnected_message = "off"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)
server.listen()
print(f"Server is listening!")

while True:
    connection, address = server.accept()
    print(f"Client {address} has connected to the server.".encode(format))

    connected = True
    while connected:
        initial_message = connection.recv(data).decode(format)
        print(f"Length of the message is ", initial_message)

        if initial_message:
            message_length = int(initial_message)
            message = connection.recv(message_length).decode(format)
            if message == disconnected_message:
                connection.send("Goodbye! It was nice meeting you!")
                print("Terminating connection with the client", address)
                connected = False
            else:
                vowel = "aeiouAEIOU"
                count = 0
                for i in message:
                    if i in vowel:
                        count += 1
                if count == 0:
                    connection.send("Not Enough Vowels I Guess".encode(format))
                elif count <= 2:
                    connection.send("Enough Vowels I Guess". encode(format))
                else:
                    connection.send("Too Many Vowels". encode(format))
                    
    connection.close()