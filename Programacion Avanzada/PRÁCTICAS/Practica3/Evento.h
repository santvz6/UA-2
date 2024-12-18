#include "Fecha.h"
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