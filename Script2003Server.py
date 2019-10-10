import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 5150
server.bind((host, port))
server.listen(5)
print('Listening for a client...')
client, addr = server.accept()
print('Accepted connection from:', addr)
client.send(str.encode('Welcome to my server!'))
while True:
    data = client.recv(1024)
    if (bytes.decode(data) == 'exit'):
       break
    else:
       print('Received data from client:', bytes.decode(data))
       client.send(data)
print('Ending the connection')
client.send(str.encode('exit'))
client.close()