class Autos:
    def __init__(self,marca, modelo, patente, color, velocidad_Max, encendido):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.velocidad_Max = velocidad_Max
        self.velocidad_Min = 0
        self.encendido = False

def acelerar(self, valocidad):
    self.velocidad_actual = self.velocidad_actual + valocidad

def mostrar_informacion(self):
    return ('Este auto ' + self.marca+' '+self.modelo+' ' + 'Esta andando a ' +str(self.velocidad_actual))



mi_auto = Autos('Ford', 'Fiesta', '0AE 167','Azul', 180, False)

mi_auto.mostrar_informacion()

mi_auto.acelerar(50)

