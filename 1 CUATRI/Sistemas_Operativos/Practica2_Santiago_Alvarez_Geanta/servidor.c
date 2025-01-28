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


int bytesLeidos;
char buffer[1024];


void tratarPeticion(int sCliente) {

    // Abrimos archivo .HTML -> obtenemos su descriptor de Archivos
    int archivoPedido = open("Google.html", O_RDONLY);

    // Leemos el descriptor de archivo almacenando su informacion en el buffer
    while ((bytesLeidos = read(archivoPedido, buffer, sizeof(buffer))) > 0) {
        // Enviamos el contenido del buffer al socketCliente
        send(sCliente, buffer, bytesLeidos, 0);
    }
}

void procesarCliente(int sCliente) {
    tratarPeticion(sCliente); 
    close(sCliente);   // Tratada la petición cerramos nuestro socketCliente
}

void ServidorHTTP() {

    int ss;         // Socket Server
    int sCliente;   // Socket Cliente (temporal)
    int numClientesAtendidos = 1;

    struct sockaddr_in server_addr;         // Dirección del servidor
    server_addr.sin_family = AF_INET;       // IPv4
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(9999);     // Puerto 9999

    struct sockaddr_in client_addr;             // Dirección del cliente
    socklen_t client_len = sizeof(client_addr); // Tamaño de la dirección del cliente

    // Creación del socket, devuelve el descriptor del socket
    ss = socket(AF_INET, SOCK_STREAM, 0);
    if (ss < 0) {
        perror("Error en socket() servidorHTTP()\n");
        exit(1);
    }

    // Asociamos el socket con la dirección IP y puerto
    if (bind(ss, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error en bind() servidorHTTP()\n");
        exit(1);
    }

    // Disponibilidad para recibir peticiones de servicio
    if (listen(ss, numClientesAtendidos) < 0) {
        perror("Error en listen() servidorHTTP()\n");
        exit(1);
    }

    while(1) {
        // Aceptamos la conexión entrante
        sCliente = accept(ss, (struct sockaddr*)&client_addr, &client_len);

        if (sCliente < 0) {
            perror("Error en accept() servidorHTTP()\n");
            continue;
        } else {
            printf("Cliente conectado\n");
        }

        pid_t pid = fork();
        if (pid == 0) {
            close(ss); // Ya no necesitamos el socket de escucha
            procesarCliente(sCliente);
            exit(0);
        }
        else{
            close(sCliente);
        }
    }
    close(ss);
}

int main() {
    ServidorHTTP();
    return 0;
}
