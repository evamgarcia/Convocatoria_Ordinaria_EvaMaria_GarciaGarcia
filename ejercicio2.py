#Crea una clase llamada stormtrooper.py que tenga los atributos nombre y rango
#Crea el constructor de la clase. 
# Añadir en el constructor un print para informar de que el stormtrooper se ha creado con éxito.
# Crear un método llamado calificacion que clasifique a los Stormtrooper del imperio galáctico de la siguiente manera:

class stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print("El stormtrooper {self.nombre} se ha creado con éxito")

class rango(stormtrooper):
   identificador_de_cohoerte = 8 
   identificador_de_siglo = 6 
   numero_de_clase = 4
   numero_de_serie = 2
   def __init__(self, nombre, rango):
       super().__init__(nombre, rango)
       self.identificador_de_cohoerte = identificador_de_cohoerte
       self.identificador_de_siglo = identificador_de_siglo
       self.numero_de_clase = numero_de_clase
       self.numero_de_serie = numero_de_serie

class calificacion(stormtrooper):
    codigo_de_legion = "TK"
    def __init__(self, nombre, rango):
        super().__init__(nombre, rango)
        self.codigo_de_legion = codigo_de_legion





