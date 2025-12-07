#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define VALORES_POR_PROCESO 5
#define UMBRAL 50

double calcularMedia(int *datos, int n) {
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += datos[i];
    }
    return (double)suma / n;
}

int main(int argc, char *argv[]) {
    int rank, size;
    int *datos = NULL;       
    int totalElementos;
    int *localDatos;
    double localMedia;
    double *mediasLocales = NULL;
    double t_inicial, t_final;

    // Inicialización del entorno MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    totalElementos = VALORES_POR_PROCESO * size;

    // Verificación de que el número de elementos sea múltiplo del número de procesos
    if(totalElementos % size != 0) {
        if(rank == 0) {
            fprintf(stderr, "El número total de elementos (%d) debe ser múltiplo de la cantidad de procesos (%d).\n", totalElementos, size);
        }
        MPI_Finalize();
        exit(EXIT_FAILURE);
    }

    // Reserva de memoria para los datos locales en cada proceso
    localDatos = (int *)malloc(VALORES_POR_PROCESO * sizeof(int));
    if(localDatos == NULL) {
        fprintf(stderr, "Error al asignar memoria en el proceso %d.\n", rank);
        MPI_Finalize();
        exit(EXIT_FAILURE);
    }

    // El proceso 0 genera los datos aleatorios
    if(rank == 0) {
        datos = (int *)malloc(totalElementos * sizeof(int));
        if(datos == NULL) {
            fprintf(stderr, "Error al asignar memoria en el proceso 0.\n");
            MPI_Finalize();
            exit(EXIT_FAILURE);
        }
        srand(time(NULL));
        printf("Datos generados:\n");
        for (int i = 0; i < totalElementos; i++) {
            datos[i] = rand() % 101; // Números aleatorios entre 0 y 100
            printf("%d ", datos[i]);
        }
        printf("\n");
    }

    // Sincronización antes de iniciar el conteo de tiempo
    MPI_Barrier(MPI_COMM_WORLD);
    t_inicial = MPI_Wtime();

    // Distribución de los datos a todos los procesos
    MPI_Scatter(datos, VALORES_POR_PROCESO, MPI_INT, localDatos, VALORES_POR_PROCESO, MPI_INT, 0, MPI_COMM_WORLD);

    // Cada proceso calcula la media local de sus datos
    localMedia = calcularMedia(localDatos, VALORES_POR_PROCESO);

    // El proceso 0 reserva memoria para las medias locales recibidas
    if(rank == 0) {
        mediasLocales = (double *)malloc(size * sizeof(double));
        if(mediasLocales == NULL) {
            fprintf(stderr, "Error al asignar memoria para las medias en el proceso 0.\n");
            MPI_Finalize();
            exit(EXIT_FAILURE);
        }
    }

    // Se recogen las medias locales en el proceso 0
    MPI_Gather(&localMedia, 1, MPI_DOUBLE, mediasLocales, 1, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Sincronización previa al análisis final
    MPI_Barrier(MPI_COMM_WORLD);

    // El proceso 0 analiza las medias y verifica el umbral crítico
    if(rank == 0) {
        printf("\nMedias locales por proceso:\n");
        for(int i = 0; i < size; i++) {
            printf("Proceso %d: %f\n", i, mediasLocales[i]);
        }

        // Verifica si alguna media supera el umbral
        int alerta = 0;
        printf("\nProcesos que superan el umbral de %d:\n", UMBRAL);
        for(int i = 0; i < size; i++) {
            if(mediasLocales[i] > UMBRAL) {
                printf("¡Alerta! Proceso %d con media %f\n", i, mediasLocales[i]);
                alerta = 1;
            }
        }
        if(!alerta) {
            printf("Ningún proceso supera el umbral crítico.\n");
        }
        t_final = MPI_Wtime();
        printf("\nTiempo total de ejecución: %f segundos\n", t_final - t_inicial);
    }

    // Liberación de memoria
    if(datos) free(datos);
    if(localDatos) free(localDatos);
    if(mediasLocales) free(mediasLocales);

    // Finalización del entorno MPI
    MPI_Finalize();
    return 0;
}
