class stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"El stormtrooper {self.nombre} se ha creado con éxito")
    
    def __str__(self) -> str:
        return f"Stormtrooper {self.nombre} es un {self.rango}"
        
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