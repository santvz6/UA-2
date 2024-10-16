#include "Evento.h"
#include <iostream>
using namespace std;

Evento::Evento(){
    //fecha.Fecha() = ""
    descripcion = "Sin descripcion";
}

Evento::Evento(const Fecha&, string){
    if (string=="") descripcion="Sin descripcion";
}


//Constructor de copia
Evento(const Evento&);
//Operador de asignación
Evento& operator=(const Evento &);
//Destructor: pone la fecha a 1/1/1900 y la descripción a "sin descripción"
~Evento();
//Devuelve (una copia de) la fecha
Fecha getFecha() const;
//Devuelve (una copia de) la descripción
string getDescripcion() const;
//Modifica la fecha
void setFecha(const Fecha& );
//Modifica la descripción
bool setDescripcion(string);