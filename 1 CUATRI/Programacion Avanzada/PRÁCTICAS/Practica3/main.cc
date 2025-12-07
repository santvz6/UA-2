#include "Calendario.h"
#include <sstream>
#include <algorithm>

int main() {
    vector<string> categorias;
    string linea;

    // Leer las categorías
    while (getline(cin, linea) && linea != "[FIN_CATEGORIAS]") {
        categorias.push_back(linea);
    }

    // Crear el calendario
    Calendario calendario;

    // Leer comandos y ejecutarlos
    while (getline(cin, linea) && linea != "[FIN]") {
        istringstream comando(linea);
        string metodo;
        comando >> metodo;

        if (metodo == "insertarEvento") {
            int dia, mes, anyo, categoria;
            string titulo, descripcion;
            comando >> dia >> mes >> anyo;
            comando >> titulo >> descripcion >> categoria;

            // Reemplazar guiones bajos por espacios
            replace(titulo.begin(), titulo.end(), '_', ' ');
            replace(descripcion.begin(), descripcion.end(), '_', ' ');

            Fecha fecha(dia, mes, anyo);
            Evento evento(fecha, titulo, descripcion, categoria);
            bool exito = calendario.insertarEvento(evento);
            cout << exito << endl;

        } else if (metodo == "eliminarEvento") {
            int dia, mes, anyo;
            comando >> dia >> mes >> anyo;
            Fecha fecha(dia, mes, anyo);
            bool exito = calendario.eliminarEvento(fecha);
            cout << exito << endl;

        } else if (metodo == "comprobarEvento") {
            int dia, mes, anyo;
            comando >> dia >> mes >> anyo;
            Fecha fecha(dia, mes, anyo);
            bool existe = calendario.comprobarEvento(fecha);
            cout << existe << endl;

        } else if (metodo == "obtenerEvento") {
            int dia, mes, anyo;
            comando >> dia >> mes >> anyo;
            Fecha fecha(dia, mes, anyo);
            Evento eventoObtenido = calendario.obtenerEvento(fecha);
            cout << eventoObtenido.aCadena(categorias) << endl;
            
        } else if (metodo == "aCadena") {
            cout << calendario.aCadena(categorias) << endl;

        } else if (metodo == "deshacerInsercion") {
            calendario.deshacerInsercion();

        } else if (metodo == "deshacerBorrado") {
            calendario.deshacerBorrado();

        } else if (metodo == "aCadenaPorTitulo") {
            string titulo;
            comando >> titulo;
            replace(titulo.begin(), titulo.end(), '_', ' ');
            cout << calendario.aCadenaPorTitulo(titulo, categorias) << endl;
        
        } else if (metodo == "categoriaMasFrecuente") {
            int categoria = calendario.categoriaMasFrecuente();
            cout << categoria << endl;
        
        } else if (metodo == "diaMasFrecuente") {
            cout << calendario.diaMasFrecuente() << endl;
        
        } else if (metodo == "mesMasFrecuente") {
            cout << calendario.mesMasFrecuente() << endl;
        
        } else if (metodo == "anyoMasFrecuente") {
            cout << calendario.anyoMasFrecuente() << endl;
        
        } else {
            cerr << "Metodo no reconocido: " << metodo << endl;
        }
    }

    return 0;
}