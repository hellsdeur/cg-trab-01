from tkinter import mainloop

from src import (tela, rasterizacao, bresenham)

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

linha = bresenham.Bresenham((15, -3), (-15, -15))

tela.Desenhar(linha.saida, azul)
    


# interrompe a execução dos comandos e mostra a figura na tela
mainloop()