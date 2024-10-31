#include "Calendario.h"
#include <iostream>


// Constructor por defecto
Calendario::Calendario() : head(nullptr) {}

// Constructor de copia
Calendario::Calendario(const Calendario& obj) : head(nullptr) {
    NodoCalendario* actual = obj.head;
    
    // Quedan nodos todavía (Si apunta a nullptr no se ejecuta)
    while (actual) {
        insertarEvento(actual->evento.fecha, actual->evento.descripcion);
        actual = actual->siguiente;
    }
}

// Operador de asignación
Calendario& Calendario::operator=(const Calendario& otro) {
    if (this == &otro) return *this; // Evitar autoasignación
    while (head) eliminarEvento(head->evento.fecha); // Eliminar nodos actuales

    NodoCalendario* actual = otro.head;
    while (actual) {
        insertarEvento(actual->evento.fecha, actual->evento.descripcion);
        actual = actual->siguiente;
    }
    return *this;
}

// Destructor
Calendario::~Calendario() {
    while (head) {
        NodoCalendario* temp = head;
        head = head->siguiente;
        delete temp;
    }
}

// Insertar un evento en el calendario
bool Calendario::insertarEvento(int fecha, const std::string& descripcion) {
    Evento nuevoEvento(fecha, descripcion);
    if (comprobarEvento(fecha)) return false; // No permite duplicados

    NodoCalendario* nuevoNodo = new NodoCalendario(nuevoEvento);
    if (!head || head->evento.fecha > fecha) {  // Inserta al inicio si es el menor
        nuevoNodo->siguiente = head;
        head = nuevoNodo;
        return true;
    }

    // Insertar en la posición adecuada
    NodoCalendario* actual = head;
    while (actual->siguiente && actual->siguiente->evento.fecha < fecha) {
        actual = actual->siguiente;
    }
    nuevoNodo->siguiente = actual->siguiente;
    actual->siguiente = nuevoNodo;
    return true;
}

// Eliminar un evento del calendario
bool Calendario::eliminarEvento(int fecha) {
    if (!head) return false;
    if (head->evento.fecha == fecha) {  // Eliminar el primer nodo
        NodoCalendario* temp = head;
        head = head->siguiente;
        delete temp;
        return true;
    }

    NodoCalendario* actual = head;
    while (actual->siguiente && actual->siguiente->evento.fecha != fecha) {
        actual = actual->siguiente;
    }

    if (actual->siguiente) {  // Nodo encontrado
        NodoCalendario* temp = actual->siguiente;
        actual->siguiente = actual->siguiente->siguiente;
        delete temp;
        return true;
    }

    return false;  // No encontrado
}

// Comprobar si existe un evento en una fecha
bool Calendario::comprobarEvento(int fecha) const {
    NodoCalendario* actual = head;
    while (actual) {
        if (actual->evento.fecha == fecha) return true;
        actual = actual->siguiente;
    }
    return false;
}

// Método auxiliar para imprimir el calendario (para verificar datos)
void Calendario::imprimirCalendario() const {
    NodoCalendario* actual = head;
    while (actual) {
        std::cout << "Fecha: " << actual->evento.fecha 
                  << ", Descripción: " << actual->evento.descripcion << "\n";
        actual = actual->siguiente;
    }
}
