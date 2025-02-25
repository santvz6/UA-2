#include <stdio.h>
#include <omp.h>

#define N 1000  

int main() {
    int i;
    double suma = 0.0;
    double A[N];

  
    for (i = 0; i < N; i++)
        A[i] = i * 1.0;

  
    #pragma omp parallel for reduction(+:suma)
    for (i = 0; i < N; i++) {
        suma += A[i];  
    }

    
    printf("Suma total: %f\n", suma);

    return 0;
}
