#Suponga que Obi-Wan Kenobi está atrapado bajo el fuego de los stormtroppers, 
# pero muy cerca está su mochila que contiene muchos artefactos valiosos que debe 
# impedir a toda costa que sean requisados por El Imperio.
# Implementa una función recursiva llamada “usar la fuerza” que le permita Obi-Wan Kenobi en su último aliento 
#y “con ayuda de la fuerza” realizar las siguientes actividades:
# sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o 
# que no queden más objetos en la mochila;
# Determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# Utilizar una lista para representar la mochila.

class mochila_artefactos():
    def init (self):
        self.objetos = []
    def str (self):
        return str(self.objetos)
    def len(self):
        return len(self.objetos)

    def agregar_objetos(self, objetos):
        self.objetos.append(objetos)

    def sacar_objetos(self,objetos):
        self.objetos.remove(objetos)

    def usar_la_fuerza(self, i=0):
        if i == len(self.objetos):
            return f"No se encontró el sable de luz"
        if self.objetos[i] == "sable de luz":
            return f"El sable de luz estaba" + str(i+1) + "de la mochila"
        return self.usar_la_fuerza(i+1)


mochila = mochila_artefactos()
mochila.agregar_objetos("sable de luz")
mochila.agregar_objetos("collar")
mochila.agregar_objetos("nave")
mochila.agregar_objetos("fuerza")
mochila.agregar_objetos("libros")

print(mochila.usar_la_fuerza())