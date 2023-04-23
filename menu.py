from claseViajeroFrecuente import ViajeroFrecuente
from ManejadorVF import ManejadorViajeros

class MenuOpciones:
    def __init__(self):
        self.__opcion = None

    def opciones(self, registro):
        while self.__opcion != ("[1, 2, 3]"):
            print("Menu de opciones: ")
            print("1)- Consultar Millas.")
            print("2)- Acumular Millas.")
            print("3)- Canjear Millas.")
            print("4)- SALIR")
            self.__opcion = int(input("Seleccione una opcion: "))
            if self.__opcion == 1:
                print(registro.cantidadTotaldeMillas())
            elif self.__opcion == 2:
                mrecorridas = int(input("Ingrese la cantidad de millas recorridas: "))
                print(registro.acumularMillas(mrecorridas))
            elif self.__opcion == 3:
                mcanje = int(input("Ingrese la cantidad de millas a canjear: "))    
                print(registro.canjearMillas(mcanje))
            else:
                print("Opcion no valida, ingrese otra opcion")