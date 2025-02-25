#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <omp.h>

using namespace std;

const int MAP_SIZE = 200;
const int MIN_FAROLAS = 50, MAX_FAROLAS = 500;
const int BAJO_MIN = 70, BAJO_MAX = 100;
const int MEDIO_MIN = 150, MEDIO_MAX = 200;
const int ALTO_MIN = 250, ALTO_MAX = 300;

struct Celda {
    int num_farolas;
    int consumo_total;
};


// PASO 1: INICIALIZACIÓN DEL MAPA
void inicializarMapa(vector<vector<Celda>> &mapa) {
    srand(time(0));

    for (int i = 0; i < MAP_SIZE; i++) {
        for (int j = 0; j < MAP_SIZE; j++) {
            mapa[i][j].num_farolas = rand() % (MAX_FAROLAS - MIN_FAROLAS + 1) + MIN_FAROLAS;
            mapa[i][j].consumo_total = 0;

            for (int k = 0; k < mapa[i][j].num_farolas; k++) {
                int tipo = rand() % 3;
                if (tipo == 0)
                    mapa[i][j].consumo_total += rand() % (BAJO_MAX - BAJO_MIN + 1) + BAJO_MIN;
                else if (tipo == 1)
                    mapa[i][j].consumo_total += rand() % (MEDIO_MAX - MEDIO_MIN + 1) + MEDIO_MIN;
                else
                    mapa[i][j].consumo_total += rand() % (ALTO_MAX - ALTO_MIN + 1) + ALTO_MIN;
            }
        }
    }
}

// PASO 2: CÁLCULO SECUENCIAL
void calcularConsumoSecuencial(const vector<vector<Celda>> &mapa, long long &total_farolas, long long &consumo_total) {
    total_farolas = 0;
    consumo_total = 0;

    for (int i = 0; i < MAP_SIZE; i++) {
        for (int j = 0; j < MAP_SIZE; j++) {
            total_farolas += mapa[i][j].num_farolas;
            consumo_total += mapa[i][j].consumo_total;
        }
    }
}

// PASO 3: CÁLCULO PARALELO CON OpenMP
void calcularConsumoParalelo(const vector<vector<Celda>> &mapa, long long &total_farolas, long long &consumo_total, string tipo_schedule) {
    total_farolas = 0;
    consumo_total = 0;

    if (tipo_schedule == "static") {
        #pragma omp parallel for reduction(+:total_farolas, consumo_total) schedule(static)
        for (int i = 0; i < MAP_SIZE; i++) {
            for (int j = 0; j < MAP_SIZE; j++) {
                total_farolas += mapa[i][j].num_farolas;
                consumo_total += mapa[i][j].consumo_total;
            }
        }
    } 
    else if (tipo_schedule == "dynamic") {
        #pragma omp parallel for reduction(+:total_farolas, consumo_total) schedule(dynamic)
        for (int i = 0; i < MAP_SIZE; i++) {
            for (int j = 0; j < MAP_SIZE; j++) {
                total_farolas += mapa[i][j].num_farolas;
                consumo_total += mapa[i][j].consumo_total;
            }
        }
    } 
    else if (tipo_schedule == "guided") {
        #pragma omp parallel for reduction(+:total_farolas, consumo_total) schedule(guided)
        for (int i = 0; i < MAP_SIZE; i++) {
            for (int j = 0; j < MAP_SIZE; j++) {
                total_farolas += mapa[i][j].num_farolas;
                consumo_total += mapa[i][j].consumo_total;
            }
        }
    }
}

// PASO 4: ANÁLISIS DEL RENDIMIENTO

double calcularConsumo(bool secuencial, const vector<vector<Celda>> &mapa, long long &total_farolas, long long &consumo_total, string tipo_schedule) {
    double start_sec;

    if (secuencial || tipo_schedule.empty()) {
        start_sec = omp_get_wtime();
        calcularConsumoSecuencial(mapa, total_farolas, consumo_total);
    } else {
        start_sec = omp_get_wtime();
        calcularConsumoParalelo(mapa, total_farolas, consumo_total, tipo_schedule);
    }
    double end_sec = omp_get_wtime();
    return end_sec - start_sec;
}   


int main() {
    vector<vector<Celda>> mapa(MAP_SIZE, vector<Celda>(MAP_SIZE));

    // Inicializamos el mapa
    inicializarMapa(mapa);

    long long total_farolas_sec, consumo_total_sec;
    long long total_farolas_par, consumo_total_par;


    // Secuencial
    double tiempo_sec = calcularConsumo(true, mapa, total_farolas_sec, consumo_total_sec, "");
    // Paralelo: Static
    double tiempo_static = calcularConsumo(false, mapa, total_farolas_sec, consumo_total_sec, "static");
    // Paralelo: Dynamic
    double tiempo_dynamic = calcularConsumo(false, mapa, total_farolas_sec, consumo_total_sec, "dynamic");
    // Paralelo: Guided
    double tiempo_guided = calcularConsumo(false, mapa, total_farolas_sec, consumo_total_sec, "guided");

    // Resultados
    cout << "Resultados Secuenciales:" << endl;
    cout << "Total de farolas: " << total_farolas_sec << endl;
    cout << "Consumo total: " << consumo_total_sec << " vatios" << endl;
    cout << "Tiempo de ejecución: " << tiempo_sec << " segundos" << endl;

    cout << "\nResultados Paralelos (Static):" << endl;
    cout << "Tiempo de ejecución: " << tiempo_static << " segundos" << endl;

    cout << "\nResultados Paralelos (Dynamic):" << endl;
    cout << "Tiempo de ejecución: " << tiempo_dynamic << " segundos" << endl;

    cout << "\nResultados Paralelos (Guided):" << endl;
    cout << "Tiempo de ejecución: " << tiempo_guided << " segundos" << endl;

    return 0;
}

