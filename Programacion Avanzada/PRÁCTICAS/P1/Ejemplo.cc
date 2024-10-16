#include "Fecha.h"
#include<iostream>
using namespace std;

void testStr(const string& output, const string& expected){
    if( output == expected ){
        cout << "OK" << endl;
    }else{
        cout << "ERROR: se esperaba:'"<<expected<<"' pero la salida ha sido:'"<<output<<"'"<< endl;
    }
}

void testBool(bool output, bool expected){
    if( output == expected ){
        cout << "OK" << endl;
    }else{
        cout << "ERROR: se esperaba:'"<<expected<<"' pero la salida ha sido:'"<<output<<"'"<< endl;
    }
}

int main()
{ 

   /* Métodos básicos */
   cout << "Probando métodos básicos" << endl;
   Fecha f;
   testStr(f.aCadena(false,false),"1/1/1900");

   Fecha f2(22,1,1000);
   testStr(f2.aCadena(false,false),"1/1/1900");
   
   Fecha f3(29,2,2100);
   testStr(f3.aCadena(false,false),"1/1/1900");
   
   Fecha f4(29,2,2000);
   testStr(f4.aCadena(false,false),"29/2/2000");
   
   
   Fecha f5(f4);
   testStr(f5.aCadena(false,false),"29/2/2000");
   
   
   Fecha f6;
   f6=f5;
   testStr(f6.aCadena(false,false),"29/2/2000");
   
   // Ambos tienen los mismos valores de parámetros pero sus salidas son contrarias
   testBool( f6==f5, true );
   testBool( f6!=f5, false );


   testBool( f6==f2, false );
   testBool( f6!=f2, true );
   
   testBool( f6.setDia(30) ,false);
   testBool( f6.setDia(0) ,false);
   testBool( f6.setDia(25) ,true);
   
   testStr(f6.aCadena(false,false),"25/2/2000");
   
   testBool( f6.setMes(0) ,false);
   testBool( f6.setMes(13) ,false);
   testBool( f6.setMes(3) ,true);
   
   testStr(f6.aCadena(false,false),"25/3/2000");
 
   testBool(f6.setMes(2),true);
   testBool(f6.setDia(29),true);
   
   testBool( f6.setAnyo(0) ,false);
   testBool( f6.setAnyo(1500) ,false);
   testBool( f6.setAnyo(-2000) ,false);
   testBool( f6.setAnyo(2001) ,false);
   testBool( f6.setAnyo(2004) ,true);
   
   testStr(f6.aCadena(false,false),"29/2/2004");
   
  
   /*
   incrementaDias
   */
   cout << "Probando incrementaDias" << endl;
   const int NUM_INCREMENTOS=31;
   int incrementos[] = {
    3, 13, 14, 20, 30, 31, 60, 61, 105, 106,
    164, 165, 365, 1536, -3, -16, -17, -30,
    -31, -60, -61, -91, -92, -200, -201, -202,
    -365, -9287,-45549,-45550,-45551};
   Fecha fechas[] = {
    Fecha(20, 9, 2024),
    Fecha(30, 9, 2024),
    Fecha(1, 10, 2024),
    Fecha(7, 10, 2024),
    Fecha(17, 10, 2024),
    Fecha(18, 10, 2024),
    Fecha(16, 11, 2024),
    Fecha(17, 11, 2024),
    Fecha(31, 12, 2024),
    Fecha(1, 1, 2025),
    Fecha(28, 2, 2025),
    Fecha(1, 3, 2025),
    Fecha(17, 9, 2025),
    Fecha(1, 12, 2028),
    Fecha(14, 9, 2024),
    Fecha(1, 9, 2024),
    Fecha(31, 8, 2024),
    Fecha(18, 8, 2024),
    Fecha(17, 8, 2024),
    Fecha(19, 7, 2024),
    Fecha(18, 7, 2024),
    Fecha(18, 6, 2024),
    Fecha(17, 6, 2024),
    Fecha(1, 3, 2024),
    Fecha(29, 2, 2024),
    Fecha(28, 2, 2024),
    Fecha(18, 9, 2023),
    Fecha(15, 4, 1999),
    Fecha(2, 1, 1900),
    Fecha(1, 1, 1900),  
    Fecha(17, 9, 2024)
  };
  
  Fecha f7;
  
  for(int i=0; i < NUM_INCREMENTOS; i++){
      f7.setDia(17);
      f7.setMes(9);
      f7.setAnyo(2024);
      f7.incrementaDias(incrementos[i]);
      testStr( f7.aCadena(false,false) ,fechas[i].aCadena(false,false) );
  }
  
  
  /* incrementaMeses */
  cout << "Probando incrementaMeses" << endl;
  f7.incrementaMeses(0);
  testStr( f7.aCadena(false,false) , "17/9/2024" );
  f7.incrementaMeses(1);
  testStr( f7.aCadena(false,false) , "17/10/2024" );
  f7.incrementaMeses(-1);
  testStr( f7.aCadena(false,false) , "17/9/2024" );
  f7.incrementaMeses(-7);
  testStr( f7.aCadena(false,false) , "17/2/2024" ); 
  testBool(f7.incrementaMeses(-1),true);
  testBool(f7.setDia(30), true);
  testBool(f7.incrementaMeses(1),false);
  testStr( f7.aCadena(false,false) , "30/1/2024" ); 
  
  
  /* incrementaAnyos */
  cout << "Probando incrementaAnyos" << endl;
  Fecha f8(29,2,2004);
  testBool(f8.incrementaAnyos(1),false);
  testStr(f8.aCadena(false,false),"29/2/2004");
  testBool(f8.incrementaAnyos(-2004),false);
  testStr(f8.aCadena(false,false),"29/2/2004");
  testBool(f8.setDia(28),true);
  testBool(f8.incrementaAnyos(10),true);
  testStr(f8.aCadena(false,false),"28/2/2014");
  testBool(f8.incrementaAnyos(-20),true);
  testStr(f8.aCadena(false,false),"28/2/1994");
  
  /* aCadena */
  cout << "Probando aCadena" << endl;
  testStr(f8.aCadena(true,false),"28 de febrero de 1994");
  testStr(f8.aCadena(true,true),"lunes 28 de febrero de 1994");
  testStr(f8.aCadena(false,true),"lunes 28/2/1994");
  Fecha f9;
  testStr(f9.aCadena(false,true),"lunes 1/1/1900");
  f9.incrementaDias(1);
  testStr(f9.aCadena(false,true),"martes 2/1/1900");
  f9.incrementaDias(3);
  testStr(f9.aCadena(false,true),"viernes 5/1/1900");
  f9.setAnyo(2000);
  testStr(f9.aCadena(false,true),"miércoles 5/1/2000");
  f9.setMes(11);
  testStr(f9.aCadena(false,true),"domingo 5/11/2000");
    
}
