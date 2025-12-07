#include "Coordenada.h"
#include <iostream>
using namespace std;


int main(){
    Coordenada c;
    c.imprimir();
    c.setX(8);
    int a = c.getY();
    cout<<a<<endl;
    c.setY(33);
    c.imprimir();

    // No entiendo por qué no va: Coordenada(c) c1;

    return 0;
}