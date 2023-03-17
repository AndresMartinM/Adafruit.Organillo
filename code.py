# Instrumento para Bicicleta

# Santiago de Chile 2022 - Andres Martin y Valentina Quilodran
# Adafruit Circuit Playground Bluefruit (lib v7)
# para un Instrumento Musical Secuencial que se monta sobre una rueda de Bicicleta
# del ramo Instrumentos Musicales Digitales - Semestre Primavera FAU

import time
import board
import analogio
import simpleio
from adafruit_circuitplayground.bluefruit import cpb

pulsoA1 = analogio.AnalogIn(board.A1)

vMin = 0.3 # voltaje minimo de lectura
vMax = 3.3 # voltaje maximo de lectura

frecMin = 80 # frecuencia para el voltaje minimo
frecMax = 1000 # frecuencia para el voltaje maximo

def getVoltage(pin):  # helper
    return (pin.value * 3.3) / 65536

def VaF(voltage):  #transforma los valores de voltage a frecuencia
    return simpleio.map_range(voltage, vMin, vMax, frecMin, frecMax)

while True:
    v = getVoltage(pulsoA1) # registramos el voltaje en un float

    if v > vMin:
        cpb.start_tone(VaF(v), 1) # el adafruit emite una frecuencia acorde al voltaje
        print("Analog Voltage: %f" % v)
        print("")
        time.sleep(0.06) # espera a que pase el tiempo
    cpb.stop_tone() # deja de sonar hasta que vuelva a pasar una corriente que supere el voltaje minimo de lectura
