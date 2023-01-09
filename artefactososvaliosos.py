#Crea una clase llamada artefactosvaliosos.py que tenga los atributos peso, nombre, precio y fecha de caducidad.
#Crea el constructor de la clase. Añade en el constructor un print para informar de que la conserva se ha creado con éxito
#Crea el método __str__ para visualizar por pantalla la información de los productos

class artefactosvaliosos:
    def __init__(self, peso, nombre, precio, fecha_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        print(f"El artefacto {self.nombre} se ha creado con éxito")

    def __str__(self) -> str:
        return f"El artefacto {self.nombre} pesa {self.peso} y su precio es de {self.precio} y su fecha de caducidad es {self.fecha_caducidad}"


#Prueba a mostrar los datos de algunos artefactos valiosos ordenados por su fecha de caducidad 
#y a modificar algún valor, por ejemplo, prueba a modificar el precio de un de la conserva

collar = artefactosvaliosos(3, "collar", 105, "13/11/2021")
pendientes = artefactosvaliosos(5, "pendientes", 50, "29/11/2023")
reloj = artefactosvaliosos(4, "reloj", 256, "12/12/2020")

objetos = [collar, pendientes, reloj]
objetos.sort(key=lambda x: x.fecha_caducidad)
for objeto in objetos:
    print(objeto)



