class Circulo:
    def _init_(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio

    def calcularArea(self):
        return self.__pi*self.__radio**2

    def getPi(self):
        return self.__pi

    def setRadio(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor > 0:
                self.__radio = nuevoValor
                print("El radio se ha modificado correctamente: (self.__radio)")
            else:
                print("El radio no puede ser negativo")
        else:
            print("El radio tiene que ser un número positivo")

c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())