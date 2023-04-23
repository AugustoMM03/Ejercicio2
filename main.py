import claseViajeroFrecuente as VF
import ManejadorVF
from menu import MenuOpciones

def test():
    controlador = ManejadorVF.ManejadorViajeros()
    controlador.crearLista()
    numviajero = int(input("Ingrese un numero de viajero: "))
    reg = controlador.buscarViajero(numviajero)
    menu = MenuOpciones()
    menu.opciones(reg)

if __name__== '__main__':
    test()