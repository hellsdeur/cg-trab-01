from tkinter import mainloop

from src import (tela, rasterizacao, bresenham, polilinha)

# algumas cores
azul = '#0080ff'
vermelho = '#ff0000'
verde = '#00ff40'
roxo = '#bf00ff'
amarelo = '#ffff00'

# criação da tela
tela = tela.Tela(1000)

# exemplo básico de uso
'''
tela.DesenharPixel(24, 5, '#f00')
tela.DesenharPixel(5, 7, '#f00')
tela.DesenharPixel(5, 3, '#f00')
'''
pts = []
x = -30
y = 0
for i in range(30):
    if i % 2 == 0:
        x += 5
    elif y != 0:
        y = 0
    else:
        y = abs(x)
        
    pts.append((x, y))
    
linhas = polilinha.Polilinha(pts)

tela.Desenhar(linhas.saida, azul)


# interrompe a execução dos comandos e mostra a figura na tela
mainloop()