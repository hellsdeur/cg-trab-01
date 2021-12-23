from src.rasterizacao import Rasterizacao
from src.bresenham import Bresenham


class Polilinha(Rasterizacao):
    def __init__(self, pontos:list):
        super().__init__(pontos)
        
        for x in range(len(pontos)-1):
            linha = Bresenham(pontos[x], pontos[x+1])
            
            for pt in linha.saida:
                self.saida.append(pt)
            
        
        