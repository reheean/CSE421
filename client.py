import socket
format ='utf-8'
port = 5050
data = 16
hostname = socket.gethostname()
host_address = socket.gethostbyname(hostname)
server_socket_address = (host_address, port)
disconnected_message = "off"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)

def message_to_send(message):
    message = message.encode(format)
    message_length = len(message)
    send_length = str(message_length).encode(format)
    send_length += b' ' * (data - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(format))

while True:
    temp = input("Enter message: ")
    if temp == disconnected_message:
        message_to_send(disconnected_message)
        break
    else:
        message_to_send(temp)