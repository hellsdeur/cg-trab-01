from tkinter import mainloop

from src import (tela, bresenham, polilinha, curvas, circulo, transformacao,
                 preenchimento_recursivo, recorte_linha)

# algumas cores
azul = '#0080ff'
vermelho = '#ff0000'
verde = '#00ff40'
roxo = '#bf00ff'
amarelo = '#ffff00'

# criação da tela
tela = tela.Tela(800)

# exemplo básico de uso
'''
tela.DesenharPixel(24, 5, '#f00')
tela.DesenharPixel(5, 7, '#f00')
tela.DesenharPixel(5, 3, '#f00')
'''
# c = curvas.Curvas(15, [(0, 0), (5, 5),(10,20), (20, 0)])

# c = circulo.Circulo({
#     "centro": [6,3],
#     "raio": 5
# })

p1, p2 = (-7,-5),(-1, 1)
xmin = -2
xmax = 2
ymin = -1
ymax = 1
r = recorte_linha.RecorteLinha(p1, p2, xmin, xmax, ymin, ymax)
tela.destacarJanela(xmin, xmax, ymin, ymax)

tela.Desenhar(r.saida, azul)

linha = bresenham.Bresenham(p1, p2)

#tela.Desenhar(linha.saida, azul)


# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
