#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// Uso de Share Memory
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>

#include <time.h> // usasdo para generar números aleatorios



int main() {
    int shmid; // Declaramos el ID de la Memoria Compartida
    int *numeros = NULL; 
    char error[100];
    const int SHM_TAM = 1024; // tamaño de la memoria compartida

    // Para la creación del segmento de memoria utilizamos "shmget()"
    // IPC_PRIVATE: solo los que comparten parentesco acceden
    // Permisos: 6 es para escribir y leer
    if ((shmid = shmget(IPC_PRIVATE, SHM_TAM, 0666)) < 0){
        sprintf(error,"Pid %d: Error al crear el segmento de memoria compartida: ",getpid());
        perror(error);
        exit(1);
    }

    __pid_t pid = fork();

    switch(pid){
        case -1: 
            perror("No se pudo crear el proceso hijo\n");
            exit(1); // salida NO exitosa
    
        case 0:
            // ligamos el segmento de memoria compartida al proceso (usando shmat [share memory attach])

            // NULL → La dirección donde se desea que se incluya. NULL → lo cuál permite que
            // se incluya en cualquier zona libre del espacio de direcciones del proceso  
            // NULL → identificadores de permisos (en la práctica también será NULL).  
            numeros = (int *)shmat(shmid, NULL, NULL);

            // Generamos 10 números aleatorios y los almacenamos en la memoria compartida
            // Como explicó el profesor de Métodos de Inferencia (los números aleatorios se obtienen del resto de una división del tiempo actual)
            printf("Soy el hijo (%d): los números generados son: ",getpid());
            srand(time(NULL));
            for (int i = 0; i < 10; i++){
                numeros[i] = rand() % 100; // Números aleatorios entre 0 y 99
                printf("%d, ", numeros[i]);
            }
            printf("\n");

            // Desligamos el segmento de memoria compartida
            if (shmdt((char *)numeros)<0){
                sprintf(error,"Pid %d: Error al desligar la memoria compartida: ",getpid());
                perror(error);
                exit(1);
            }
            exit(0);

        default:
            wait(NULL); // Una vez generados los números y guardados en la memoria compartida
            // Importante desligar la memoria compartida del proceso hijo

            // ligamos el segmento de memoria compartida al proceso padre
            numeros = (int *)shmat(shmid, NULL, NULL);

            // Leemos los números de la memoria compartida y calculamos la media
            printf("Soy el hijo (%d): los números generados fueron: ",getpid());
            int sum = 0;
            for (int i = 0; i < 10; i++) {
                sum += numeros[i];
                printf("%d, ", numeros[i]);
            }
            printf("\n");
            float media = sum / 10.0;
            printf("La media es de: %f\n", media);

            // Desadjuntmos el segmento de memoria compartida
            if (shmdt((char *)numeros)<0){
                sprintf(error,"Pid %d: Error al desligar la memoria compartida: ",getpid());
                perror(error);
                exit(1);
            }
            
            // shmctl: para realizar un conjunto de operaciones de control sobre una zona de memoria compartida
            // Liberamos el segmento de memoria compartida usando IPC_RMID
            // IPC_RMID: elimina el identificador de memoria compartida especificado por shmid del sistema,
            // destruyendo el segmento de memoria compartida y las estructuras de control asociadas

            if (shmctl(shmid, IPC_RMID, 0)<0){
                sprintf(error,"Pid %d: Error al liberar la memoria compartida: ",getpid());
                perror(error);
                exit(1);
            }
    }

    return 0;
}
