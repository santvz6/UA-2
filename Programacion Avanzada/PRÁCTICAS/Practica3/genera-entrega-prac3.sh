#! /bin/bash

OUT="entrega.cc"
MAIN="main.cc"

if [ ! -f "Fecha.h" ]; then
   echo "ERROR: No se encuentra el fichero Fecha.h"
   exit 1
fi

if [ ! -f "Fecha.cc" ]; then
   echo "ERROR: No se encuentra el fichero Fecha.cc"
   exit 1
fi

if [ ! -f "Evento.h" ]; then
   echo "ERROR: No se encuentra el fichero Evento.h"
   exit 1
fi

if [ ! -f "Evento.cc" ]; then
   echo "ERROR: No se encuentra el fichero Evento.cc"
   exit 1
fi


if [ ! -f "Calendario.h" ]; then
   echo "ERROR: No se encuentra el fichero Calendario.h"
   exit 1
fi

if [ ! -f "Calendario.cc" ]; then
   echo "ERROR: No se encuentra el fichero Calendario.cc"
   exit 1
fi

if [ ! -f "$MAIN" ]; then
   echo "ERROR: No se encuentra el fichero $MAIN. Asegúrate de haber descomprimido correctamente el fichero descargado de Moodle"
   exit 1
fi

cat Fecha.h | grep -v '#[ ]*include[ ]*"' > $OUT
echo "" >> $OUT
cat Evento.h | grep -v '#[ ]*include[ ]*"' >> $OUT
echo "" >> $OUT
cat Calendario.h | grep -v '#[ ]*include[ ]*"' >> $OUT
echo "" >> $OUT
cat $MAIN | grep -v '#[ ]*include[ ]*"' >> $OUT
echo "" >> $OUT
cat Fecha.cc  | grep -v '#[ ]*include[ ]*"' >> $OUT
echo "" >> $OUT
cat Evento.cc  | grep -v '#[ ]*include[ ]*"' >> $OUT
echo "" >> $OUT
cat Calendario.cc  | grep -v '#[ ]*include[ ]*"' >> $OUT

echo "Ahora puedes entregar el fichero entrega.cc en jutge.org"
