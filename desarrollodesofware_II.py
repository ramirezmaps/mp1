class Curso:
    def __init__(self,n,a,s,c,m):
        self.nombre = n
        self.año = a
        self.semestre = s
        self.creditos = c
        self.minimo = m
        self.profesor = None
        self.lista_de_curso = []

    def __str__(self):
        return f"Curso: {self.nombre}"

    def asignar_profesor(self, p):
        self.profesor = p

    def inscribir_alumno(self, alumno):
        self.lista_de_curso.append(alumno)

    def calcular_promedio(self):
        suma = 0
        for est in self.lista_de_curso:
            suma  = suma + est.calcular_promedio()

        return (suma/len(self.lista_de_curso))

  
class Profesor:

    def __init__(self, n, e, o, d ):
        self.nombre = n
        self.edad = e
        self.oficina = o
        self.departamento = d

    def evaluar_alumno(self, estudiante, nota):
        estudiante.notas.append(nota)

    def dictar_clase(self):
        print(f"el profesor {self.nombre} está disctando una clase")

    def __str__(self):
        return f"{self.nombre} del departamento {self.departamento}, oficiina: {self.oficina}"


class Estudiante:
    def __init__(self, n, e, num_al, año_ing):
        self.nombre = n
        self.edad = e
        self.numero_alumno = num_al
        self.año_ingreso = año_ing
        self.avance = 0
        self.notas = []

    def aprueba(self):
        return (sum(self.notas) / len(self.notas)) >= 3.95
    
    def estudiar(self, mins):
        self.avance = self.avance + (0.05 * mins)

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def __str__(self):
        return f"estudiante {self.nombre}. Promedio: {self.calcular_promedio()}, ¿aprueba? {self.aprueba()}"



if __name__ == "__main__":

    curso_dsp = Curso("Desarrollo de software en python", 2022, 1, 10, True)
    profe = Profesor("Cristian", 32, "09", "DCC")

    curso_dsp.asignar_profesor(profe)
    curso_dsp.profesor.dictar_clase()
    print(curso_dsp)   

    al1 = Estudiante("Camilo",20,"123",2018)    
    al2 = Estudiante("Rocio",19,"456",2019)
    al3 = Estudiante("Dario",23,"789",2015)
    al4 = Estudiante("Rafaela",22,"012",2018)
    al5 = Estudiante("Aurora",22,"345",2018)

    curso_dsp.inscribir_alumno(al1)
    curso_dsp.inscribir_alumno(al2)
    curso_dsp.inscribir_alumno(al3)
    curso_dsp.inscribir_alumno(al4)
    curso_dsp.inscribir_alumno(al5)
    
    profe.evaluar_alumno(al1, 5.0)
    profe.evaluar_alumno(al1, 1.5)
    profe.evaluar_alumno(al3, 6.3)
    profe.evaluar_alumno(al5, 2.0)
    profe.evaluar_alumno(al4, 2.9)
    profe.evaluar_alumno(al2, 4.2)
    profe.evaluar_alumno(al2, 3.6)
    profe.evaluar_alumno(al4, 5.6)
    profe.evaluar_alumno(al2, 5.1)
    profe.evaluar_alumno(al1, 4.9)

    print(f"calcular el promedio del curso: {curso_dsp.calcular_promedio()}")

    print(al1)
    print(al2)
    print(al3)
    print(al4)
    print(al5)





  