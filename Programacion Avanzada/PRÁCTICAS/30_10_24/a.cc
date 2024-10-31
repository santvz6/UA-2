#include <iostream>
#include <vector>
using namespace std;

int main(){
    // Vector de tamaño 10 con treses
    vector<int> v(10, 3);
    for (int i=0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;


    // Declaramos un puntero
    // Lo normal es poner que apunte a nullptr
    int* p_int;

    // Si luego queremos acceder a la dirección del puntero
    // Nos saldrá un número aleatorio ya que no está apuntando a nullptr
    cout << *p_int << endl;
    delete p_int;

    // Si usamos lo siguiente (hemos reservado un hueco en la memoria (en concreto hemos reservado un entero = 4bytes))
    // Pero seguimos sin darle el valor al que apunta
    int* p_int = new int;

    delete p_int;
    p_int = nullptr;

}
