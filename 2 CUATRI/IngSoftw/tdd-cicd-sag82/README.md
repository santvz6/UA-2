[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3pirK5jc)
# Práctica 3 - TDD y CI/CD

# Implementación de una librería de procesamiento de texto

## Introducción

En esta práctica implementarás una librería llamada `textutils` que incluye un conjunto de funciones para el análisis y transformación de texto en Python. Esta librería servirá como base para practicar la escritura de pruebas unitarias, el manejo de casos límite, la validación de errores, el uso de `mock` para aislar dependencias internas y la verificación del comportamiento del código mediante `logging`. Algunas funciones serán puramente deterministas y podrán probarse de forma aislada, mientras que otras dependerán de funciones auxiliares o combinarán distintos flujos de ejecución, lo que te permitirá desarrollar pruebas de integración más completas.

La práctica está diseñada para que explores progresivamente distintas técnicas de verificación, siguiendo buenas prácticas de desarrollo y utilizando herramientas como `unittest`, `coverage`, `mock` y `logging`.

## Evaluación

Esta práctica **se puede realizar de forma individual o en grupos de dos personas**. En caso de realizarla en grupo, ambos miembros deberán participar activamente en el desarrollo de la práctica y conocer en detalle el código implementado, y su participación deberá quedar reflejada en el repositorio. 

| Concepto                                                            | Peso |
|---------------------------------------------------------------------|------|
| Implementación correcta                                             |  20% |
| Cobertura de código                                                 |  30% |
| Las pruebas cubren todos los casos descritos                        |  20% |
| GitHub Actions ejecuta pruebas automáticamente en cada pull request |  20% |
| Linting automático (flake8)                                         |  10% |

Para valorar la cobertura de código, se utilizará la herramienta `coverage` para medir el porcentaje de código cubierto por las pruebas. Se obtendrá la calificación en función del porcentaje de cobertura alcanzado. La calificación se calculará de la siguiente manera:
- Sólo casos generales (0% - 76% de cobertura): 0 puntos
- Comprobaciones básicas de los parámetros de entrada (76% - 88% de cobertura): 1 punto
- Comprobaciones adicionales (89% - 100% de cobertura): 2-3 puntos, proporcional a la cobertura alcanzada.

> Los porcentajes de cobertura son aproximados, la calificación final dependerá de la cobertura real sobre el código implementado. No se valorará la cobertura de código de las pruebas en sí mismas.

Para el apartado de linting, deberás investigar cómo configurar e integrar `flake8` en tu flujo de trabajo. Puedes usar `pre-commit` para ejecutar `flake8` automáticamente al hacer commit, o bien configurar una acción de GitHub Actions que lo ejecute al abrir un pull request.


## Metodología

Para el desarrollo de esta práctica, deberás trabajar siguiendo un flujo de trabajo basado en ramas, integrando las pruebas de la librería mediante un sistema de integración continua con GitHub Actions. Esto te permitirá verificar automáticamente que tu código cumple con los requisitos funcionales y de calidad antes de incorporarlo a la rama principal del proyecto.

### Flujo de trabajo

1. Crea una nueva rama cada vez que vayas a trabajar en una funcionalidad nueva o a corregir un error.
2. Realiza los cambios en tu rama de trabajo y asegúrate de que todas las pruebas se ejecutan correctamente de forma local.
3. Cuando hayas finalizado una funcionalidad, abre un **pull request** (PR) hacia la rama `main`.
4. Configura una acción de GitHub Actions que se ejecute automáticamente al abrir un pull request hacia `main`. Esta acción deberá:
    - Ejecutar todas las pruebas unitarias de la librería con `unittest`
    - Comprobar que la cobertura de código es suficiente (recomendado: usar `coverage`)
    - (Opcional) Ejecutar herramientas de análisis estático como `flake8` o `black`
5. El pull request no debe fusionarse hasta que todas las comprobaciones hayan pasado correctamente.

> ⚠️ **No está permitido hacer `push` directamente en la rama `main`**. Todo el desarrollo debe integrarse mediante pull requests para asegurar la validación automática del código.

### TDD

