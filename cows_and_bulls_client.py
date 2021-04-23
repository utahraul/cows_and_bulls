import sys
import cows_and_bulls_server

secret_number_to_guess = cows_and_bulls_server.generate_secret_number()
print(secret_number_to_guess)

game_in_progress = True
number_of_rounds = 0

while (game_in_progress):
    input_del_usuario = input("He generado un numero secreto de 4 digitos en que ninguna cifra se repite. Cual crees que es: ")
    print(input_del_usuario)
    print(game_in_progress)

    cows_and_bulls_server.comprobar_resultado(secret_number_to_guess, input_del_usuario, game_in_progress)