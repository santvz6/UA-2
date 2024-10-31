#include <iostream>
#include "Calendario.h"
#include "Evento.h"

int main() {
    // Crear un objeto Calendario
    Calendario calendario;

    // Insertar algunos eventos
    std::cout << "Insertando eventos..." << std::endl;
    calendario.insertarEvento(20231010, "Conferencia de Ciencia de Datos");
    calendario.insertarEvento(20231015, "Reunión del Proyecto X");
    calendario.insertarEvento(20231101, "Día de todos los santos");
    calendario.insertarEvento(20231020, "Entrega de Tareas");

    // Imprimir calendario después de la inserción
    std::cout << "Eventos en el calendario después de la inserción:" << std::endl;
    calendario.imprimirCalendario();

    // Comprobar si existe un evento en una fecha específica
    int fecha = 20231015;
    std::cout << "\n¿Existe un evento el " << fecha << "? ";
    if (calendario.comprobarEvento(fecha)) {
        std::cout << "Sí, existe un evento en esa fecha." << std::endl;
    } else {
        std::cout << "No, no hay ningún evento en esa fecha." << std::endl;
    }

    // Intentar insertar un evento en una fecha ya ocupada
    std::cout << "\nIntentando insertar un evento duplicado en la fecha " << fecha << "..." << std::endl;
    if (!calendario.insertarEvento(fecha, "Evento duplicado")) {
        std::cout << "No se pudo insertar el evento: ya existe un evento en la fecha " << fecha << "." << std::endl;
    }

    // Eliminar un evento
    std::cout << "\nEliminando el evento en la fecha " << fecha << "..." << std::endl;
    calendario.eliminarEvento(fecha);

    // Imprimir calendario después de la eliminación
    std::cout << "Eventos en el calendario después de la eliminación:" << std::endl;
    calendario.imprimirCalendario();

    return 0;
}
