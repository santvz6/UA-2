#include <stdio.h>
#include <omp.h>
#include <math.h>

#define N 1000000

int main() {
    long long suma = 0;
    double start, end;

    omp_sched_t schedules[] = {omp_sched_static, omp_sched_dynamic, omp_sched_guided};
    const char* schedule_names[] = {"static", "dynamic", "guided"};

    for (int s = 0; s < 3; s++) {
        suma = 0;
        omp_set_schedule(schedules[s], 1000);  // Tamaño del chunk

        start = omp_get_wtime();
        #pragma omp parallel for schedule(runtime) reduction(+:suma)
        for (int i = 1; i <= N; i++) {
            suma += i * i;  // Suma de cuadrados
        }
        end = omp_get_wtime();

        printf("Schedule: %s - Suma: %lld, Tiempo: %f segundos\n", schedule_names[s], suma, end - start);
    }

    return 0;
}
