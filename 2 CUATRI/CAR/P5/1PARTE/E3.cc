#include <stdio.h>
#include <omp.h>

#define N 10

int main() {
    int array[N] = {0};

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        printf("Hilo %d escribiendo %d en la posición %d\n", id, id + 1, id);
        printf("Hilo %d leyendo la posición 5: %d\n", id, array[5]);
    }

    for (int i = 0; i < N; i++) array[i] = 0;
    printf("\n------------------\n\n");

    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        array[id] = id + 1;
        printf("Hilo %d escribió %d en la posición %d\n", id, id + 1, id);

        #pragma omp barrier
        printf("Hilo %d lee la posición 5: %d\n", id, array[5]);
    }

    return 0;
}
