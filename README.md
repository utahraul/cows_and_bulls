Crear un juego de Cows & Bulls:

- El programa genera un n�mero secreto de 4 d�gitos en que ning�n digito se repite. Ej bueno: 2543 � Ej malo: 1122
- El usuario intentar� adivinar el n�mero secreto insertando un numero de 4 d�gitos.
- Por cada intento le indicamos cuantos Bulls y cuantas Cows ha logrado
- Un Bull se consigue cuando el intento del usuario tiene uno de los 4 d�gitos del numero secreto en el orden correcto
- Un Cow se consigue cuando el intento del usuario tiene uno de los 4 d�gitos del numero secreto pero en el orden incorrecto

Ejemplo:
- Numero secreto generado por el ordenador: 1674
- Primer intento del utilizador: 3476 � Bulls: 1 (ser�a el 7) Cows: 2 (el 4 y el 6) � En el juego no hay que indicar al usuario que n�meros son las cows y cu�les son los bulls

El usuario tendr� que seguir jugando hasta acertar todos los d�gitos en su orden correcto
Cuando el usuario consigue descubrir el numero correcto, el juego termina y indicamos cuantos intentos �l necesit�.

Extras:
- Si el usuario escribe exit, el programa se cierra
- Si el usuario inserta un numero con m�s de 4 d�gitos no contamos el intento y le decimos que ponga un numero de 4 d�gitos
- Si el usuario inserta un numero con menos de 4 d�gitos no contamos el intento y le decimos que ponga un numero de 4 d�gitos- 
- Si el usuario inserta un n�mero con d�gitos repetidos, no contamos el intento y le decimos que tiene d�gitos duplicados 
- Si el usuario inserta un texto, no contamos el intento y le decimos que tiene que insertar un numero de 4 d�gitos
- Hacer tests 
