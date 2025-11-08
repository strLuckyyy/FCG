'''

Exercício OpenGL - Casa 2D
by: Abrahão Francis Gonçalves

Main -> Arquivo atual, chama os métiodos responsáveis por:
 - inicializa o opengl
 - os objetos
 - os shades 
 - renderização da cena

Window -> Responsável pelo gerenciamento da janela e do loop de renderização. 
 Lá é definido e renderizado os shaders utilizados na renderização.

Object -> Classe base para todos os objetos na cena. 
Fornece métodos para inicializar as formas geométricas básicas (quadrados e triângulos), definir cores e transformações no mundo.

Todos os outros arquivos (ground, house, tree, sun) definem classes específicas que herdam de Object e implementam seus próprios métodos de desenho e renderização.

Eles seguem a mesma estrutura básica:
 - Definem os atributos necessários (como VAOs para diferentes partes do objeto).
 - Possuem um método draw() para inicializar a geometria do objeto.
 - Possuem um método render() para desenhar o objeto na tela usando os shaders definidos na janela.

Dentro do render(), o objeto deve vincular seu VAO, configurar a matriz de transformação e chamar a função de desenho apropriada (glDrawArrays).

Se chamar o self.transformation() sem parâmetros, ele utiliza as transformações padrão (sem translação, rotação ou escala).

A tree é a única com transformações aplicadas, as outras utilizam as transformações padrão. Fiz isso para não bagunçar tanto a imagem.

Perdão pelo atraso na entrega, acabei ficando com pouco tempo essa semana. Espero que goste do resultado! :)

'''

from window import Window
from ground import Ground
from house import House
from tree import Tree
from sun import Sun

window = Window()
ground = Ground()
house = House()
tree = Tree()
sun = Sun()

objects = [ground, house, tree, sun]

def draw_obj():
    for obj in objects:
        obj.draw()
    
def main():
    window.initializeOpenGL()
    draw_obj()
    window.initializeShaders()
    window.initializeRender(objects)
    
if __name__ == "__main__":
    main()