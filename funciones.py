# Chequea que no sea un numero del menu
def testea_numero_menu(user_input,min,max):
    if user_input.isnumeric():
        while int(user_input) > min or int(user_input) < max:
            print("Número incorrecto, vuelve a escoger número de la opción")
            user_input = int(input())
        return int(user_input)
    else:
        while not user_input.isnumeric():
            print("introduce un numero")
            user_input = input()
        return int(user_input)