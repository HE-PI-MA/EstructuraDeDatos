class Pila:

    def __init__(self):
        self._items = []


    def push(self, item):
        """
        Apilar. Agrega un elemento a la cima de la pila.
        (Actúa como 'setter', modificando el estado interno).
        """
        self._items.append(item)

    def pop(self):
        """
        Desapilar. Elimina y devuelve el elemento de la cima de la pila.
        (Actúa como 'setter' al modificar el estado y 'getter' al devolver el valor).
        """
        if self.is_empty():
            raise IndexError("pop de pila vacía: No se puede desapilar.")
        return self._items.pop()

    def peek(self):
        """
        Cima/Tope. Devuelve el elemento de la cima sin eliminarlo.
        (Actúa como 'getter', consultando el valor en el estado).
        """
        if self.is_empty():
            raise IndexError("peek de pila vacía: La pila no tiene elementos.")
        return self._items[-1]

    def is_empty(self):
        """
        Está Vacía. Retorna True si la pila no contiene elementos.
        (Actúa como 'getter', consultando el estado).
        """
        return len(self._items) == 0

    def size(self):
        """
        Tamaño. Retorna el número total de elementos en la pila.
        (Actúa como 'getter', consultando el estado).
        """
        return len(self._items)

    # Métodos opcionales para una mejor interacción
    def __len__(self):
        return self.size()
    
    def __str__(self):
        # Muestra la pila, con la cima a la derecha.
        return f"Pila: {self._items}"






# CÓDIGO DE PRUEBA Y USO (A PARTIR DE AQUÍ SE EJECUTARÁ)


# Creación de la Pila
p = Pila()
# NOTA: La salida de __str__ mostrará 'Pila: []'
print(f"Pila creada: {p}")
print(f"1. ¿Está vacía? {p.is_empty()}") # Salida: 1. ¿Está vacía (is_empty)? True

# 2. Apilar (push - Setter)
p.push(10)
p.push(20)
p.push(30)
print(f"\nPila después de la agregacion: {p}") # Salida: Pila después de pushes: Pila: [10, 20, 30]
print(f"3. Tamaño: {p.size()}") # Salida: 3. Tamaño (size): 3

# 4. Cima (peek - Getter)
print(f"4. Elemento en la cima: {p.peek()}") # Salida: 4. Elemento en la cima (peek): 30

# 5. Desapilar (pop - Setter/Getter)
item_sacado = p.pop()
print(f"5. Elemento removido: {item_sacado}") # Salida: 5. Elemento removido (pop): 30
print(f"Pila después de pop: {p}") # Salida: Pila después de pop: Pila: [10, 20]
print(f"6. Nuevo tamaño: {p.size()}") # Salida: 6. Nuevo tamaño: 2

# Intento de operación inválida
try:
    p.pop()  # Remueve 20
    p.pop()  # Remueve 10
    print(f"Pila actual antes de fallar: {p}") # Salida: Pila actual antes de fallar: Pila: []
    p.pop()  # Este pop fallará porque la pila ya está vacía
except IndexError as e:
    print(f"\nError capturado: {e}") # Salida: Error capturado: pop de pila vacía: No se puede desapilar.