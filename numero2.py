definir operación(self)

# declaramos la clase Alumno
class Alumno:
    # declaramos el metodo __init__
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=float(input("Ingrese la nota del alumno: "))

      #Declarramos el metodo mostrar
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

#declaramos la clase Alumno

class final(Alumno):
    def aprobado_reprobado(self):
        if self.nota >= 3.0:
          print("El alumno aprobo")
            
        else:
            print("El alumno desaprobo")
 
#Bloque principal
Alumno=Alumno()
Alumno.mostrar()
final1=final()
final1.aprobado_reprobado()
