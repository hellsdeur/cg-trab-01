from tkinter import mainloop

from src import (tela, bresenham, polilinha, curvas, circulo, transformacao,
                 preenchimento_recursivo, varredura, projecao, recorte_linha,
                 recorte_poligono)

# algumas cores
azul = '#0080ff'
vermelho = '#ff0000'
verde = '#00ff40'
roxo = '#bf00ff'
amarelo = '#ffff00'

# criação da tela
tela = tela.Tela(800)

p1, p2 = (-7,-5),(-1, 1)
xmin = -2
xmax = 2
ymin = -1
ymax = 1
r = recorte_linha.RecorteLinha(p1, p2, xmin, xmax, ymin, ymax)
tela.destacarJanela(xmin, xmax, ymin, ymax)



# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
