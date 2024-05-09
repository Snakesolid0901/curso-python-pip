import random  # Importa el módulo random para generar opciones aleatorias.

# Función para que el usuario elija una opción.
def choose_options():
    options = ('piedra', 'papel', 'tijera')  # Opciones disponibles.
    user_option = input('piedra, papel o tijera => ')  # Solicita la opción al usuario.
    user_option = user_option.lower()  # Convierte la entrada del usuario a minúsculas para facilitar la comparación.

    if user_option not in options:  # Si la opción ingresada por el usuario no está en las opciones válidas.
        print('esa opcion no es valida')  # Imprime un mensaje de error.
        return None, None  # Devuelve None para indicar que la selección no es válida.

    computer_option = random.choice(options)  # Selecciona una opción aleatoria para la computadora.

    # Imprime las opciones elegidas por el usuario y la computadora.
    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    return user_option, computer_option  # Devuelve las opciones elegidas por el usuario y la computadora.

# Función para verificar las reglas del juego y determinar el ganador.
def check_rules(user_option, computer_option, user_wins, computer_wins):

    if user_option == computer_option:  # Si las opciones son iguales, es un empate.
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':  # Si el usuario elige piedra y la computadora tijera, el usuario gana.
            print('piedra gana a tijera')
            print('user gano!')
            user_wins += 1  # Incrementa el contador de victorias del usuario.
        else:  # En caso contrario, la computadora gana.
            print('Papel gana a piedra')
            print('computer gano!')
            computer_wins += 1  # Incrementa el contador de victorias de la computadora.
    elif user_option == 'papel':
        if computer_option == 'piedra':  # Si el usuario elige papel y la computadora piedra, el usuario gana.
            print('papel gana a piedra')
            print('user gano')
            user_wins += 1
        else:  # En caso contrario, la computadora gana.
            print('tijera gana a papel')
            print('computer gano!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':  # Si el usuario elige tijera y la computadora papel, el usuario gana.
            print('tijera gana a papel')
            print('user gano!')
            user_wins += 1
        else:  # En caso contrario, la computadora gana.
            print('piedra gana a tijera')
            print('computer gano!')
            computer_wins += 1

    return user_wins, computer_wins  # Devuelve el número actual de victorias del usuario y de la computadora.

def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print('El ganador es la computadora')
        return True  # Retorna True para indicar que el juego debe detenerse
    elif user_wins == 2:
        print('El ganador es el usuario')
        return True  # Retorna True para indicar que el juego debe detenerse
    else:
        return False  # Retorna False para indicar que el juego debe continuar

# Función principal para ejecutar el juego.
def run_game():
    computer_wins = 0  # Inicializa el contador de victorias de la computadora.
    user_wins = 0  # Inicializa el contador de victorias del usuario.
    rounds = 1  # Contador de rondas.

    while True:  # Bucle infinito para jugar múltiples rondas.
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)  # Imprime el número de victorias de la computadora.
        print('user_wins', user_wins)  # Imprime el número de victorias del usuario.

        rounds += 1  # Incrementa el número de rondas.

        user_option, computer_option = choose_options()  # El usuario elige una opción y la computadora elige una opción aleatoria.
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)  # Verifica quién gana la ronda.
        if check_winner(user_wins, computer_wins):
            break
        
        
        

run_game()  # Llama a la función principal para ejecutar el juego.