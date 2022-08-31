from clases import lista_personas, lista_cuentas, Persona, Cuenta, CuentaJoven

def ingresar_float(nombre):
    while True:
        try:
            numero = input(f'Ingrese {nombre}: ')
            if numero == '':
                return 0
            numero = float(numero)
            return numero
        except:
            print('ERROR: Debe ingresar un número')

def instanciar_persona():
    while True:
        nombre = input('Ingrese nombre: ')
        if nombre == '':
            break
        for i in nombre:
            if i.isdigit():
                print('ERROR: No se pueden ingresar números')
                break
        else:
            break
    while True:
        try:
            edad = input('Ingrese edad: ')
            if edad == '':
                edad = 0
                break
            edad = int(edad)
            if edad < 0 or edad > 199:
                print('ERROR: No es un número válido')
            else:
                break
        except:
            print('ERROR: Debe ingresar un número entero')
    while True:
        try:
            dni = int(input('Ingrese DNI: '))
            if dni < 100000 or dni > 9999999999:
                print('ERROR: No es un número válido')
                continue
            for i in lista_personas:
                if i.dni == dni:
                    print('ERROR: Ya hay una persona registrada con este DNI')
                    break
            else:
                break
        except:
            print('ERROR: Debe ingresar un número entero')
    
    persona = Persona(nombre, edad, dni)
    lista_personas.append(persona)
    print('Se ha registrado una nueva persona')
    persona.mostrar()

def buscar_persona():
    while True:
        try:
            dni = int(input('Ingrese DNI de la persona: '))
            if dni < 100000 or dni > 9999999999:
                print('ERROR: No es un número válido')
                continue
            for i in lista_personas:
                if i.dni == dni:
                    return i
            else:
                print('ERROR: No hay una persona registrada con ese DNI')
        except:
            print('ERROR: Debe ingresar un número entero')

def instanciar_cuenta(tipo):
    titular = buscar_persona()
    cantidad = ingresar_float('cantidad')
    if tipo == 1:
        cuenta = Cuenta(titular, cantidad)
        lista_cuentas.append(cuenta)
        print('Se ha registrado una nueva Cuenta')
        cuenta.mostrar()
    elif tipo == 2:
        if titular.es_titular_valido():
            bonificacion = ingresar_float('bonificación')
            cuenta = CuentaJoven(titular, cantidad, bonificacion)
            lista_cuentas.append(cuenta)
            print('Se ha registrado una nueva Cuenta Joven')
            cuenta.mostrar()
        else:
            print('ERROR: La persona debe tener entre 18 y 24 años')

def mostrar_cuentas():
    cuentas = []
    persona = buscar_persona()
    for i in lista_cuentas:
        if i.titular.dni == persona.dni:
            cuentas.append(i)
    print(f'Cuentas de {persona.nombre}:')
    for i in cuentas:
        i.mostrar()


