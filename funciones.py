# Chequea que no sea una letra
def testea_numero(prompt):
    while not prompt.isnumeric():
        print("introduce un numero, no letra")
        prompt = input()
    return int(prompt)


# Chequea que sea un numero del menu
def testea_numero_menu(user_input):
    while user_input > 5 or  user_input < 0:
        print("Número incorrecto, vuelve a escoger número de la opción")
        user_input = int(input())
    return int(user_input)