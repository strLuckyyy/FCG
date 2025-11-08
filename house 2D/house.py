from object import Object
from OpenGL.GL import *
import numpy as np

class House(Object):
    def __init__(self):
        self.base_vao = None
        self.door_vao = None
        self.roof_vao = None
        self.window = None
    
    def draw(self):
        # Base da casa (quadrado)
        self.base_vao = self.squareInitialize([-.3,-.5-.3], [1,.65], self.rgbToFloat(189,135,65))  # Marrom

        # Telhado da casa (triângulo)
        self.roof_vao = self.triagleInitialize(True, [-.35, .15-.3], [1.1, .5], self.rgbToFloat(255, 155, 0)) # Laranja
        
        # Desenhar a porta da casa (quadrado)
        self.door_vao = self.squareInitialize(location=[-.1, -.48-.3], size=[0.2, 0.4], color=[1, 1, .8])

        # Desenhar a janela da casa (quadrado)
        self.window = self.squareInitialize(location=[.3, -.2-.3], size=[0.2, 0.2], color=self.rgbToFloat(0, 191, 255))  # Azul claro

    def render(self, shader_programm):
        # Renderizar a base da casa
        glBindVertexArray(self.base_vao)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        # --------------------------------------------------------------
        # Renderizar o telhado da casa
        glBindVertexArray(self.roof_vao)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        # --------------------------------------------------------------
        # Renderizar a porta e a janela da casa
        glBindVertexArray(self.door_vao)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        # --------------------------------------------------------------
        # Renderizar a janela da casa
        glBindVertexArray(self.window)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        return shader_programm
