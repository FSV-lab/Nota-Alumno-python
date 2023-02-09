class Alumno:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def calcular_nota(self):
        return sum(self.calificaciones) / len(self.calificaciones)

alumno1 = Alumno("Juan", [70, 80, 90])
print("La nota del alumno " + alumno1.nombre + " es: " + str(alumno1.calcular_nota()))
