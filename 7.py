

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def Arearet(self):
        a = self.altura * self.largura
        print('\nArea do retangulo em m²: ', a)

    def Imprimir(self):
        print('Altura: ' + str(self.altura) + ' e Largura: ' + str(self.largura))



ret = Retangulo(7, 5)
ret.Imprimir()
ret.Arearet()
