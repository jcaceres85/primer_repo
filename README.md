# JUEGO DEL AHORCADO

#### Por José Cáceres

![Logo_UNAH](https://www.unah.edu.hn/themes/portalunah/assets/images/logo-unah.png)

TABLA DE CONTENIDO
===================
- [INTRODUCCIÓN](#intro)
- [INSTRUCCIONES](#instrucciones)
- [REQUISITOS DEL JUEGO AHORCADOS](#requisitos)


Este conjunto de problemas le dará a conocer el tema de la creación de funciones en Python, así como mecanismos de bucle para repetir un proceso de cálculo hasta que se alcanza una condición. Deberá guardar sus códigos (3) con su primer nombre y su primer apellido, seguido del problema de aplicación y la parte del problema que representa el código pa02_parte1.py (Lois_Lane_pa02_parte1.py, Lois_Lane_pa02_parte2.py, Lois_Lane_pa02_parte3.py). ¡No olvide incluir comentarios para ayudar a entender su código!

Colaboración
Puedes trabajar en parejas. Sin embargo, cada estudiante debe escribir y entregar su tarea por separado. Asegúrese de indicar con quién ha trabajado en los comentarios de su presentación.

INTRODUCCIÓN
----------------
Vas a implementar una variación del juego clásico de palabras Ahorcado. Si no estás familiarizado con las reglas del juego, puedes leer https://es.wikipedia.org/wiki/Ahorcado_(juego). ¡No te sientas intimidado por este problema, realmente es más fácil de lo que parece! Vamos a abordar este problema, guiándolo a través de la creación de funciones de ayuda antes de implementar el juego real.

INSTRUCCIONES
--------------
Descarga los archivos “ahorcado_detallado.py” y “palabras.txt” y guarda ambos en el mismo directorio. Ejecuta el archivo ahorcado.py antes de escribir algún código para asegurarse que sus archivos se guardan correctamente. El código que se te ha dado carga las palabras desde un archivo. Deberías ver la siguiente salida en el Shell de IPython:
	Cargando lista de palabras desde archivo...
    78566 palabras cargadas.
Si ve el texto anterior, continúe con los Requisitos del Juego Ahorcado.
¡Si no lo hace, vuelva a verificar que ambos archivos estén guardados en el mismo lugar!


REQUISITOS DEL JUEGO AHORCADOS
-------------
Implementarás una función llamada hangman que permitirá al usuario jugar al ahorcado contra la computadora. La computadora elige la palabra y el jugador intenta adivinar las letras de la palabra.
Aquí está el comportamiento general que queremos implementar. ¡No te intimides! Esta es solo una descripción: dividiremos esto en pasos y proporcionaremos más especificaciones funcionales más adelante en la descripción del problema, así que ¡sigue leyendo!
La computadora debe seleccionar una palabra al azar de la lista de palabras disponibles que se proporcionó en words.txt
Tenga en cuenta que palabras.txt contiene palabras en letras minúsculas.
El usuario recibe un cierto número de conjeturas al comienzo.
El juego es interactivo, el usuario ingresa su conjetura y la computadora:
revela la letra si existe en la palabra secreta
penalizar al usuario y actualiza el número de conjeturas restantes
El juego termina cuando el usuario adivina la palabra secreta o el usuario se queda sin intentos.
