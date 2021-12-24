from src.rasterizacao import Rasterizacao
from src.bresenham import Bresenham

'''
para construir uma curva são calculados pontos (que fazem parte da curva)
a partir dos pts de controle. Em seguida, os pontos calculados são
conectados com o algoritmo de Bresenham.

a variavel n define quantos pontos serão calculados
'''


class Curvas(Rasterizacao):
    def __init__(self, n, pts_controle: list):
        super().__init__([pts_controle])

        self.pontos = []
        passo = 1 / n
        t = 0.0

        for d in range(n+1):
            self.pontos.append(self.casteljau(t, pts_controle))
            t += passo

        self.juntar_pontos()

    def casteljau(self, t, pontos_controle):
        pts = []
        for p in pontos_controle:
            pts.append(list(p))

        for i in range(1, len(pts)):
            for j in range(len(pts)-i):
                pts[j][0] = (1 - t) * pts[j][0] + t * pts[j+1][0]
                pts[j][1] = (1 - t) * pts[j][1] + t * pts[j + 1][1]

        return [int(pts[0][0]), int(pts[0][1])]

    def juntar_pontos(self):
        for x in range(len(self.pontos) - 1):
            linha = Bresenham(self.pontos[x], self.pontos[x + 1])

            for pt in linha.saida:
                self.saida.append(pt)
