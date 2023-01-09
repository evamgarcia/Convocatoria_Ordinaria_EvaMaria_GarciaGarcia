class stormtrooper:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print(f"El stormtrooper {self.nombre} se ha creado con éxito")
    
    def __str__(self) -> str:
        return f"Stormtrooper {self.nombre} es un {self.rango}"
        
