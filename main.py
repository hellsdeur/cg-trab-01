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




cubo = [
    [0, 0, 0], [4, 0, 0], [4, 4, 0], [0, 4, 0],
    [0, 0, 4], [4, 0, 4], [4, 4, 4], [0, 4, 4]
]

objeto = projecao.Projecao(entrada=cubo, recuo=-10)
objeto.projetar()
# objeto.perspectiva(dist=-30)

tela.Desenhar(objeto.saida, azul)





# interrompe a execução dos comandos e mostra a figura na tela
mainloop()
