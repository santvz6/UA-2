#include <iostream>
using namespace std;

bool esPrimo(int num){
    for (int i=2; i<num; i++){
        if (num%i==0){
            return false;
        }
    }
    return true;
}


int main(){
    int inicio, fin;
    
    cin>>inicio;
    cin>>fin;
    
    cout<<"inicio: "<<inicio<<endl;
    cout<<"fin: "<<fin<<endl;
    
    // No consideramos  que el 1 no es primo
    for(int i=inicio; i<=fin; i++){
        cout<<"Probando: "<<i<<endl;
        if (esPrimo(i))
            cout<<"Es primo"<<endl;
        else
            cout<<"No es primo"<<endl;
    }
    
    return 0;
}