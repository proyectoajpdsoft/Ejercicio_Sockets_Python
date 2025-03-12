import socket

def Main():
    servidor = "localhost"
    puerto = 8089
    
    # Definimos el objeto socket    
    obSocket = socket.socket()
    # Preparamos la conexión
    obSocket.bind((servidor, puerto))
    # Establecemos el número máximo de conexiones permitidas: 1
    obSocket.listen(1)
    print("Servidor iniciado, queda a la escucha de conexiones de clientes...")
    # Dejamos el servidor escuchando peticiones de clientes
    conexion, cliente = obSocket.accept()
    # Cuando un cliente se conecte, mostramos su IP
    print(f"Conexión al sevidor desde cliente: {str(cliente)}")
    # Dejamos la aplicación servidor ejecutándose hasta que se reciba la conexión de un cliente y su mensaje
    while True:
        # Decodificamos los datos recibidos del cliente
        datosRecibidos = conexion.recv(1024).decode()
        # Si no se han recibido datos, o si se recibe "q", cerramos el servidor
        if not datosRecibidos or datosRecibidos.upper() == "Q":
            break
        # Mostramos por consola el mensaje enviado del cliente al servidor
        print(f"Mensaje recibido: {str(datosRecibidos)}")
        # Enviamos al cliente otro mensaje para que sepa que se ha recibido     
        conexion.send(f"Mensaje recibido en el servidor del cliente IP {cliente}".encode())
    
    # Cerramos la conexión del servidor para liberar el uso del puerto
    conexion.close

if __name__ == "__main__":
    Main()