#ifndef CALENDARIO_H
#define CALENDARIO_H

#include "Evento.h"

#include<string>
#include <map>
#include <stack>

using namespace std;

class Calendario{
    private:
        map<Fecha, Evento> eventos;
        stack<Fecha> historialInserciones;
        stack<Evento> historialBorrados;

    public:
        //Constructor por defecto: calendario sin ningún evento
        Calendario();
        //Constructor de copia
        Calendario(const Calendario&);
        //Operador de asignación
        Calendario& operator=(const Calendario &);
        //Destructor
        ~Calendario();
        //Añade un evento al calendario. Si ya existía un evento en esa fecha, 
        //devuelve false y no hace nada. En caso contrario, devuelve true.
        bool insertarEvento(const Evento&);
        //Elimina un evento del calendario. Si no había ningún evento asociado a esa fecha, 
        //devuelve false y no hace nada. En caso contrario, devuelve true.
        bool eliminarEvento(const Fecha&);
        //Comprueba si hay algún evento asociado a la fecha dada
        bool comprobarEvento(const Fecha&) const;
        //Obtiene la descripción asociada al evento. Si no hay ningún evento asociado a la fecha
        //devuelve un objeto de tipo Evento creado con su constructor por defecto
        Evento obtenerEvento(const Fecha&) const;
        //Devuelve una cadena con el contenido completo del calendario
        string aCadena(const vector<string>&) const;
        //Deshace la última inserción exitosa
        void deshacerInsercion();
        //Deshace el último borrado exitoso
        void deshacerBorrado();
        //Devuelve una cadena con el contenido completo del calendario
        string aCadenaPorTitulo(const string&, const vector<string>&) const;
        //categoría, día, mes y año más frecuente
        int categoriaMasFrecuente() const;
        int diaMasFrecuente() const;
        int mesMasFrecuente() const;
        int anyoMasFrecuente() const;
};

#endif
