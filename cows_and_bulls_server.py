import random

def generate_secret_number():
    secret_number = ''
    digits = ['0','1','2','3','4','5','6','7','8','9']
    max_value = 9
    for number in range(1, 5):
        print('max_value = ' + str(max_value))
        random_number = random.randint(0,max_value)
        print(random_number)
        new_number_for_secret_number = digits[random_number]
        secret_number = secret_number + new_number_for_secret_number
        digits.pop(random_number)
        max_value = max_value - 1
    return(secret_number)

def comprobar_resultado(secret_number_to_guess, input_del_usuario, game_in_progress):
    if (input_del_usuario == 'exit'):
        print('Bye, bye')
        game_in_progress = False
        return(game_in_progress)
    else:
        if (int(input_del_usuario) == int(secret_number_to_guess)):
            print('Genial, has ganado')
            game_in_progress = False
            return(game_in_progress)
        else: verificar_cows_and_bulls(secret_number_to_guess, input_del_usuario)

def verificar_cows_and_bulls(secret_number_to_guess, input_del_usuario):
    Bulls = 0
    Cows = 0
    for i in range(4):
        if str(input_del_usuario)[i] in secret_number_to_guess:
            if str(input_del_usuario)[i] == str(secret_number_to_guess)[i]:
                Bulls = Bulls + 1
                #print('Esto es un bull: ' + str(input_del_usuario)[i])
            else:
                Cows = Cows + 1
    print('Hay ' + str(Bulls) + ' Bulls y ' + str(Cows) + ' Cows')
    return()