from tkinter import mainloop

from src import (tela, bresenham, polilinha, curvas, circulo, transformacao)

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

trans_poligono = transformacao.Transformacao(
    entrada=[[0,0], [1,0], [2,0], [3,0], [3,1], [3,2], [3,3], [2,3], [1,3], [0,3], [0,2], [0,1]]
)


tela.DesenharPixel(0,0, '#f00')

tela.printMatriz()

# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
