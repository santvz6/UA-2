#include "Coordenada.h"
#include <iostream>
using namespace std;

Coordenada::Coordenada(){
    x = 0;
    y = 0;
    z = 0;
}

Coordenada::~Coordenada(){

}

Coordenada::Coordenada(const Coordenada &c){ //const + & (no se hace copia[&] y no se pasa por valor[const] (con objetos grandes es recomendable))
    x = c.getX();
    y = c.getY();
    z = c.getZ();
}

void Coordenada::imprimir(){
    cout<<"("<<getX()<<", "<<getY()<<", "<<getZ()<<")"<<endl;
}

bool Coordenada::setX(int xi){
    x = xi;
    return true;
}
bool Coordenada::setY(int yi){
    y = yi;
    return true;
}
bool Coordenada::setZ(int zi){
    z = zi;
    return true;
}

int Coordenada::getX() const{
    return x;
}
int Coordenada::getY() const{
    return y;
}
int Coordenada::getZ() const{
    return z;
}

