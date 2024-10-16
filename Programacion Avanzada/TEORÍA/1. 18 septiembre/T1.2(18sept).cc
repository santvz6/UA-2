#include <iostream>
#include <cstring>
using namespace std;

int main(){
    
//- ARRAY -
    
    // Array - Tamaño Fijo (6)
    int numeros[] = {1,3,5,7,9,11};
    // Asignación
    numeros[0] = 0;
    // numeros[1] = 5 - 1
    numeros[1] = numeros [2] - 1;
    /* 6 no es índice del array, aún así
     se asigna el valor (en otro lugar) */
    numeros[6] = 1;
    
// STRINGS

    // Cadenas de texto en arrays
    char cadena[]="hola";
    cout<<"Segundo elemento de la cadena: "<<cadena[1]<<endl;
    
    // Para nedir la longitud de la cadena
    cout<<"La longitud de la cadena es "<<strlen(cadena)<<endl;
    
    // cin>> con strings solo lee hasta el primer espacio que haya
    
    // Para medir la longitud del string
    string s="Bienvenido";
    cout<<"La longitud del string es: "<<s.length()<<endl;
    // Buscar dentro de un rango
    cout<<"Del (2 al 5): "<<s.substr(2,5)<<endl;
    
    // Pasar de str a int - viceversa
    int num=100
    int conversion1=stoi(s)
    int conversion2=to_string(num)
    
    
// - FUNCIONES -
    
    //pasar por referencia es más veloz
    // void (const &variable) → va rápido porque no hace copia
    // pero si se modifica la variable dentro de la funcion sale un
    // error (por eso usamos const)
    

// - PUNTEROS -
    // Variables Puntero

    int *punteroEntero; // Dirección de memoria donde obligatoriamente habrá un entero
    
    // Ejemplo
    int i=3;
    int *pi; // se reserva/crea la dirección para un próximo número entero
    pi =&i; // Obtiene y guarda la dirección de i
    *pi=11; // i = 11 (al usar *pi, se llama a la variable de la dirección pi)
    
    
    return 0;
}