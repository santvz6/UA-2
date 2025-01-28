// SOCKET
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>

// READ & WRITE
#include <fcntl.h>
#include <string.h>

// PROCESOS
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

// INET_ADDR()
#include <arpa/inet.h>

void ClienteHTTP(char *dirIP, int puerto, char *recurso) {

    int sc; // Socket Clientes 

    // Variables de Read - Write
    int bytesLeidos;
    char buffer[1024];

    // reutiliza una dirección de red asociada a un socket
    static struct sockaddr_in sa; 

    // Configuración de la dirección del servidor
    sa.sin_family = AF_INET;          
    sa.sin_addr.s_addr = inet_addr(dirIP);
    sa.sin_port = htons((uint16_t)puerto);



    // Crear el socket cliente
    sc = socket(AF_INET, SOCK_STREAM, 0);
    if (sc < 0) {
        perror("Error al crear el socket clienteHTTP\n");
        exit(1);
    }

    

    // Coenctamos el cliente con la dirección IP del servidor: (descriptor socket, dirección servidor,longitud)
    if (connect(sc, (struct sockaddr *)&sa, sizeof(sa)) < 0) {
        perror("Error al conectar con el servidor\n");
        close(sc);
        exit(1);
    } else {
        printf("Conexión establecida\n");
    }


    // Tiempo dónde el servidor esta realizando la petición GET


    // Leemos el contenido escrito en el Socket del cliente
    while ((bytesLeidos = read(sc, buffer, sizeof(buffer))) > 0) {
        printf("%s", buffer);
    }

    // Finalizamos el cliente
    close(sc);
}

int main() {
    // Iniciar cliente
    char *dirIP = "127.0.0.1";
    int puerto = 9999;
    char *recurso = "/Google.html";

    ClienteHTTP(dirIP, puerto, recurso);
    return 0;
}
