#include <stdio.h>
#include <omp.h>

#define PASOS 100

int main() {
    int plato = 0;

    printf("Cocineros colaborando para preparar un plato en %d pasos...\n", PASOS);

    #pragma omp parallel
    {
        int id = omp_get_thread_num();

        #pragma omp for
        for (int i = 0; i < PASOS; i++) {
            if (i == 50) {  // Momento crítico del Gran Chef
                #pragma omp critical
                {
                    printf("Gran Chef %d preparando una sección especial...\n", id);
                    for (int j = 1; j <= 5; j++) {
                        plato += 1;
                        printf("Gran Chef %d añadió el ingrediente especial %d. Total: %d\n", id, j, plato);
                    }
                }
            } else {  // Trabajo normal de los cocineros
                int preparado = 0;
                for (int k = 0; k < 3; k++) {
                    preparado += 1;
                }

                #pragma omp atomic
                plato += preparado;

                printf("Cocinero %d añadió el ingrediente preparado (%d pasos). Total: %d\n", id, preparado, plato);
            }

        }
        // Barrera para asegurarnos de que todos esperan antes de continuar
        #pragma omp barrier
    }

    printf("Plato terminado con %d ingredientes.\n", plato);
    return 0;
}
