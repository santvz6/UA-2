#include <iostream>
#include <cstring>
using namespace std;

int main(){

    char letras[]={'T', 'R', 'W'}; // hay más letras...
    
    // Podríamos poner directamente int 
    // Pero queremos usar strings para practicar
    string s;
    
    cout << "Introduce un número de DNI con letra: " << endl;
    cin >> s;
    
    // 1er Mét: Para extraer la parte del número
    string numero_str;
    for(int i=0; i<8; i++){
        numero_str += s[i];
    }
    
    // 2º Mét.
    string numero_str2 = s.substr(0,8);
    
    //Pasarlo a INT
    int numero = stoi(numero_str);
    
    int resto=numero%23;
    
    if (letras[resto]== s[8])
        cout<< "DNI correcto"<<endl;
    else
        cout<<"DNI incorrecto"<<endl;
    
    
    
    
    return 0;
}