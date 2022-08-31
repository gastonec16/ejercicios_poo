lista_personas = []
lista_cuentas = []

class Persona:
    def __init__(self, nombre='', edad=0, dni=0):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def dni(self):
        return self._dni

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @edad.setter
    def edad(self, value):
        self._edad = value

    @dni.setter
    def dni(self, value):
        self._dni = value

    def mostrar(self):
        print(f'''Datos de persona:
                Nombre:\t{self.nombre}
                Edad:\t{self.edad}
                DNI:\t{self.dni}''')

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def es_titular_valido(self):
        return self.es_mayor_de_edad() and self.edad < 25
    
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad

    @titular.setter
    def titular(self, value):
        self._titular = value
    
    @cantidad.setter
    def cantidad(self, value):
        self._cantidad = value

    def mostrar(self):
        print(f'''Datos de Cuenta:
                Titular:\t{self.titular.nombre}
                Cantidad:\t{self.cantidad}''')

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print('No se ha ingresado dinero a la cuenta')

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad
        else:
            print('No se ha retirado dinero de la cuenta')

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, value):
        self._bonificacion = value

    def mostrar(self):
        print(f'''Datos de Cuenta Joven:
                Titular:\t{self.titular.nombre}
                Cantidad:\t{self.cantidad}
                Bonificación:\t{self.bonificacion}''')
