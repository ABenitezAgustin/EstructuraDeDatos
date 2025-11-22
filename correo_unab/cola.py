class Nodo:
    # Nodo para construir colas
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class Cola:
    """Implementación de una cola usando nodos."""
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def enqueue(cola, dato):
    """Agregar un elemento al final de la cola."""
    nodo = Nodo(dato)
    if cola.frente is None:          # La cola está vacía
        cola.frente = nodo
        cola.final = nodo
    else:
        cola.final.siguiente = nodo
        cola.final = nodo

    cola.tamanio += 1


def dequeue(cola):
    """Quitar y devolver el nodo del frente de la cola."""
    if cola.tamanio == 0:
        raise RuntimeError("No se puede remover un elemento de una cola vacía")
    
    nodo_a_devolver = cola.frente
    cola.frente = nodo_a_devolver.siguiente
    
    if cola.frente is None:     # la cola quedó vacía
        cola.final = None

    cola.tamanio -= 1
    return nodo_a_devolver


def is_empty(cola):
    return cola.tamanio == 0
