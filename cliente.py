import socket

def Main():
    # Dirección IP o nombre DNS del servidor
    servidor = "localhost"
    # Puerto de conexión por socket al servidor
    puerto = 8089
    
    # Definimos el objeto socket    
    obSocket = socket.socket()
    # Preparamos la conexión
    obSocket.connect((servidor, puerto))
    textoUsuario = "Introduzca un mensaje para enviar al servidor (introduce 'q' para salir): "
    mensaje = input(textoUsuario)
    # Mientras no se introduzca "q" pediremos al usuario que introduzca mensajes
    while mensaje.upper() != "Q":
        # Codificamos el mensaje y lo enviamos por socket al servidor
        obSocket.send(mensaje.encode())
        # Recibimos un posible mensaje desde el servidor
        datosRecibidos = obSocket.recv(1024).decode()
        # Mostramos el mensaje recibido desde el servidor
        print(f"Mensaje recibido del servidor: {str(datosRecibidos)}")
        # Volvemos a pedir al usuario que introduzca un mensaje
        mensaje = input(textoUsuario)
    
    # Cerramos la conexión
    obSocket.close()

if __name__ == "__main__":
    Main()