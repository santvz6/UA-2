#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define NUM_USERS 10000
#define NUM_LANGUAGES 4  // 0: English, 1: Spanish, 2: French, 3: German

int main() {
    int i;
    // Arreglos para almacenar datos de cada usuario
    int *languageDetected = new int[NUM_USERS];
    double *lat = new double[NUM_USERS];
    double *lon = new double[NUM_USERS];
    int *adaptSuggestion = new int[NUM_USERS];


    // Variables para acumular globalmente el número de usuarios por idioma
    int countEng = 0, countSpa = 0, countFre = 0, countGer = 0;

    // Semilla para generar números aleatorios (simulación)
    srand(42);

    // Procesamiento paralelo de usuarios:
    // • schedule(dynamic): para balancear la carga cuando el procesamiento de cada usuario varíe.
    // • reduction: acumula de forma segura los conteos por idioma.
    #pragma omp parallel for schedule(dynamic) reduction(+:countEng,countSpa,countFre,countGer)
    for (i = 0; i < NUM_USERS; i++) {
        // Simulación de reconocimiento de voz: se asigna un idioma aleatorio (0 a 3)
        int lang = rand() % NUM_LANGUAGES;
        languageDetected[i] = lang;
        if (lang == 0) countEng++;
        else if (lang == 1) countSpa++;
        else if (lang == 2) countFre++;
        else if (lang == 3) countGer++;

        // Simulación de geolocalización: se asignan coordenadas aleatorias (0 a 100)
        lat[i] = (double)(rand() % 101);
        lon[i] = (double)(rand() % 101);

        // Determinar el idioma predominante de la región:
        // Por simplicidad, si la latitud es menor a 50 se asume que es español (1), sino inglés (0).
        int regionLang = (lat[i] < 50.0) ? 1 : 0;

        // Lógica de adaptación:
        // Si el idioma detectado difiere del predominante en la región, se recomienda adaptar el idioma.
        // Se utiliza critical para proteger la asignación, simulando una operación compleja.
        if (languageDetected[i] != regionLang) {
            #pragma omp critical
            {
                adaptSuggestion[i] = 1;
            }
        } else {
            adaptSuggestion[i] = 0;
        }
    }

    // Barrera para asegurar que todos los hilos hayan completado el procesamiento
    #pragma omp barrier

    // Generación del “mapa global”: impresión de estadísticas
    printf("Estadísticas globales de idiomas:\n");
    printf("English: %d\n", countEng);
    printf("Spanish: %d\n", countSpa);
    printf("French: %d\n", countFre);
    printf("German: %d\n", countGer);

    // Cálculo del total de recomendaciones de adaptación
    int totalAdapt = 0;
    for (i = 0; i < NUM_USERS; i++) {
        totalAdapt += adaptSuggestion[i];
    }
    printf("Total de sugerencias de adaptación: %d de %d usuarios.\n", totalAdapt, NUM_USERS);

    // Liberar la memoria asignada
    delete[] languageDetected;
    delete[] lat;
    delete[] lon;
    delete[] adaptSuggestion;

    return 0;
}
