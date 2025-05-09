#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {

    long long N  = 10000000000; // 10 000 millones
    double start, end;
    double suma = 0.0;
    
    for (int num_hilos = 1; num_hilos <= 8; num_hilos *= 2) {
        printf("\nEjecutando con %d hilos:\n", num_hilos);
        suma = 0.0;
        start = omp_get_wtime();
            
        #pragma omp parallel for num_threads(num_hilos) reduction(+:suma)
        for (long long i = 0; i < N*num_hilos; i++) {
            suma += 1;
        }
            
        end = omp_get_wtime();
    
        printf("Resultado final (%i hilos): %2f\n", num_hilos, suma);
        printf("Tiempo: %f segundos\n", end - start);
    }    
}