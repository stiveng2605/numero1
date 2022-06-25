# declaramos la clase numeros
class numeros:
    # declaramos el metodo __init__
    def __init__(self):
        self.num1=int(input("Digite el primer numero"))
        self.num2=int(input("Digite el segundo numero"))

  #Realizamos las operaciones
    def suma(self):
      suma = self.num1 + self.num2
      print("La suma de los dos numeros es: ", suma)

    def resta(self):
      resta =  self.num1 - self.num2
      print("La resta de los dos numeros es: ", resta)

    def mult(self):
      mult = self.num1 * self.num2
      print("La multiplcacion de los dos numeros es: ", mult)

    def division(self):
      division = self.num1 / self.num2 
      print("La division de los dos numeros es: ", division)

#Bloque principal
numeros=numeros()
numeros.suma()
numeros.resta()
numeros.mult()
numeros.division()