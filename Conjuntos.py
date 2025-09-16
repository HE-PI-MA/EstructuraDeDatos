class ConjuntoEstatico:
    def __init__(self, elementos):
        if not isinstance(elementos, list):
            raise TypeError("Los elementos deben pasarse como lista.")
        # Guardamos una copia sin duplicados
        self.__elementos = list(set(elementos))  

    # Getter: devuelve una copia de los elementos
    def get_elementos(self):
        return self.__elementos.copy()

    # Setter: reemplaza todos los elementos
    def set_elementos(self, nuevos_elementos):
        if not isinstance(nuevos_elementos, list):
            raise TypeError("Los nuevos elementos deben ser una lista.")
        self.__elementos = list(set(nuevos_elementos))

    def agregar_elemento(self, elemento):
        """Agrega un elemento si no está en el conjunto."""
        if elemento not in self.__elementos:
            self.__elementos.append(elemento)
        else:
            print(f"El elemento '{elemento}' ya existe en el conjunto.")

    def eliminar_elemento(self, elemento):
        """Elimina un elemento si existe en el conjunto."""
        if elemento in self.__elementos:
            self.__elementos.remove(elemento)
        else:
            print(f"El elemento '{elemento}' no está en el conjunto.")

    def union(self, otro_conjunto):
        """Devuelve un nuevo conjunto con la unión de dos conjuntos."""
        elementos_union = list(set(self.__elementos) | set(otro_conjunto.get_elementos()))
        return ConjuntoEstatico(elementos_union)

    def interseccion(self, otro_conjunto):
        """Devuelve un nuevo conjunto con la intersección."""
        elementos_interseccion = list(set(self.__elementos) & set(otro_conjunto.get_elementos()))
        return ConjuntoEstatico(elementos_interseccion)

    def diferencia(self, otro_conjunto):
        """Devuelve un nuevo conjunto con la diferencia."""
        elementos_diferencia = list(set(self.__elementos) - set(otro_conjunto.get_elementos()))
        return ConjuntoEstatico(elementos_diferencia)

    def es_subconjunto(self, otro_conjunto):
        """Verifica si este conjunto es subconjunto del otro."""
        return set(self.__elementos).issubset(set(otro_conjunto.get_elementos()))

    def contiene(self, elemento):
        """Verifica si un elemento está en el conjunto."""
        return elemento in self.__elementos

    def __str__(self):
        return "{" + ", ".join(map(str, self.__elementos)) + "}"


# 🔹 Ejemplo de uso:
conjunto1 = ConjuntoEstatico([5, 6, 7])
print("Conjunto inicial:", conjunto1)

conjunto1.agregar_elemento(8)
print("Agregado 8:", conjunto1)

conjunto1.eliminar_elemento(6)
print("Eliminado 6:", conjunto1)

# Probamos unión
conjunto2 = ConjuntoEstatico([7, 8, 9])
print("Conjunto2:", conjunto2)

union_resultado = conjunto1.union(conjunto2)
print("Unión conjunto1 y conjunto2:", union_resultado)

interseccion_resultado = conjunto1.interseccion(conjunto2)
print("Intersección conjunto1 y conjunto2:", interseccion_resultado)

diferencia_resultado = conjunto1.diferencia(conjunto2)
print("Diferencia conjunto1 - conjunto2:", diferencia_resultado)

print("¿conjunto1 es subconjunto de conjunto2?:", conjunto1.es_subconjunto(conjunto2))
print("¿conjunto1 contiene el 8?:", conjunto1.contiene(8))
