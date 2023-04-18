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
            viajero = VF.ViajeroFrecuente(numvia,d,nom,ape)
            self.__ListaViajeros.append(viajero)
    def leerLista(self):
        for p in range (len(self.__ListaViajeros)):
            print("{} {} {} {}".format(self.__ListaViajeros[p]))

    def buscarViajero(self):
        numviajero = int(input("Ingrese el numero de viajero frecuente: "))
        viajero = VF.ViajeroFrecuente()
        v=0
        while(self.__ListaViajeros[v] != numviajero):
            if numviajero == self.__ListaViajeros[v]:
                viajero = self.__ListaViajeros[v]
                print("Se encontro al viajero")
            v += 1
        if viajero == None:
            print("No se encontro al viajero ingresado")
            exit()
        
        opcion = None
        while opcion != ["1", "2", "3"]:
            print("Menu de opciones: ")
            print("1)- Consultar Millas.")
            print("2)- Acumular Millas.")
            print("3)- Canjear Millas.")
            opcion = int(input("Ingrese una opción: "))
            if opcion == "1":
                print("Cantidad de millas acumuladas: ", viajero.cantidadTotaldeMillas())
            elif opcion == "2":
                millas = int(input("Ingrese la cantidad de millas a acumular: "))
                print("Millas acumuladas: ", viajero.acumularMillas(millas))
            elif opcion == "3":
                millas = int(input("Ingrese la cantidad de millas a canjear: "))
                print("Millas acumuladas: ", viajero.canjearMillas(millas))