# Chequea que no sea un numero del menu
def testea_numero_menu(user_input):
    if user_input.isnumeric():
        while int(user_input) > 5 or int(user_input) < 0:
            print("Número incorrecto, vuelve a escoger número de la opción")
            user_input = int(input())
        return int(user_input)
    else:
        while not user_input.isnumeric():
            print("introduce un numero")
            user_input = input()
        return int(user_input)