El desarrollo de la librería se realizará siguiendo la metodología TDD (Test Driven Development). Esto significa que deberás escribir primero las pruebas para cada función antes de implementar su lógica. Asegúrate de que todas las pruebas pasen antes de considerar la tarea como completada:

- Para cada función, deberás escribir todas las pruebas necesarias para cubrir los casos de uso y los casos límite. No olvides incluir pruebas que verifiquen el manejo de errores y excepciones.
- Una vez que todas las pruebas estén escritas, deberás implementar la función y asegurarte de que todas las pruebas pasen.
- Si alguna prueba no pasa, deberás corregir la implementación de la función hasta que todas las pruebas sean satisfactorias.
- Puedes hacer todos los commits que necesites en tu rama de trabajo, pero deberá haber al menos un commit que contenga únicamente las pruebas y otro commit posterior que contenga la implementación de la función. Esto te permitirá tener un historial claro de los cambios realizados.
- **Una vez que todas las pruebas pasen, deberás iniciar el pull request hacia `main`**. Asegúrate de que el código esté limpio y bien documentado antes de abrir el pull request.

Normas para escribir las pruebas:
- Deberás utilizar el módulo `unittest` de Python.
- Deberás crear un archivo de pruebas separado para cada función de la librería.
- Utiliza nombres descriptivos para las pruebas y los métodos de prueba.
- Asegúrate de que las pruebas sean claras y fáciles de entender.

> ⚠️ Recuerda que el objetivo de esta práctica es practicar TDD, por lo que **no debes implementar las funciones antes de escribir las pruebas**. Si lo haces, perderás la oportunidad de practicar TDD.

## Funciones de la librería `textutils`

A continuación se describen las funciones que deberás implementar como parte de la librería `textutils`. Cada función deberá implementarse de acuerdo a la especificación indicada, respetando los nombres y firmas indicadas para que las pruebas puedan ejecutarse correctamente.  
Salvo que se indique lo contrario, todas las funciones deben recibir como primer parámetro un texto de tipo `str`, y deberán lanzar una excepción adecuada si se recibe un tipo de dato no válido.

Algunas funciones reutilizan otras funciones de la librería internamente. En estos casos, deberás crear pruebas que validen el comportamiento de alto nivel, y utilizar `mock` para verificar que se están utilizando correctamente las funciones auxiliares.

> ⚠️ Asegúrate siempre de validar que el parámetro `text` es una cadena de texto. Si no lo es, deberás lanzar un `TypeError`.

### Funciones básicas

Estas funciones están diseñadas para ser probadas de forma unitaria. Todas ellas son deterministas y no dependen de otras funciones de la librería. Su objetivo es que practiques la escritura de pruebas simples, el análisis de casos límite y la validación de entradas.

#### `count_lines(text: str) -> int`

Devuelve el número de líneas contenidas en el texto. Se considera una línea a cualquier secuencia de caracteres que termina con un salto de línea (`\n`). Deberás ignorar líneas vacías.
- Ejemplo: `count_lines("Hola\nmundo")` devuelve `2`.
- Ejemplo: `count_lines("Hola\n\nmundo")` devuelve `2`.
- Ejemplo: `count_lines("Hola\nmundo\n")` devuelve `2`.
- Ejemplo: `count_lines("Hola\nmundo\ncruel")` devuelve `3`.
- Ejemplo: `count_lines("")` devuelve `0`.

#### `count_words(text: str) -> int`

Devuelve el número de palabras contenidas en el texto. Se consideran palabras las secuencias de caracteres separadas por espacios. Deberás ignorar espacios múltiples o al inicio/final del texto.

- Ejemplo: `count_words("Esto es una prueba")` devuelve `4`.
- Ejemplo: `count_words("   Hola    mundo  ")` devuelve `2`.
- Ejemplo: `count_words("Me he comido 2 bocadillos")` devuelve `5`.
- Ejemplo: `count_words("2 * 2")` devuelve `3`.

#### `count_letters(text: str) -> int`

Devuelve el número de letras (mayúsculas o minúsculas) contenidas en el texto. Deberás ignorar números, espacios, signos de puntuación u otros caracteres no alfabéticos.

- Ejemplo: `count_letters("Hola 123!")` devuelve `4`.

#### `remove_punctuation(text: str) -> str`

