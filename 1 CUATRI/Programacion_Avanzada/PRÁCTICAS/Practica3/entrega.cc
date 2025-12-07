#include <iostream>
#include <string>
using namespace std;

class Fecha{
    private:
        int dia, mes, año;

        bool esValida(int, int, int );
        bool esBisiesto(int ) const;
        int getMesCant(int, int );
        bool resetAtributos(int, int, int);
        int getDiaSemana() const;

    public:
        //Constructor por defecto: inicializa la fecha a 1/1/1900
        Fecha();
        //Constructor sobrecargado: inicializa la fecha según los parámetros
        Fecha(int dia,int mes,int anyo);
        //Constructor de copia
        Fecha(const Fecha &);
        //Destructor: pone la fecha a 1/1/1900
        ~Fecha();
        //Operador de asignación
        Fecha& operator=(const Fecha &);
        //Operador de comparación
        bool operator==(const Fecha &) const;
        // Operador de comparación
        bool operator!=(const Fecha &) const;
        //Operador de comparación
        bool operator<(const Fecha &) const;
        //Operador de comparación
        bool operator>(const Fecha &) const;


        //Devuelve el día
        int getDia() const;
        //Devuelve el mes
        int getMes() const;
        //Devuelve el año
        int getAnyo() const;
        //Modifica el día: devuelve false si la fecha resultante es incorrecta
        bool setDia(int);
        //Modifica el mes: devuelve false si la fecha resultante es incorrecta
        bool setMes(int);
        //Modifica el anyo: devuelve false si la fecha resultante es incorrecta
        bool setAnyo(int);
        //Incrementa la fecha en el número de días pasado como parámetro.
        //Si el parámetro es negativo, la decrementa
        bool incrementaDias(int );
        //Incrementa la fecha en el número de meses pasado como parámetro.
        //Si el parámetro es negativo, la decrementa
        bool incrementaMeses(int );
        //Incrementa la fecha en el número de años pasado como parámetro.
        //Si el parámetro es negativo, la decrementa
        bool incrementaAnyos(int );
        //Devuelve una representación como cadena de la fecha
        string aCadena(bool larga, bool conDia) const;
};

#include <vector>

class Evento{
    private:
        Fecha f; // Antes de ejecutar constructores instanciamos nuestro objeto de tipo fecha
        string titulo;
        string descripcion;
        int categoria;

    public:
        //Constructor por defecto: inicializa la fecha a 1/1/1900 ...
        //y la descripción a "sin descripción"
        Evento();
        //Constructor sobrecargado: inicializa la fecha según los parámetros
        Evento(const Fecha &, const string &, const string &, const int &);
        //Constructor de copia
        Evento(const Evento&);
        //Operador de asignación
        Evento& operator=(const Evento &);
        //Destructor: pone la fecha a 1/1/1900 y la descripción a "sin descripción"
        ~Evento();

        bool operator==(const Evento &) const;
        //Operador de comparación
        bool operator!=(const Evento &) const;
        //Operador de comparación
        bool operator<(const Evento &) const;
        //Operador de comparación
        bool operator>(const Evento &) const;

        //Devuelve (una copia de) la fecha
        Fecha getFecha() const;
        //Devuelve (una copia de) el título
        string getTitulo() const;
        //Devuelve (una copia de) la descripción
        string getDescripcion() const;
        //Devuelve la categoría
        int getCategoria() const;

        //Modifica la fecha
        void setFecha(const Fecha &);
        //Modifica el titulo
        void setTitulo(const string &);
        //Modifica la categoría
        void setCategoria(int);
        //Modifica la descripción
        void setDescripcion(const string &);

        //Devuelve una cadena con el contenido del evento
        string aCadena(const vector<string>&) const;
};

#ifndef CALENDARIO_H
#define CALENDARIO_H


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


Fecha::Fecha(){
    dia = 1;
    mes = 1;
    año = 1900;
}

Fecha::Fecha(int diai,int mesi,int añoi){
    if (esValida(diai, mesi, añoi)){
        dia = diai;
        mes = mesi;
        año = añoi;
    }
    
    else{
        dia = 1;
        mes = 1;
        año = 1900;
    }
}

Fecha::~Fecha(){
    dia = 1;
    mes = 1;
    año = 1900;
}

Fecha::Fecha(const Fecha &obj) {
    dia = obj.dia;
    mes = obj.mes;
    año = obj.año;
}

Fecha& Fecha::operator=(const Fecha &obj) {

    // this -> dirección de memoria del objeto
    // *this -> objeto real

    // Evitar la autoasignación (comparamos dirección del objeto actual con la del objeto argumento)
    if (this!=&obj){
        dia = obj.dia;
        mes = obj.mes;
        año = obj.año;
    }

    // Devolver la referencia al objeto actual
    return (*this);
}

bool Fecha::operator==(const Fecha &obj) const {
    return (dia == obj.dia && mes == obj.mes && año == obj.año);
}

