from src.rasterizacao import Rasterizacao
from src.polilinha import Polilinha
from src.bresenham import Bresenham
import numpy as np


class Projecao(Rasterizacao):
    def __init__(self, entrada):
        super().__init__(entrada)

    def projetar(self, plano="xy"):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_proj = [[0 for i in range(len(self.entrada[0]))] for i in range(len(self.entrada[0]))]

        if plano == "xy":
            missed_diagonal = 2
            x_saida = 0
            y_saida = 1
        elif plano == "xz":
            missed_diagonal = 1
            x_saida = 0
            y_saida = 2
        elif plano == "yz":
            missed_diagonal = 0
            x_saida = 1
            y_saida = 2

        for i in range(0, len(self.entrada[0])):
            if i != missed_diagonal:
                matriz_proj[i][i] = 1

        for point in self.entrada:
            projecao = np.dot(matriz_proj, point)
            if [projecao[x_saida], projecao[y_saida]] not in self.saida:
                self.saida.append([projecao[x_saida], projecao[y_saida]])

    def perspectiva(self, dist):
        for ponto in self.entrada:
            ponto.append(1)

        matriz_perspectiva = [[0 for i in range(len(self.entrada[0]))] for i in range(len(self.entrada[0]))]

        for i in range(0, len(self.entrada[0])):
            if i != len(self.entrada[0])-1:
                matriz_perspectiva[i][i] = dist

        matriz_perspectiva[len(matriz_perspectiva)-1][len(matriz_perspectiva)-2] = 1

        for point in self.entrada:
            projecao = np.dot(matriz_perspectiva, point)
            # print(projecao)
            projecao = np.multiply(projecao, 1/point[2])
            self.saida.append([round(projecao[0]), round(projecao[1])])

        self.saida = Polilinha(self.saida, fechar=True).saida

        unicos = []

        for ponto in self.saida:
            if ponto[0] == ponto[1]:
                if [ponto[0], ponto[1]] not in unicos:
                    unicos.append([ponto[0], ponto[1]])

        unicos.pop(0)
        print(unicos)

        self.saida += Bresenham(unicos[0], unicos[1]).saida
