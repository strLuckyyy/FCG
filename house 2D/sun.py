from OpenGL.GL import *
from object import Object
import numpy as np

class Sun(Object):
    def __init__(self):
        self.sun_vao = None
    
    def draw(self):
        # Desenhar o sol (quadrado)
        self.sun_vao = self.squareInitialize(
            location=[0.7, 0.7], size=[0.2, 0.25], color=self.rgbToFloat(255, 223, 0)
        )  # Amarelo para o sol
        
    def render(self, shader_programm):
        # Renderizar o sol
        glBindVertexArray(self.sun_vao)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        return shader_programm
