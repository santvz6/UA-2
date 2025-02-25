#include <stdio.h>
#include <omp.h>

int main() {
    int contador = 0;
    int N = 10000;
    double end;
    
    double start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        contador += 1;  // Condición de carrera aquí
    }
    end = omp_get_wtime();
    printf("Sin atomic - Valor de contador: %d, Tiempo: %f segundos\n", contador, end - start);

    
    contador = 0;
    start = omp_get_wtime();
    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        #pragma omp atomic
        contador += 1;
    }
    end = omp_get_wtime();
    printf("Con atomic - Valor de contador: %d, Tiempo: %f segundos\n", contador, end - start);

    return 0;
}
