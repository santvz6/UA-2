#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#include <signal.h>

/*
El ejercicio nos pide crear un proceso hijo (A) del proceso padre (R),
luego este proceso A tendrá un hijo(B) que a su vez,
este tendrá 3 hijos (X, Y, Z)

Para compilar usaremos > gcc -o nombreCompilacion nombreArchivoC
*/

// IPC (InterProcessComunication): Señales, tuberías, memoria compartida

// Permisos RWX
/// 		110

__pid_t pidA; // declaramos la variable pidA con el tipo de dato: __pid_t
__pid_t pidB;
__pid_t pidX;
__pid_t pidY;
__pid_t pidZ;

char proceso;
unsigned int seconds;

void handler_z(){
	
	printf("Ejecutando handler_z\n");
	
	switch(toupper(proceso)){
		case 'A':
			printf("Señal a A");
			kill(pidA, SIGUSR1);
			break;
		case 'B':
		printf("Señal a B");
			kill(pidB, SIGUSR1);	
			break;
		case 'X':
			printf("Señal a X");
			kill(pidX, SIGUSR2);
			break;
		case 'Y':	
			printf("Señal a Y");
			kill(pidY, SIGUSR2);
			break;
		default:
			printf("No se ha seleccionado un proceso válido\n");

	};
};

void handler_ab(){
	printf("Ejecutando handler_ab\n");
	__pid_t pidExec;
	pidExec = fork();
	switch(pidExec){
		case -1:
			printf ("No he podido crear el proceso hijo A\n");
			break;
		case 0:
			printf("Soy execlp(%d) y muero", getpid());
			execlp("pstree", "pstree", NULL);
	}
};

void handler_xy(){
	printf("Ejecutando handler_xy, (%d)\n", getpid());

	__pid_t pidExec;
	pidExec = fork();
	switch(pidExec){
		case -1:
			printf ("No he podido crear el proceso hijo A\n");
			break;
		case 0:
			printf("Soy execlp(%d) y muero\n", getpid());
			execlp("ls", "ls", NULL);
			exit(0);
	}	
};

int main(int argc, char *argv[]){
	//AGREGAR AL ARG1 Y ARG2 EL ARGV {1: ARG1, 2: ARG2}
	// argv[0] es el fichero

    // fork() > crea un proceso hijo que se ejecuta en paralelo con el proceso padre.
    // El proceso padre es el hueco reservado en RAM para ejecutar las instrucciones del script.
    // Al crar un proceso hijo se crea otro hueco en la RAM

	__pid_t pidInicial = getpid();

	proceso = argv[1][0];
	seconds = atoi(argv[2]);
	printf("Valor de argv[1]: %c\n", proceso);
	
	
	pidA = fork(); 

	switch (pidA){
		// Ha fallado el fork;
		case -1:	
			printf ("No he podido crear el proceso hijo A\n");
			break;

		// Instrucciones para el hijo A;
		case 0:
			printf ("Soy el hijo A, mi PID es %d y mi padre es %d\n", getpid(), getppid());
				
			pidB = fork(); // El hijo A tiene un hijo B
			
			switch (pidB){
				case -1:
					printf ("No he podido crear el proceso hijo B\n");
					break;
				
				// Instrucciones para el hijo B;
				case 0:
					printf ("Soy el hijo B, mi PID es %d, mi padre es %d y mi abuelo es %d\n", getpid(), getppid(), pidInicial);
					for (int i=0; i<3; i++){
						__pid_t pidXYZ = fork(); // El hijo B se transforma en Padre de XYZ

						switch (pidXYZ){
							case -1:
								printf ("No he podido crear el proceso hijo XYZ\n");
								break;

							// Instrucciones para X v Y v Z
							case 0:
							    // En cada iteración se crea un hijo distinto del mismo padre
								switch(i){
									case 0:
										pidX = getpid();
										printf ("Soy el hijo X, mi PID es %d, mi padre es %d, mi abuelo es %d y mi bisabuelo es %d\n", getpid(), getppid(), pidA, pidInicial);
										signal(SIGUSR2, handler_xy);
										pause(); //De esta forma se queda en la lista de bloqueados (esperando a la señal SIGUSR1)			
										printf("Soy X(%d) y muero\n",getpid());
										exit(0);
									case 1:
										pidY = getpid();
										printf ("Soy el hijo Y, mi PID es %d, mi padre es %d, mi abuelo es %d y mi bisabuelo es %d\n", getpid(), getppid(), pidA, pidInicial);
										signal(SIGUSR2, handler_xy);
										pause();
										printf("Soy Y(%d) y muero\n",getpid());
										exit(0);
										
									case 2:
										pidZ = getpid();
										printf ("Soy el hijo Z, mi PID es %d, mi padre es %d, mi abuelo es %d y mi bisabuelo es %d\n", getpid(), getppid(), pidA, pidInicial);				
										
										signal(SIGALRM, handler_z);
										alarm(seconds);
										pause();
									
										printf("Soy Z(%d) y muero\n",getpid());
										exit(0);
								};

							// Instrucciones para el padre B;
							default:
								switch(i){
									case 0:
										printf ("Soy el padre B, mi PID es %d y el PID de mi hijo X es %d \n", getpid(), pidXYZ);
										break; // para salirnos del switch
									case 1:
										printf ("Soy el padre B, mi PID es %d y el PID de mi hijo Y es %d \n", getpid(), pidXYZ);
										break;
									case 2:
										printf ("Soy el padre B, mi PID es %d y el PID de mi hijo Z es %d \n", getpid(), pidXYZ);
										break;
								};		

								//wait(NULL); // esperamos a que acabe el hijo correspondiente y...
								break;      // ...nos salimos del bucle for, para pasar al siguiente hijo
						};
 
					};

					signal(SIGUSR1, handler_ab);
					pause();
					wait(NULL);

				// Instrucciones para el padre A;
				default:		
					printf ("Soy el padre A, mi PID es %d y el PID de mi hijo B es %d \n", getpid(), pidB);
					wait(NULL);
					/*Podría hacer aquí el exit(0), total, esto es lo que va a ejecutar 
					el padre(y luego si no se hace exit(0) los hijos de este padre) */
			};

			signal(SIGUSR1, handler_ab);
			pause();
			wait(NULL);


		// Instrucciones para el padre R;
		default:		
			printf ("Soy el padre R, mi PID es %d y el PID de mi hijo A es %d \n", getpid(), pidA);
			// sleep (30); Muy impreciso dado que no sé cuando muere su hijo
			wait(NULL); // usamos wait para esperar de forma exacta	
			/* waitpid(pidA, NULL, 0) Según he visto de esta forma se espera a 
			la muerte del hijo en concreto y no de un hijo cualquiera */
	};

	printf ("Soy R(%d) y muero\n", getpid());
	exit (0); 
}
