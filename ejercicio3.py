class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print("Alumno creado con éxito")

    def calificacion(self):
        if self.nota>=5:
            print("El alumno", self.nombre, "ha aprobado con un", self.nota)
        else:
            print("El alumno", self.nombre, "ha suspendido con un", self.nota)


alumno1=Alumno("Pedro", 5)
alumno1.calificacion()

alumno2=Alumno("Juan", 6.3)
alumno2.calificacion()

alumno3=Alumno("Ana", 4.2)
alumno3.calificacion()
