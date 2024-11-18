#include <iostream>
using namespace std;


// Una estructura es una clase con métodos y atributos públicos
struct Elemento{
    int numero;
    struct Elemento *siguiente; // Puntero llamado siguiente
};

struct Elemento *pi, *pa, *pf; // PunteroInicial, PunteroAuxiliar(ACTUAL) , PunteroFinal


// Algoritmo para insertar el valor
void insertar_lista(int valor) {

    // La lista está vacía
    if (pi == nullptr){
        pi = new (Elemento); // Creamos el nodo
        pi->numero = valor; // Asignamos al atributo numero de este nodo el valor "valor"
        pf = pi; // Al solo tener un nodo (ESTAMOS EN LA CREACIÓN DEL PRIMER NODO) el pi = pf
    
    // La lista no está vacía
    } else {
        pa = new(Elemento);
        pf->siguiente = pa; // EL puntero final ahora está en el siguiente nodo (tenemos más de 1 nodo)
        pa->numero = valor;
        pf = pa; // Una vez realizada la asignación el puntero final toma el valor del auxiliar
    }
    pf->siguiente = nullptr; // mientras no se inserte ningún nodo el puntero final es nullptr
}

void mostrar_elementos() {
    pa = pi; // Empezamos siempre por el primer elemento de la lista
    int i = 1;

    cout << endl << endl << "Elementos de la Lista Enlazada" << endl << endl;
    while (pa != nullptr){

        cout << "Elemento numero " << i << ": " << pa->numero << endl;
        pa = pa->siguiente; // el puntero auxiliar pasa al siguiente nodo
        i ++;
    }
}

int main(){

    for (int i=0; i < 5; i++){
        int valor;
        cout << endl << "Ingrese valor: ";
        cin >> valor;
        insertar_lista(valor);
    }

    mostrar_elementos();

    return 0;
}