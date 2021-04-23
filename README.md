Crear un juego de Cows & Bulls:

- El programa genera un número secreto de 4 dígitos en que ningún digito se repite. Ej bueno: 2543 – Ej malo: 1122
- El usuario intentará adivinar el número secreto insertando un numero de 4 dígitos.
- Por cada intento le indicamos cuantos Bulls y cuantas Cows ha logrado
- Un Bull se consigue cuando el intento del usuario tiene uno de los 4 dígitos del numero secreto en el orden correcto
- Un Cow se consigue cuando el intento del usuario tiene uno de los 4 dígitos del numero secreto pero en el orden incorrecto

Ejemplo:
- Numero secreto generado por el ordenador: 1674
- Primer intento del utilizador: 3476 – Bulls: 1 (sería el 7) Cows: 2 (el 4 y el 6) – En el juego no hay que indicar al usuario que números son las cows y cuáles son los bulls

El usuario tendrá que seguir jugando hasta acertar todos los dígitos en su orden correcto
Cuando el usuario consigue descubrir el numero correcto, el juego termina y indicamos cuantos intentos él necesitó.

Extras:
- Si el usuario escribe exit, el programa se cierra
- Si el usuario inserta un numero con más de 4 dígitos no contamos el intento y le decimos que ponga un numero de 4 dígitos
- Si el usuario inserta un numero con menos de 4 dígitos no contamos el intento y le decimos que ponga un numero de 4 dígitos- 
- Si el usuario inserta un número con dígitos repetidos, no contamos el intento y le decimos que tiene dígitos duplicados 
- Si el usuario inserta un texto, no contamos el intento y le decimos que tiene que insertar un numero de 4 dígitos
- Hacer tests 
