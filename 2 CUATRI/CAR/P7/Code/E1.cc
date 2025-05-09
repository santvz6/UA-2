#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {

    long long N  = 10000000000; // 10 000 millones
    double suma = 0.0;
    double start, end;
    
    for (int num_hilos = 1; num_hilos <= 8; num_hilos *= 2) {
        suma = 0.0;
        start = omp_get_wtime();
        
        #pragma omp parallel for num_threads(num_hilos) reduction(+:suma)
        for (long long i = 0; i < N; i++) {
            suma += (i * 1.5) / (i + 1.0);
        }
        
        end = omp_get_wtime();

        printf("Resultado final (%i hilos): %2f\n", num_hilos, suma);
        printf("Tiempo: %f segundos\n", end - start);
    }

    return 0;
}