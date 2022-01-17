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


obj = circulo.Circulo({
    "centro": [11,-7],
    "raio": 7
})

tela.Desenhar(obj.saida, azul)


# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