bool Fecha::operator!=(const Fecha &obj) const {
    return (dia != obj.dia || mes != obj.mes || año != obj.año);
}

bool Fecha::operator<(const Fecha& obj) const {
    if (año < obj.año) return true;
    if (año == obj.año && mes < obj.mes) return true;
    if (año == obj.año && mes == obj.mes && dia < obj.dia) return true;
    return false;
}

bool Fecha::operator>(const Fecha& obj) const {
    if (año > obj.año) return true;
    if (año == obj.año && mes > obj.mes) return true;
    if (año == obj.año && mes == obj.mes && dia > obj.dia) return true;
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

bool Fecha::setDia(int diai){
    if (esValida(diai, mes, año)){
        dia = diai;
        return true;
    }
    return false;
}

bool Fecha::setMes(int mesi){
    if (esValida(dia, mesi, año)){
        mes = mesi;
        return true;
    }
    return false;
}

bool Fecha::setAnyo(int añoi){
    if (esValida(dia, mes, añoi)){
        año = añoi;
        return true;
    }
    return false;
}

bool Fecha::incrementaAnyos(int inc){
    int diai = dia;
    int mesi = mes;
    int añoi = año;
    if (esValida(dia, mes, año+inc)){
        año += inc;
        return true;
    }
    return resetAtributos(diai, mesi, añoi);
}
    
bool Fecha::incrementaMeses(int inc){
    int diai = dia;
    int mesi = mes;
    int añoi = año;

    while (inc != 0){
        // Incremento Positivo
        if (inc>0){
            if (inc > 12-mes){
                mes = 1;
                año++;
                inc -= 12 - mes + 1; // +1: Establecemos el mes a 1
            }
            else{
                mes += inc;
                inc = 0;
            }
        }
        // Incremento Negativo
        else{
            if(-inc >= mes){
                mes = 12;
                año --;
                inc -= mes;
            }
            else{
                mes += inc;
                inc = 0;
            }
        }
    }

    if (esValida(dia, mes, año))
        return true;
    else
        return resetAtributos(diai, mesi, añoi);
}

bool Fecha::incrementaDias(int inc){
    int diai = dia;
    int mesi = mes;
    int añoi = año;

    while (inc!=0){
        // INCREMENTO POSITIVO
        if (inc > 0){
            // AÑOS
            if (esBisiesto(año) && inc >= 366){
                año ++;
                inc -= 366;
            }       
            else if (!esBisiesto(año) && inc >= 365){
                año ++;
                inc -= 365;
            }  
            else{
                // MESES
                int mesact = getMesCant(mes, año);
                if (inc > mesact - dia){
                    if (mes != 12){
                        inc -= mesact - dia + 1;
                        mes ++;
                        dia = 1;   
                    }
                    else{
                        inc -= 31 - dia + 1;
                        mes = dia = 1;
                        año++;
                    }
                }
                else{
                    // DÍAS  
                    dia += inc;
                    inc = 0;
                    }
            }  
        }
        // INCREMENTO NEGATIVO
        else{
            // AÑOS
            if (esBisiesto(año) && -inc >= 366 && (mes > 2 || (mes == 2 && dia == 29))){    
                año --;
                inc += 366;
            }       
            else if ((!esBisiesto(año) && -inc >= 365) || (esBisiesto(año) && mes <= 2 && !(mes == 2 && dia ==29))){
                año --;
                inc += 365;
            }  
            else{
                // MESES
                if (-inc >= dia){
                    if (mes != 1){
                        inc += dia; // Quitamos al mes lo que queda
                        mes--;
                        dia = getMesCant(mes, año);     
                    }
                    else{
                        inc += dia;
                        mes = 12;
                        año--;
                        dia = getMesCant(mes, año);
                    }
                } 
                else{
                    dia += inc;
                    inc = 0;
                }
            }  
        }
    }

    if (esValida(dia, mes, año)){
        return true;
    }
    else{
        resetAtributos(diai, mesi, añoi);
        return false;
    }
    
}

bool Fecha::esValida(int diai ,int mesi, int añoi){
    int tipo_mes = getMesCant(mesi, añoi);
    if (0 < diai && diai <= tipo_mes && 0 < mesi && mesi <= 12 && añoi >= 1900)
        return true;
    return false;
}

bool Fecha::esBisiesto(int año) const{
    if (año % 4 == 0) {
        if (año % 100 == 0) {
            // 4, 100 y 400 > Sí Bisiesto
            if (año % 400 == 0) {
                return true;
            } 
            // 4 y 100 > No Bisiesto
            else {
                return false;
            }
        
        } 
        // sólo 4 > Sí Bisiesto
        else {
            return true;
        }
    }
    // No es divisible entre 4 > No Bisiesto
    else {
        return false;
    }
}

int Fecha::getMesCant(int mes, int año){
    int meses31[] = {1, 3, 5, 7, 8, 10, 12};
    int len_meses31 = sizeof(meses31) / sizeof(meses31[0]);
    if (mes==2 && esBisiesto(año))
        return 29;
    else if (mes==2 && !esBisiesto(año))
        return 28;
    for(int i=0; i < len_meses31; i++){
        if (mes==meses31[i])
            return 31;
    }
    return 30;
}

bool Fecha::resetAtributos(int diai, int mesi, int añoi) {
    // No usamos set, porque esas fechas ya eran válidas en su momento
    // Si cambiamos día, mes y año uno a uno, puede ocasionarse un error de fecha
    dia = diai;
    mes = mesi;
    año = añoi;
    return false;
}

int Fecha::getDiaSemana() const {
    // Días de cada mes en un año no bisiesto
    int diasMes[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int totalDias = 0;

    // Sumar días completos desde 1/1/1900 hasta el 1/1 del año actual
    for (int y = 1900; y < año; y++) {
        if (esBisiesto(y)) {
            totalDias += 366;
        } else {
            totalDias += 365;
        }
    }

    // Sumar días completos de los meses del año actual hasta el mes anterior
    for (int m = 1; m < mes; m++) {
        if (m == 2 && esBisiesto(año)) {
            totalDias += 29; // Febrero en año bisiesto
        } else {
            totalDias += diasMes[m - 1];
        }
    }

    // Sumar los días del mes actual
    totalDias += dia - 1;

    // Calcular el día de la semana
    return totalDias % 7;
}



string Fecha::aCadena(bool larga, bool conDia) const{
    string cadena;
    string dias_semana[] = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"};
    string meses[] = {"enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                    "agosto", "septiembre", "octubre", "noviembre", "diciembre"};

    if (larga) {
        cadena = to_string(dia) + " de " + meses[mes-1] + " de " + to_string(año);
        if (conDia) {
            cadena = dias_semana[getDiaSemana()] + " " + cadena;
        }
    } 
    else {
        cadena = to_string(dia) + "/" + to_string(mes) + "/" + to_string(año);
        if (conDia){
            cadena = dias_semana[getDiaSemana()] + " " + cadena;
        } 
    }
    return cadena;
}


// Constructor por defecto
Evento::Evento() {
    f = Fecha(1, 1, 1900);
    titulo = "sin título";
    descripcion = "";
    categoria = -1;
}

// Constructor sobrecargado: inicializa la fecha según los parám    etros
Evento::Evento(const Fecha& obj, const string&nuevoTitulo ,const string& nuevaDescripicon, const int& nuevaCategoria) {
    f = obj;
    setTitulo(nuevoTitulo);
    setDescripcion(nuevaDescripicon);
    setCategoria(nuevaCategoria);
}

// Constructor de copia 
Evento::Evento(const Evento& obj) {
    f = obj.getFecha();
    setTitulo(obj.getTitulo());
    setDescripcion(obj.getDescripcion());
    setCategoria(obj.getCategoria());
}

// Destructor
Evento::~Evento() {
    titulo = "sin título";
    descripcion = "";
    categoria = -1;
}


///////////////////////////////// OPERADORES
Evento& Evento::operator=(const Evento& obj) {
    if (this != &obj) {  // Evitamos la autoasignación
        f = obj.getFecha();
        setTitulo(obj.getTitulo());
        setDescripcion(obj.getDescripcion());
        setCategoria(obj.getCategoria());
    }
    // Devolvemos el objeto
    return (*this);
}
bool Evento::operator==(const Evento &obj) const{
    return (f == obj.getFecha() && titulo == obj.getTitulo() && descripcion == obj.getDescripcion() && categoria == obj.getCategoria());
}

bool Evento::operator!=(const Evento &obj) const{
    return !(*this == obj); // reutilizamos la lógica de operator ==
}
bool Evento::operator<(const Evento &obj) const{
    return (f < obj.f);
}
bool Evento::operator>(const Evento &obj) const{
    return (f > obj.f);
}


///////////////////////////////// GET

// Devuelve (una copia de) -> Lo pasamos por valor para no modificar el valor original
Fecha Evento::getFecha() const {
    return f;
}
string Evento:: getTitulo() const {
    return titulo;
}
string Evento::getDescripcion() const {
    return descripcion;
}
int Evento::getCategoria() const {
    return categoria;
}

///////////////////////////////// SET

void Evento::setFecha(const Fecha& obj) {
    f = obj;
}
void Evento::setTitulo(const string& nuevoTitulo) {
    if (!nuevoTitulo.empty()) {
        titulo = nuevoTitulo;
    }
    else {titulo = "sin título";
    }
}
void Evento::setDescripcion(const string& nuevaDesc) {
    descripcion = nuevaDesc;
}
void Evento::setCategoria(int nuevaCategoria) {
    if (nuevaCategoria < -1) {
        categoria = -1;
    }
    categoria = nuevaCategoria;
}

string Evento::aCadena(const vector<string>& vector) const{
    string cadena = getFecha().aCadena(true, true) + ":" + getTitulo() + "[" + vector[categoria] + "]:" + getDescripcion();
    return cadena;
}


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
