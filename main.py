from tkinter import mainloop

from src import (tela, bresenham, polilinha, curvas, circulo, transformacao,
                 preenchimento_recursivo, recorte_linha, recorte_poligono,
                 varredura)

# algumas cores
azul = '#0080ff'
vermelho = '#ff0000'
verde = '#00ff40'
roxo = '#bf00ff'
amarelo = '#ffff00'

# criação da tela
tela = tela.Tela(800)


c = curvas.Curvas(3, [(-4, 20),(-1, ) (0, 0), (-8, 2)])
tela.Desenhar(c.saida, azul)

mainloop()
