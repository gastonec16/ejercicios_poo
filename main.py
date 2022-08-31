from funciones import instanciar_persona, instanciar_cuenta, buscar_persona, mostrar_cuentas

menu = ''
while menu != '6':

    menu = input(f'''Seleccione una opción:
            1. Agregar persona
            2. Mostrar información de persona
            3. Crear Cuenta
            4. Mostrar información de cuenta
            5. Crear Cuenta Joven
            6. Salir
    Opción: ''')

    match(menu):
        case '1':
            instanciar_persona()
        case '2':
            buscar_persona().mostrar()
        case '3':
            instanciar_cuenta(1)
        case '4':
            mostrar_cuentas()
        case '5':
            instanciar_cuenta(2)
        case '6':
            break
        case _:
            print('ERROR: No es una opción válida')
