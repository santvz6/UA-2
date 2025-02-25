#include <stdio.h>
#include <omp.h>

#define N 1000000

int main() {
    long long suma = 0;
    double start, end;

   
    suma = 0;
    start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        suma += 1;  // Condición de carrera 
    }
    end = omp_get_wtime();
    printf("Sin protección - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);


    suma = 0;
    start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        #pragma omp atomic
        suma += 1;
    }
    end = omp_get_wtime();
    printf("Con atomic - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);


    suma = 0;
    start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        #pragma omp critical
        {
            suma += 1;
        }
    }
    end = omp_get_wtime();
    printf("Con critical - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);

    return 0;
}
