from object import Object
import numpy as np
from OpenGL.GL import *


class Tree(Object):
    def __init__(self):
        self.bole_vao = None
        self.leaves_vao = None
    
    def draw(self):
        # Desenhar a copa da árvore (quadrado)
        self.leaves_vao = self.squareInitialize(
            location=[-0.9, -.3], size=[.65, .7], color=[0.0, 1.0, 0.0]
        )  # Verde
        
        # Desenhar o tronco da árvore (quadrado)
        self.bole_vao = self.squareInitialize(
            location=[-.68, -0.8], size=[0.2, 0.5], color=[0.55, 0.27, 0.07]
        )  # Marrom
        
    def render(self, shader_programm):
        # Renderizar o tronco da árvore
        glBindVertexArray(self.bole_vao)
    
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)

        # --------------------------------------------------------------
        # Renderizar a copa da árvore
        glBindVertexArray(self.leaves_vao)
        
        transform = self.transformation(
            translate=[0.5, 0.0, 0.0],
            rotate=[0.0, 0.5, 0.0],
            scale=[1.0, 2.0, 1.0]
        )
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        return shader_programm