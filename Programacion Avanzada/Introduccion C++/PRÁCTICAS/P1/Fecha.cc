// Fichero para implementar la funcionalidad 
// de los métodos que incluye la clase

#include "Fecha.h" // Importamos el fichero Fecha.h
#include <iostream>
using namespace std;


// La clase Fecha se instancia utilizando la función Fecha() (por tanto Fecha() será el constructor)
Fecha::Fecha(){
    cout<<"Ejecutando Constructor"<<endl;
    dia = 1;
    mes = 1;
    año = 1900;
}

bool Fecha:: esBisiesto(){
    if (año%4==0 && año%100==0)
        return true;
    else if(año%4==0 && año%100==0 && año%400==0)
        return true;
    else
        return false;
}

int Fecha::getDia() const{
    return dia;
}

int Fecha::getMes() const{
    return mes;
}

int Fecha::getAnyo() const{
    return año;
}

bool Fecha::incrementaAnyos(int inc){
    año += inc;
}

bool Fecha::incrementaMeses(int inc){
    while(inc!=0){
        if (mes!=12){
            mes++;
            inc-=1;
        }
        else
            mes=1;
            año++;
            inc-=1
    }
    
}

bool Fecha::incrementaDias(int inc){
    
}

// Destructor de la clase
Fecha::~Fecha(){
    cout<<"Ejecutando Destructor"<<endl;
}