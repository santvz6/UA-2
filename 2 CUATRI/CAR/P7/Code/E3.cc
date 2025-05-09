#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main() {

    long long N  = 100000000; // 100 millones
    double start, end;
    
    for (int num_hilos = 4; num_hilos <= 8; num_hilos *= 2) {
        printf("\nEjecutando con %d hilos:\n", num_hilos);
        
        for (int k = 0; k < 3; k++) {
            double resultado_final = 0.0;

            if (k==0) {
                start = omp_get_wtime();
                #pragma omp parallel for num_threads(num_hilos) reduction(+:resultado_final) schedule(static)
                for (long long i = 0; i < 16; i++) {
                    double local_result = 0.0;
                    long long carga = N * (i % 4 + 1);
                    for (long long j = 0; j < carga; j++) {
                        local_result += (j * 0.5) / (j + 1.0);
                    }
                    resultado_final += local_result;
                }
            
                end = omp_get_wtime();
                if (omp_get_thread_num() == 0) {
                    printf("Schedule static -> Resultado final schedule(static %i hilos): %2f\n", num_hilos, resultado_final);
                    printf("Tiempo: %f segundos\n", end - start);
                }
            } else if (k==1) {
            
                start = omp_get_wtime();
                #pragma omp parallel for num_threads(num_hilos) reduction(+:resultado_final) schedule(dynamic, 1)
                for (long long i = 0; i < 16; i++) {
                    double local_result = 0.0;
                    long long carga = N * (i % 4 + 1);
                    for (long long j = 0; j < carga; j++) {
                        local_result += (j * 0.5) / (j + 1.0);
                    }
                    resultado_final += local_result;
                }
            
                end = omp_get_wtime();
                if (omp_get_thread_num() == 0) {
                    printf("Schedule dynamic -> Resultado final (%i hilos): %2f\n", num_hilos, resultado_final);
                    printf("Tiempo: %f segundos\n", end - start);
                }
            } else if (k==2) {
            
                start = omp_get_wtime();
                #pragma omp parallel for num_threads(num_hilos) reduction(+:resultado_final) schedule(guided)
                for (long long i = 0; i < 16; i++) {
                    double local_result = 0.0;
                    long long carga = N * (i % 4 + 1);
                    for (long long j = 0; j < carga; j++) {
                        local_result += (j * 0.5) / (j + 1.0);
                    }
                    resultado_final += local_result;
                }
            
                end = omp_get_wtime();
                if (omp_get_thread_num() == 0) {
                    printf("Schedule guided -> Resultado final (%i hilos): %2f\n", num_hilos, resultado_final);
                    printf("Tiempo: %f segundos\n", end - start);
                }
            }
            
        }
    }

    return 0;
}