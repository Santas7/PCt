import time, socket, sys

new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)

port = 8080

new_socket.bind((host_name, port))
print("(PCt) The server is started automatically!")
print("This server IP: ", s_ip)

new_socket.listen(5)

conn, add = new_socket.accept()

print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])

client = (conn.recv(1024)).decode()
print(client + ' has connected in chat.')

conn.send("PCt".encode())
while True:
    message = input('<PCt> ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f"<{client}>", ' ', message)
