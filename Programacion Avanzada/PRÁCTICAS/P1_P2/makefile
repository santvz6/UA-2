COMP=g++
OPT=-Wall -std=c++11

# Archivo ejecutable final
ejemplo: ejemplo.o Calendario.o Evento.o
	$(COMP) $(OPT) -o ejemplo ejemplo.o Calendario.o Evento.o

# Compilación de Ejemplo.cc
ejemplo.o: Ejemplo.cc Calendario.h Evento.h
	$(COMP) $(OPT) -c Ejemplo.cc

# Compilación de Calendario.cc
Calendario.o: Calendario.cc Calendario.h Evento.h
	$(COMP) $(OPT) -c Calendario.cc

# Compilación de Evento.cc
Evento.o: Evento.cc Evento.h
	$(COMP) $(OPT) -c Evento.cc

# Limpieza de archivos intermedios
clean:
	rm -f *.o ejemplo
