#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#include <fcntl.h> // Read
#include <string.h> // Write

int main(int argc, char *argv[]) {

    int pipe_v[2];  // Array de 2 espacios
                    // [0] > lectura, [1] > escritura

    __pid_t pid;
    const int BUFFER_SIZE = 1024;
    char buffer[BUFFER_SIZE];
    ssize_t bytesLeidos;



    // Crear la tubería
    if (pipe(pipe_v) == -1) {
        perror("pipe");
    }

    pid = fork();
    switch (pid){
        case -1:
            perror("No se ha podido crear el proceso hijo\n");
            break;

        // El hijo escribe
        case 0:
            close(pipe_v[1]);  // Cerramos el extremo de escritura de la tubería

            // argv[2] > parámetro archivo destino
            int archivoDest = open(argv[2], O_WRONLY | O_TRUNC, 0644);
            if (archivoDest == -1){
                printf("No se ha podido abrir el archivo destino\n");
                printf("Creando nuevo archivo destino: %s\n", argv[2]);
                archivoDest = creat(argv[2], 0644);
                if (archivoDest < 0) {
                    perror("Error al crear el archivo destino");
                    exit(1);
                }
            }


            // El buffer tiene que ser mayor o igual al tamaño leido
            while ((bytesLeidos = read(pipe_v[0], buffer, BUFFER_SIZE)) > 0)
                write(archivoDest, buffer, bytesLeidos);

            close(pipe_v[0]);
            close(archivoDest);
            exit(1);

        // El padre lee
        default:
            close(pipe_v[0]);  // Cerramos el extremo de lectura de la tubería

            int archivoOrigen = open(argv[1], O_RDONLY);
            if (archivoOrigen == -1) {
                 perror("No se ha podido abrir el archivo origen\n");
            }

            while ((bytesLeidos = read(archivoOrigen, buffer, BUFFER_SIZE)) > 0)
                write(pipe_v[1], buffer, bytesLeidos);


            close(pipe_v[1]);
            close(archivoOrigen);

            // Esperar a que el proceso hijo termine
            wait(NULL);
    }
    return 0;
}