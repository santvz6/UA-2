#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    
    int rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    int dato;
    
    if (rank == 2) {
        dato = 100;
    }

    MPI_Bcast(&dato, 1, MPI_INT, 2, MPI_COMM_WORLD); 
    
    dato++; 
    printf("Proceso %d recibió: %d\n", rank, dato); 
    
    MPI_Finalize();
    return 0;
}
