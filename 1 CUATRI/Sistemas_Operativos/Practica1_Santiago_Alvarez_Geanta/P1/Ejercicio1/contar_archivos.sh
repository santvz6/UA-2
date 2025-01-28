conteo=$(find "$1" -type f -o -type d | wc -l)

echo "El número total de archivos y directorios en '$1' es: $conteo"