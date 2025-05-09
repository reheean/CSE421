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
                connection.send("Goodbye! It was nice meeting you!".encode(format))
                print("Terminating connection with the client", address)
                connected = False
            else:
                try:
                    salary = 0
                    if int(message) <= 40:
                        salary = int(message) * 200
                        
                    else:
                        salary = 8000 + (int(message) - 40) * 300
                    connection.send(f"Total Salary is {salary}".encode(format))
                except ValueError:
                    connection.send("Invalid input. Please enter a valid number of hours.".encode(format))
                    
    connection.close()