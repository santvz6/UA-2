#include <stdio.h>
#include <omp.h>

#define N 1000000

int main() {
    long long suma = 0;
    double start, end;

  
    start = omp_get_wtime();
    for (int i = 1; i <= N; i++) {
        suma += i;
    }
    end = omp_get_wtime();
    printf("Secuencial - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);

   
    suma = 0;
    start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 1; i <= N; i++) {
        suma += i; 
    }
    end = omp_get_wtime();
    printf("Paralela sin reduction - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);


    suma = 0;
    start = omp_get_wtime();
    #pragma omp parallel for reduction(+:suma)
    for (int i = 1; i <= N; i++) {
        suma += i;
    }
    end = omp_get_wtime();
    printf("Paralela con reduction - Suma: %lld, Tiempo: %f segundos\n", suma, end - start);

    return 0;
}
