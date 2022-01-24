from src.rasterizacao import Rasterizacao
from src.polilinha import Polilinha
from math import sin, cos, radians
import numpy as np


class Transformacao(Rasterizacao):
    def __init__(self, entrada):
        super().__init__(entrada)
        self.saida = entrada

    def translar(self, trans_x, trans_y):
        self.saida = []
        for ponto in self.entrada:
            ponto[0] += trans_x
            ponto[1] += trans_y
            self.saida.append(ponto)

    def escalar(self, esc_x, esc_y):
        self.saida = []
        for ponto in self.entrada:
            ponto[0] *= esc_x
            ponto[1] *= esc_y
            self.saida.append(ponto)
        self.saida.append(self.saida[0])

        self.saida = Polilinha(self.saida).saida

    def rotacionar(self, pivo, angulo):
        self.saida = []
        # de acordo com a distância pivo-origem, translar objeto para a origem
        trans_x = 0 - pivo[0]
        trans_y = 0 - pivo[1]
        translacao = Transformacao(self.entrada)
        translacao.translar(trans_x, trans_y)
        self.entrada = translacao.saida

        # transformar para radianos
        angulo_rad = radians(angulo)

        # montar a matriz de rotação
        matriz_rotacao = [[cos(angulo_rad), -sin(angulo_rad)], [sin(angulo_rad), cos(angulo_rad)]]

        # multiplicação de matrizes entre a rotação e cada coluna da entrada
        for ponto in self.entrada:
            self.saida.append([round(x) for x in np.dot(matriz_rotacao, ponto)])

        # translar objeto de volta
        translacao = Transformacao(self.saida)
        translacao.translar(-trans_x, -trans_y)
        self.saida = translacao.saida
