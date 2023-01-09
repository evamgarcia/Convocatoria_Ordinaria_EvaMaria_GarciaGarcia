#Poe Dameron, líder del escuadrón negro de la Resistencia, tiene dificultades para transmitir 
# los mensajes a la base de la Resistencia, dado que los mismos son muy largos y los satélites espías de la 
# Primera Orden los intercepta, en un lapso muy corto desde que se transmiten. 
# Por lo cual, nos solicita desarrollar un algoritmo que permita comprimir los mensajes 
# para enviarlos más rápido y no puedan ser interceptados. Contemplando los siguientes requerimientos, 
# implementar un algoritmo que pueda crear un árbol de Huffman a partir de la siguiente tabla y 
# desarrollar las funcionas para comprimir y descomprimir un mensaje.

from queue import PriorityQueue

class Node:
    def __init__(self, caracter, frecuencia, izquierda= None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha
    
    def _lt_(self, other):
        return self.frecuencia < other.frecuencia

def crear_arbol_huffman(frecuencias):
    pq = PriorityQueue()
    for caracter, frecuencia in frecuencias.items():
        pq.put(Node(caracter, frecuencia))
    while pq.qsize() > 1:
        left = pq.get()
        right = pq.get()
        node = Node(None, left.frecuencia + right.frecuencia, left, right)
        pq.put(node)
    return pq.get()

    

frecuencias = {
    "A":0.2,
    "F":0.17,
    "1":0.13,
    "3":0.12,
    "0":0.1,
    "M":0.08,
    "T":0.07
}

arbol = crear_arbol_huffman(frecuencias)

