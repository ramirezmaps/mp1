import re
import parametros as p
import random

###### INICIO PUNTO 1 ######
### Rellenar Clase Automóvil ###
class Automovil:
    def __init__(self, kilometraje, ano):
        self._kilometraje = kilometraje
        self.ano = ano
        self.ruedas = []
        self.aceleracion = 0 
        self.velocidad = 0
    
    def avanzar(self, tiempo):
        self._kilometraje += self.velocidad * tiempo

    def acelerar(self, tiempo):
        self.aceleracion += (tiempo) * 0.5
        self.velocidad += self.aceleracion * tiempo * 3.6
        self.avanzar(tiempo)
        self.aceleracion = 0
    
    def frenar(self, tiempo):
        self.aceleracion -= (tiempo) * 0.5
        self.velocidad += self.aceleracion * tiempo * 3.6
        if self.velocidad < 0:
            self.velocidad = 0
        self.avanzar(tiempo)
        self.aceleracion = 0

    def obtener_kilometraje(self):
        return(self.__kilometraje)
    
    def reemplazar_rueda(self):
        self.menor_resistencia = self.ruedas[0]
        self.posicion_menor = 0
        for i  in range(1,len(self.ruedas)):
            if self.ruedas[i] < self.menor_resistencia:
                self.menor_resistencia = self.ruedas[i] 
                self.posicion_menor = i
        self.ruedas.pop(self.posicion_menor)
        nueva_rueda = Rueda()
        self.ruedas.append(nueva_rueda)
###### FIN PUNTO 1 ######
###### INICIO PUNTO 2 ######
### Rellenar Clase Moto ###
class Moto(Automovil):
    def __init__(self, kilometraje, ano, cilindrada):
        super().__init__(kilometraje, ano)
        self.cilidrada = cilindrada
        rueda1 = Rueda()
        rueda2 = Rueda()
        self.ruedas = [rueda1, rueda2]
    
    def acelerar(self, tiempo):
        super().acelerar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('acelerar')
        
    def frenar(self, tiempo):
        super().frenar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('frenar')

    def __str__(self):
        return f"Moto del año {self.ano}."
###### FIN PUNTO 2 ######
###### INICIO PUNTO 3 ######
### Rellenar Clase Camión ###
class Camion(Automovil):
    def __init__(self, kilometraje, ano, carga):
        super().__init__(kilometraje, ano)
        self.carga = carga
        rueda1 = Rueda()
        rueda2 = Rueda()
        rueda3 = Rueda()
        rueda4 = Rueda()
        rueda5 = Rueda()
        rueda6 = Rueda()
        self.ruedas = [rueda1, rueda2, rueda3, rueda4, rueda5, rueda6]

    def acelerar(self, tiempo):
        super().acelerar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('acelerar')
        
    def frenar(self, tiempo):
        super().frenar(tiempo)
        for rueda in self.ruedas:
            rueda.gastar('frenar')

        

    def __str__(self):
        return f"Camión del año {self.ano}."
###### FIN PUNTO 3 ######


### Esta clase está completa, NO MODIFICAR ###
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"

### Esta funcion está completa, NO MODIFICAR ###
def seleccionar():
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    if elegido >= 0 and elegido < len(vehiculos):
        vehiculo = vehiculos[elegido]

        print("Se seleccionó el vehículo", str(vehiculo))
    else:
        print("intentelo de nuevo.")


###### INICIO PUNTO 4.2 ######
### Se debe completar cada opción según lo indicado en el enunciado ###

def accion(vehiculo, opcion):
    if opcion == 2: #Acelerar
        tiempo = int(input("Ingrese tiempo a acelerar (en segundos): "))
        vehiculo.acelerar(tiempo)
        print (f"Se ha acelerado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")

    elif opcion == 3: #Frenar
        tiempo = int(input("Ingrese tiempo de frenado (en segundos): "))
        vehiculo.frenar(tiempo)
        print (f"Se ha frenado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
        
    elif opcion == 4: #Avanzar
        tiempo = int(input("Ingrese tiempo para avanzar (en segundos): "))
        vehiculo.avanzar(tiempo)
        print (f"Se ha avanzado por {tiempo} segundos, llegando a una velocidad de {vehiculo.velocidad} km/h")
        
    elif opcion == 5: #Cambiar Rueda
        vehiculo.reemplazar_rueda()
        print("Se ha reemplazado la rueda con exito")
        
        
    elif opcion == 6: #Mostrar Estado
        print(f"Año: {vehiculo.ano}\nVelocidad: {vehiculo.velocidad}\nKilometraje: {vehiculo._kilometraje}") 
###### FIN PUNTO 4.2 ######


if __name__ == "__main__":

    ###### INICIO PUNTO 4.1 ######
    ### Aca deben instanciar los vehiculos indicados
    ### en el enunciado y agregarlos a la lista vehiculos
    vehiculos = []

    moto1 = Moto(25000, 2021, 1350)
    camion1 = Camion(50000, 1985, 35000)

    vehiculos.append(moto1)
    vehiculos.append(camion1)





    ###### FIN PUNTO 4.1 ######


    ### El codigo de abajo NO SE MODIFICA ###
    
    vehiculo = vehiculos[0] # Por default comienza seleccionado el primer vehículo  

    dict_opciones = {1: ("Seleccionar Vehiculo", seleccionar),
                     2: ("Acelerar", accion),
                     3: ("Frenar", accion),
                     4: ("Avanzar", accion),
                     5: ("Reemplazar Rueda", accion),
                     6: ("Mostrar Estado", accion),
                     0: ("Salir", None)
                    }

    op = -1
    while op != 0:
        
        for k, v in dict_opciones.items():
            print(f"{k}: {v[0]}")
        
        try:
            op = int(input("Opción: "))
        
        except ValueError:
            print(f"Ingrese opción válida.")
            op = -1
        
        if op != 0 and op in dict_opciones.keys():
            if op == 1:
                dict_opciones[op][1]()
            else:
                dict_opciones[op][1](vehiculo, op)
        elif op == 0:
            pass
        else:
            print(f"Ingrese opción válida.")
            op = -1
