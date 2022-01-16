from src.rasterizacao import Rasterizacao
from math import pi, sin, cos, radians


class Transformacao(Rasterizacao):
    def __init__(self, entrada):
        super().__init__(entrada)

    def translar(self, trans_x, trans_y):
        for ponto in self.entrada:
            ponto[0] += trans_x
            ponto[1] += trans_y
            self.saida.append(ponto)

    def escalar(self, esc_x, esc_y):
        for ponto in self.entrada:
            ponto[0] *= esc_x
            ponto[1] *= esc_y
            self.saida.append(ponto)

    def rotacionar(self, pivo, angulo):
        # de acordo com a distância pivo-origem, translar objeto para a origem
        trans_x = 0 - pivo[0]
        trans_y = 0 - pivo[1]
        self.translar(trans_x, trans_y)

        angulo_rad = radians(angulo)

        for ponto in self.entrada:
            print(f"Ponto original: {ponto[0]}, {ponto[1]}")

            print(f"x'\t= x\t\t* cos({angulo})\t- y\t\t* sin({angulo})")
            print(f"x'\t= {ponto[0]}\t* {round(cos(angulo_rad), 5)}\t\t- {ponto[1]}\t* {round(sin(angulo_rad), 5)}\t = ", end="")
            ponto[0] = (ponto[0] * round(cos(angulo_rad), 5)) - (ponto[1] * round(sin(angulo_rad), 5))
            print(ponto[0])

            print('\n')

            print(f"y'\t= x\t\t* sin({angulo})\t+ y\t\t* cos({angulo})")
            print(f"y'\t= {ponto[0]}\t* {round(sin(angulo_rad), 5)}\t\t+ {ponto[1]}\t* {round(cos(angulo_rad), 5)}\t = ", end="")
            ponto[1] = (ponto[0] * round(sin(angulo_rad), 5)) + (ponto[1] * round(cos(angulo_rad), 5))
            print(ponto[1])

            print('\n')
            print("="*33)
            print('\n')

            self.saida.append(ponto)

        # retornar para posição inicial
        self.translar(-trans_x, -trans_y)
