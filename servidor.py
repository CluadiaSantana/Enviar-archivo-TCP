import socket


# se crea el socket para el servidor
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#se pone el host de mi localhost y el port 5500 (es el que tengo configurado) tambien se pone que archivo se enviara
host="127.0.0.1"
port=5500
CHUNK_SIZE = 5 * 1024
FILE = "Hello.jpg"
#se le asigna al servidor el host y el puerto
serversocket.bind((host,port))
#se configura para que empiece a escuchar
serversocket.listen(3)
print(f'El servidor esta escuchando en {host} puerto {port}')
while True: #siempre se estara escuchando
    # se aceptan conexiones del exterior
    (clientsocket, address) = serversocket.accept()
    print(f'Se ha conectado con el cliente {address}')
    with clientsocket:
        #se manda el archivo
        with open(FILE, 'rb') as f:
            clientsocket.sendfile(f)
            print("El archivo se ha enviado")
    