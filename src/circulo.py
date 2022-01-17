from src.rasterizacao import Rasterizacao


class Circulo(Rasterizacao):
    def __init__(self, entrada):
        super().__init__(entrada)

        self.centro = self.entrada["centro"]
        self.raio = round(self.entrada["raio"])

        self.ponto_medio()

    def ponto_medio(self):
        # parametros iniciais e primeiros traços no octante
        x = 0
        y = self.raio
        e = -self.raio
        self.desenha_octantes(x, y)

        # desenho no segundo octante é replicado aos demais
        while x <= y:
            # ajusta o erro do x e incrementa para a direita
            e = self.e_prox(x, y, e)
            x += 1

            # se estiver dentro do círculo então decrementa y, se não então mantenha y
            if e >= 0:
                e = self.e_fin(x, y, e)
                y -= 1

            # replica nos 8 octantes, com desvio de centro
            self.desenha_octantes(x, y)

    def e_prox(self, x, y, e):
        return e + 2*x + 1

    def e_fin(self, x, y, e):
        return e - 2*y + 2

    def desenha_octantes(self, x, y):
        self.saida.append([x + self.centro[0], y + self.centro[1]])
        self.saida.append([y + self.centro[0], x + self.centro[1]])
        self.saida.append([y + self.centro[0], -x + self.centro[1]])
        self.saida.append([x + self.centro[0], -y + self.centro[1]])
        self.saida.append([-x + self.centro[0], -y + self.centro[1]])
        self.saida.append([-y + self.centro[0], -x + self.centro[1]])
        self.saida.append([-y + self.centro[0], x + self.centro[1]])
        self.saida.append([-x + self.centro[0], y + self.centro[1]])




