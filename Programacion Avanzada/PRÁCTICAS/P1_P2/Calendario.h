#include <string>
#include "Evento.h"

// Creamos un Nodo llamado NodoCalendario
// Struct: Es como una class pero con atributos publicos
struct NodoCalendario {
    Evento evento;
    // puntero que apunta a otro nodo de tipo NodoCalendario
    // asignamos el puntero siguiente de cada nodo al nodo que le sigue en la lista
    NodoCalendario* siguiente;

    // Constructor: inicializa un nodo con un Evento y establece el puntero siguiente como nullptr
    NodoCalendario(const Evento& e) : evento(e), siguiente(nullptr) {}
};

// Clase Calendario
class Calendario {
private:
    NodoCalendario* head; // Apunta al primer nodo de la lista enlazada

public:
    // Constructor por defecto
    Calendario();

    // Constructor de copia
    Calendario(const Calendario& otro);

    // Operador de asignación
    Calendario& operator=(const Calendario& otro);

    // Destructor
    ~Calendario();

    // Insertar un evento en el calendario
    bool insertarEvento(int fecha, const std::string& descripcion);

    // Eliminar un evento del calendario
    bool eliminarEvento(int fecha);

    // Comprobar si existe un evento en una fecha
    bool comprobarEvento(int fecha) const;

    // Método auxiliar para imprimir el calendario
    void imprimirCalendario() const;
};