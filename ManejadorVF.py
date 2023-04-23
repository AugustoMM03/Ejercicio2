import csv
import claseViajeroFrecuente as VF

class ManejadorViajeros:

    def __init__(self):
        self.__ListaViajeros = []

    def crearLista(self):    
        
        archivo = open('Viajeros.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            numvia = int(fila[0])
            d = str(fila[1])
            nom = str(fila[2])
            ape = str (fila[3])
            mill = int(fila[4])
            viajero = VF.ViajeroFrecuente(numvia,d,nom,ape,mill)
            self.__ListaViajeros.append(viajero)

    def leerLista(self):
        for p in range (len(self.__ListaViajeros)):
            print("{} {} {} {}".format(self.__ListaViajeros[p]))

    def buscarViajero(self, numviajero):
        viajero = None
        v = 0
        while(v < len(self.__ListaViajeros)):
            if numviajero == self.__ListaViajeros[v].getNumViajero():
                viajero = self.__ListaViajeros[v]
                print("Se encontro al viajero")
                return viajero
            v += 1
        if viajero == None:
            print("No se encontro al viajero ingresado")
