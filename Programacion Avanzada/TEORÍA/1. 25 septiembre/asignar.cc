/*
Tam     Array   NuevoArray      |                       |
5       2000    2100            |   10  20  44  32  99  |   10  20  44  32  99 ... 33
1000    1004    1008            |(2000)                 |(2100)


*/


#include <iostream>
using namespace std;

// int* array (puntero)
void asignar(int* &array, int &tamaño, int posicion, int numero){
    if (posicion >= tamaño){
        int nuevoTamaño = posicion + 1;
        int* nuevoArray=new int[nuevoTamaño];// Nuevo array con puntero en 0
        for (int i=0; i<tamaño; i++){
            nuevoArray[i]=array[i];     
        }
        delete[] array;
        array = nuevoArray; // Array apuntaría al nuevoArray y perdemos el puntero de array (pero 2000 sigue lleno) USAMOS delete[] para que no ocurra
        tamaño = nuevoTamaño;
        array[posicion]=numero;
    }
}

void imprimir(int* array, int tamaño){
    for (int i=0; i<tamaño; i++){
        cout << array[i] <<endl;
    }
    cout << endl;
}

int main(){
    int tam=5;
    int* array = new int[tam]; // new: para irnos a tierra de nadie (huecos libres en memoria que no se borran automaticamente)
    asignar(array, tam, 0, 10);
    asignar(array, tam, 1, 20);
    asignar(array, tam, 2, 44);
    asignar(array, tam, 3, 32);
    asignar(array, tam, 4, 99);
    asignar(array, tam, 20, 33); //array[20] : Hay que reservar 20 espacios de memoria aunque no se usen los de [5, 19]
    imprimir(array, tam);
    return 0;
}