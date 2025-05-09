#include <mpi.h>
#include <stdio.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, max_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    MPI_Reduce(&rank, &max_rank, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);
    
    if (rank == 0) {
        printf("El máximo de los ranks es: %d\n", max_rank); 
    }

    MPI_Finalize();
    return 0;
}
