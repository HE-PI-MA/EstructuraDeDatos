# Automovil dinámico
class NodoAutomovil:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.siguiente = None

class ListaAutomoviles:
    def __init__(self):
        self.cabeza = None

    def agregar_automovil(self, marca, modelo, año):
        nuevo_auto = NodoAutomovil(marca, modelo, año)
        nuevo_auto.siguiente = self.cabeza
        self.cabeza = nuevo_auto

    def mostrar_automoviles(self):
        actual = self.cabeza
        while actual:
            print(f"Marca: {actual.marca}, Modelo: {actual.modelo}, Año: {actual.año}")
            actual = actual.siguiente


# Ejemplo de uso:
lista = ListaAutomoviles()
lista.agregar_automovil("Toyota", "Hilux", 2021)
lista.agregar_automovil("Nissan", "Navara", 2019)
lista.mostrar_automoviles()
