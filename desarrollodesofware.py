class Curso:
    def __init__(self,n,a,s,c,m):
        self.nombre = n
        self.año = a
        self.semestre = s
        self.creditos = c
        self.minimo = m
        self.profesor = None
    
    def __str__(self):
        return f"Curso: {self.nombre}"

    def asignar_profesor(self, p):
        self.profesor = p

  
class Profesor:

    def __init__(self, n, e, o, d ):
        self.nombre = n
        self.edad = e
        self.oficina = o
        self.departamento = d

    def dictar_clase(self):
        print(f"el profesor {self.nombre} está disctando una clase")

    def __str__(self):
        return f"{self.nombre} del departamento {self.departamento}, oficiina: {self.oficina}"


if __name__ == "__main__":

    curso_dsp = Curso("Desarrollo de software en python", 2022, 1, 10, True)
    profe = Profesor("Cristian", 32, "09", "DCC")

    curso_dsp.asignar_profesor(profe)
    curso_dsp.profesor.dictar_clase()

    print(curso_dsp)





