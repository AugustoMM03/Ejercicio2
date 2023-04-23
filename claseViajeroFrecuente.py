#En una aerolínea ofrece una promoción a sus viajeros frecuentes que consiste en acumular puntos por los viajes que realizan, pudiendo luego recibir 
#beneficios a través del canje de puntos.
#Usted trabaja en el área de sistemas de la aerolínea y le han solicitado la implementación de un sistema capaz de gestionar la promoción. 

#Respetando el siguiente diseño de clase:
#    Atributos: número de viajero, DNI, nombre, apellido y millas acumuladas.
#    Métodos:
#        a- El constructor.
#        b- “cantidadTotaldeMillas”, retorna la cantidad de millas acumuladas.
#        c- “acumularMillas”, recibe como parámetro la cantidad de millas recorridas, las suma en el atributo correspondiente y retorna el valor del 
#        atributo actualizado.
#        d- “canjearMillas”, recibe como parámetro la cantidad de millas a canjear. Para utilizar las millas debe verificarse que la cantidad a canjear 
#        sea menor o igual a la cantidad de millas acumuladas, caso contrario mostrar un mensaje de error en la operación. Retorna el valor de la cantidad
#        de millas acumuladas.


#1- Leer de un archivo separado por comas los datos para crear instancias de la clase ViajeroFrecuente, y almacenarlas en una lista.

#2- El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con las siguientes opciones:

#        a- Consultar Cantidad de Millas.
#        b- Acumular Millas.
#        c- Canjear Millas.

#3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.    


import csv

class ViajeroFrecuente:
    __numeroviajero = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millasacumuladas = 0 
    def __init__(self, numeroviajero = 0, dni='', nombre='', apellido='', millasacumuladas=0):
        self.__numeroviajero = numeroviajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasacumuladas = millasacumuladas
    
    def cantidadTotaldeMillas(self):
        return self.__millasacumuladas
    
    def acumularMillas(self, recorridas):
        self.__millasacumuladas += recorridas
        return self.__millasacumuladas

    def canjearMillas(self, canjear):
        if canjear > self.__millasacumuladas:
            print("Error en la operacion, no tiene millas suficientes para realizar el canje, tiene: ")
        else:
            self.__millasacumuladas -= canjear
            print("Millas canjeadas, le quedan: ")
        return self.__millasacumuladas

    def getNumViajero(self):
        return self.__numeroviajero