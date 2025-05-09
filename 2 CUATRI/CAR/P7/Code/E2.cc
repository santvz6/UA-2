#include <stdio.h>
#include <omp.h>

int main() {
    long long N = 1000000000; // 1.000 millones
    double suma;
    double start, end;

    for (int hilos = 1; hilos <= 8; hilos *= 2) {
        printf("\nEjecutando con %d hilos:\n", hilos);

        for (int i = 0; i < 3; i++) {
            suma = 0.0; 
            start = omp_get_wtime();
            
            // Configuramos el número de hilos
            omp_set_num_threads(hilos);

            #pragma omp parallel
            {
                if (i == 0) {
                    // Critical
                    #pragma omp for
                    for (long long i = 1; i <= N; i++) {
                        double valor = (i * 1.5) / (i + 1.0);
                        #pragma omp critical
                        {
                            suma += valor;
                        }
                    }
                    end = omp_get_wtime();
                    printf("Método Critical: -> Resultado: %.2f, Tiempo: %f segundos\n", suma, end - start);
                } 
                else if (i == 1) {
                    // Atomic
                    #pragma omp for
                    for (long long i = 1; i <= N; i++) {
                        double valor = (i * 1.5) / (i + 1.0);
                        #pragma omp atomic
                        suma += valor;
                    }
                    end = omp_get_wtime();
                    printf("Método Atomic: -> Resultado: %.2f, Tiempo: %f segundos\n", suma, end - start);
                } 
                else {
                    // Reduction
                    #pragma omp for reduction(+:suma)
                    for (long long i = 1; i <= N; i++) {
                        suma += (i * 1.5) / (i + 1.0);
                    }
                    end = omp_get_wtime();
                    printf("Método Reduction: -> Resultado: %.2f, Tiempo: %f segundos\n", suma, end - start);
                }
            }
        }
    }

    return 0;
}
