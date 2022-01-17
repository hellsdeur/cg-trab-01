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


pts = [(-5,5),(-5, -5),(5, -5), (5, 5)]
xmin = -1
xmax = 10
ymin = -9
ymax = 9

obj = recorte_poligono.RecortePoligono(pts, xmin, xmax, ymin, ymax)
tela.destacarJanela(xmin, xmax, ymin, ymax)
tela.Desenhar(obj.saida, azul)

'''
poligono_original = polilinha.Polilinha(pts, fechar=True)
tela.Desenhar(poligono_original.saida, azul)
'''





# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