Elimina todos los signos de puntuación del texto. Puedes usar `string.punctuation` o una expresión regular para identificar los caracteres a eliminar. Deberás mantener los espacios y las letras sin cambios.

- Ejemplo: `remove_punctuation("Hola, mundo!")` devuelve `"Hola mundo"`.

### Funciones de análisis

Estas funciones pueden reutilizar otras funciones de la librería `textutils` y requieren validar el tipo de entrada o manejar errores en tiempo de ejecución. Algunas están diseñadas para que puedas aplicar `mock` sobre funciones auxiliares al escribir los tests.

#### `text_summary(text: str) -> dict`

Devuelve un resumen estadístico del texto con el número total de caracteres, palabras y líneas. Deberás utilizar las funciones `count_lines`, `count_words` y `count_letters` para calcular los valores. El resultado debe ser un diccionario con las claves `chars`, `words` y `lines`.

- Formato de retorno:
```python
{
  "chars": 123,
  "words": 22,
  "lines": 5
}
```

- Ejemplo: `text_summary("Hola mundo\nSegunda línea")` devuelve `{"chars": 24, "words": 4, "lines": 2}`.

#### `normalize_text(text: str) -> str`

Normaliza el texto eliminando signos de puntuación, convirtiéndolo todo a minúsculas y reemplazando múltiples espacios por un único espacio. Esta función debe reutilizar `remove_punctuation`.

- Ejemplo: `normalize_text(" ¡Hola, mundo! ")` devuelve `"hola mundo"`.

#### `extract_emails(text: str) -> list[str]`

Extrae todas las direcciones de correo electrónico contenidas en el texto. Las direcciones deben cumplir el patrón básico `nombre@dominio.ext`.

- El nombre puede contener letras, números, guiones bajos y puntos. El dominio debe contener letras y números, y la extensión debe ser de al menos 2 caracteres.
- Puedes usar una expresión regular para identificar las direcciones de correo electrónico.
- Si no se encuentra ninguna dirección, devuelve una lista vacía.

Esta función debe registrar (con logging, nivel INFO) cuántos correos han sido encontrados en el texto.

- Ejemplo: `extract_emails("Escribe a info@ejemplo.com o soporte@test.org")` devuelve `["info@ejemplo.com", "soporte@test.org"]`.

En caso de no encontrar ninguno, loggear un mensaje a nivel WARNING.

#### `safe_find(text: str, word: str, fallback: str = None) -> int | str`

Busca la palabra word dentro del texto. Si se encuentra, devuelve la posición (índice) en la que aparece.

Si no se encuentra y se proporciona un valor de `fallback`, devuelve ese valor. Si no se encuentra y no se proporciona un `fallback`, lanza un `ValueError`.

- Ejemplo: `safe_find("Hola mundo", "mundo")` devuelve `5`.
- Ejemplo: `safe_find("Hola mundo", "adiós")` lanza `ValueError`.
- Ejemplo: `safe_find("Hola mundo", "adiós", fallback="no encontrado")` devuelve `"no encontrado"`.

#### `classify_text(text: str) -> str`

Clasifica el contenido del texto en una de las siguientes categorías:

- `"empty"` si el texto está vacío (tras eliminar espacios en blanco).
- `"email_only"` si el texto contiene **únicamente** una dirección de correo válida.
- `"short"` si el texto contiene **menos de 10 palabras**.
- `"long"` si el texto contiene **50 palabras o más**.
- `"normal"` si no entra en ninguno de los casos anteriores.

Para realizar la clasificación, esta función debe reutilizar `extract_emails` y `count_words`. Si el parámetro `text` no es una cadena de texto, deberá lanzar un `TypeError`.

- Ejemplo: `classify_text("")` devuelve `"empty"`.
- Ejemplo: `classify_text("info@ejemplo.com")` devuelve `"email_only"`.
- Ejemplo: `classify_text("Hola mundo")` devuelve `"short"`.
- Ejemplo: `classify_text("Lorem ipsum dolor sit amet... (50 palabras)")` devuelve `"long"`.
- Ejemplo: `classify_text("Este es un texto de prueba con contenido intermedio.")` devuelve `"normal"`.
