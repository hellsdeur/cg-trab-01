from tkinter import mainloop

from src import (tela, rasterizacao)

# criação da tela
tela = tela.Tela(600)

# exemplo básico de uso
tela.DesenharPixel(24, 5, '#f00')
tela.DesenharPixel(5, 7, '#f00')
tela.DesenharPixel(5, 3, '#f00')

# interrompe a execução dos comandos e mostra a figura na tela
mainloop()