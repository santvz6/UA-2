#include "Evento.h"

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