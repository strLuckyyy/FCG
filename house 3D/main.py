'''

Com base nos exemplos estudados em aula, desenvolva uma cena 3D em OpenGL contendo ao menos 
3 objetos: uma casa e dois outros objetos de sua escolha 
(por exemplo: árvore, sol, personagem, etc.).

A cena deve seguir os seguintes requisitos:

Utilize VAOs simples para representar formas básicas, como, por exemplo:
* 1 VAO para um cubo
* 1 VAO para uma pirâmide

Construa os objetos mais complexos (como a casa e os demais objetos da cena) a partir 
desses VAOs básicos, aplicando transformações geométricas (translação, rotação, escala).
Cada objeto da cena deve ser desenhado utilizando instâncias dos VAOs básicos, sem criar 
novos VAOs para cada formato complexo.

Usem como base o Exemplo 7 - Câmera FPS

'''

from OpenGL.GL import *
from house import House
from window import Window
from sun import Sun
from ground import Ground
from tree import Tree

window = Window()
house = House()
sun = Sun()
ground = Ground()
tree = Tree()

obj = [house, sun, ground, tree]

def draw_obj():
    for o in obj:
        o.draw()

if __name__ == "__main__":
    window.openGLInit("Casa 3D")
    draw_obj()
    window.shaderInit()
    window.renderInit(obj)
