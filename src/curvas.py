from src.rasterizacao import Rasterizacao


class Curvas(Rasterizacao):
    def __init__(self, pontos):
        super().__init__([pontos])

