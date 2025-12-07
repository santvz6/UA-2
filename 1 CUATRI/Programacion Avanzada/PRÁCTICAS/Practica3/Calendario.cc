    #include "Calendario.h"

    /*** Calendario ***/

    //Constructor por defecto: calendario sin ningún evento
    Calendario::Calendario() {}

    //Constructor de copia
    Calendario::Calendario(const Calendario& obj) {
        eventos = obj.eventos; // Copia del mapa de eventos
        historialInserciones = obj.historialInserciones; // Copia del historial de inserciones
        historialBorrados = obj.historialBorrados; // Copia del historial de borrados
    }

    //Operador de asignación
    Calendario& Calendario::operator=(const Calendario &obj) {
        if (this != &obj) {  // Evita la auto-asignación
            eventos = obj.eventos; // Copia del mapa de eventos
            historialInserciones = obj.historialInserciones; // Copia del historial de inserciones
            historialBorrados = obj.historialBorrados; // Copia del historial de borrados
        }
        return *this;
    }

    //Destructor
    Calendario::~Calendario() {}

    //Añade un evento al calendario. Si ya existía un evento en esa fecha, 
    //devuelve false y no hace nada. En caso contrario, devuelve true.
    bool Calendario::insertarEvento(const Evento& e) {
        Fecha nuevaFecha = e.getFecha();  // Obtener la fecha del evento

        // Ya existe un key:value para esa fecha
        if (comprobarEvento(nuevaFecha)) {
            return false; 
        }

        // Insertar el nuevo evento en el mapa
        eventos[nuevaFecha] = e;

        // Guardar en el historial de inserciones
        historialInserciones.push(nuevaFecha);

        return true;
    }

    //Elimina un evento del calendario. Si no había ningún evento asociado a esa fecha, 
    //devuelve false y no hace nada. En caso contrario, devuelve true.
    bool Calendario::eliminarEvento(const Fecha& f) {
        if (!comprobarEvento(f)) {
            return false;  // No existe un evento para esa fecha
        }

        // Eliminar el evento del mapa
        map<Fecha, Evento>::iterator iterador = eventos.find(f);

        // Guardamos el evento en el historial de borrados
        historialBorrados.push(iterador->second);

        eventos.erase(iterador);

        return true;
    }

    //Comprueba si hay algún evento asociado a la fecha dada
    bool Calendario::comprobarEvento(const Fecha& f) const {
        return eventos.find(f) != eventos.end();  // Devuelve true si existe un evento
    }

    //Obtener el evento asociado a la fecha dada
    Evento Calendario::obtenerEvento(const Fecha& f) const {
        if (comprobarEvento(f)) {
            return eventos.find(f)->second;  // Retorna el evento asociado a la fecha
        }
        return Evento();  // Retorna un evento vacío si no se encuentra
    }

    // Devuelve una cadena con el contenido completo del calendario
    string Calendario::aCadena(const vector<string>& categorias) const {
        string resultado;

        // Comprobar si hay eventos
        if (eventos.empty()) {
            return resultado;
        }

        // Iterar a través de los eventos con un bucle for tradicional
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            // Añadir la cadena correspondiente al evento
            if (!resultado.empty()) {  // Si ya hay texto en el resultado, añade un salto de línea
                resultado += "\n";
            }
            resultado += it->second.aCadena(categorias);
        }

        return resultado;
    }



    //Deshacer la última inserción de evento
    void Calendario::deshacerInsercion() {
        if (!historialInserciones.empty()) {
            Fecha fechaDeshacer = historialInserciones.top();
            historialInserciones.pop();
            eventos.erase(fechaDeshacer);
        }
    }

    //Deshacer el último borrado de evento
    void Calendario::deshacerBorrado() {
        if (!historialBorrados.empty()) {
            Evento eventoDeshacer = historialBorrados.top();
            historialBorrados.pop();
            eventos[eventoDeshacer.getFecha()] = eventoDeshacer;
        }
    }

    //Devuelve una cadena con la información de los eventos que tienen
    //como título el primer argumento
    string Calendario::aCadenaPorTitulo(const string& titulo, const vector<string>& categorias) const {
        string resultado;

        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            if (it->second.getTitulo() == titulo) {
                if (!resultado.empty()) {  // Si ya hay texto en el resultado, añade un salto de línea
                    resultado += "\n";
                }
                resultado += it->second.aCadena(categorias);
            }
        }
        return resultado;
    }

    //Devuelve la categoría más frecuente en el calendario
    int Calendario::categoriaMasFrecuente() const {
        map<int, int> frecuenciaCategorias; // {categoria: frecuencia}


        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            frecuenciaCategorias[it->second.getCategoria()]++;   // Evento.getCategoria()
        }

        int categoriaFrecuente = -1;
        int maxFrecuencia = 0;

        
        for (auto it = frecuenciaCategorias.begin(); it != frecuenciaCategorias.end(); ++it) {
            if (it->second >= maxFrecuencia) { // El igual lo puse porque en sus ejemplos si es igual se establece como maximo
                maxFrecuencia = it->second;
                categoriaFrecuente = it->first;
            }
        }

        return categoriaFrecuente;
    }

    //Devuelve el día más frecuente en el calendario
    int Calendario::diaMasFrecuente() const {
        map<int, int> frecuenciaDias;

        
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            int dia = it->first.getDia();  // fecha.getDia()
            frecuenciaDias[dia]++;
        }

        int diaFrecuente = -1;
        int maxFrecuencia = 0;

        
        for (auto it = frecuenciaDias.begin(); it != frecuenciaDias.end(); ++it) {
            if (it->second >= maxFrecuencia) {
                maxFrecuencia = it->second;
                diaFrecuente = it->first;
            }
        }

        return diaFrecuente;
    }

    //Devuelve el mes más frecuente en el calendario
    int Calendario::mesMasFrecuente() const {
        map<int, int> frecuenciaMeses;

        
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            int mes = it->first.getMes();
            frecuenciaMeses[mes]++;
        }

        int mesFrecuente = -1;
        int maxFrecuencia = 0;

        
        for (auto it = frecuenciaMeses.begin(); it != frecuenciaMeses.end(); ++it) {
            if (it->second >= maxFrecuencia) {
                maxFrecuencia = it->second;
                mesFrecuente = it->first;
            }
        }

        return mesFrecuente;
    }

    //Devuelve el año más frecuente en el calendario
    int Calendario::anyoMasFrecuente() const {
        map<int, int> frecuenciaAnos;

        
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            int año = it->first.getAnyo();
            frecuenciaAnos[año]++;
        }

        int añoFrecuente = -1;
        int maxFrecuencia = 0;

        
        for (auto it = frecuenciaAnos.begin(); it != frecuenciaAnos.end(); ++it) {
            if (it->second >= maxFrecuencia) {
                maxFrecuencia = it->second;
                añoFrecuente = it->first;
            }
        }

        return añoFrecuente;
    }

    int Calendario::diaSemanaMasFrecuente() const{
        map<int, int> frecuencia;

        
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            int diaSemana = it->first.getDiaSemana();
            frecuencia[diaSemana]++;
        }

        int masFrecuente = -1;
        int maxFrecuencia = 0;

        
        for (auto it = frecuencia.begin(); it != frecuencia.end(); ++it) {
            if (it->second >= maxFrecuencia) {
                maxFrecuencia = it->second;
                masFrecuente = it->first;
            }
        }
        return masFrecuente;
    }

    Evento Calendario::eventoPorPalabra(const string& palabra) const {
        // {fecha: evento}
        for (auto it = eventos.begin(); it != eventos.end(); ++it) {
            if (it->second.getTitulo() == palabra) return it->second;
        }
        return Evento();
    }
