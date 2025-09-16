# Automovil estático 

class AutomovilEstatico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
       
    # Getters
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo



    # Setters
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo


# Crear un automóvil
auto1 = AutomovilEstatico("Toyota", "Corolla")
print(auto1.get_marca()) 
