COMP=g++
OPT=-Wall -std=c++11

ejemplo: Ejemplo.o Fecha.o
	$(COMP) $(OPT) -o ejemplo Ejemplo.o Fecha.o

Ejemplo.o: Ejemplo.cc Fecha.h
	$(COMP) $(OPT) -c  Ejemplo.cc

Fecha.o: Fecha.cc Fecha.h
	$(COMP) $(OPT) -c Fecha.cc

clean:
	rm *.o ejemplo
