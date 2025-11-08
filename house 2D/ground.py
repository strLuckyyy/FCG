from OpenGL.GL import *
from object import Object
import numpy as np

class Ground(Object):
    def __init__(self):
        self.ground_vao = None
    
    def draw(self):
        # Desenhar o chão (quadrado)
        self.ground_vao = self.squareInitialize(
            location=[-1.0, -1.0], size=[2.0, 0.3], color=self.rgbToFloat(34, 139, 34)
        )  # Verde para o chão
        
    def render(self, shader_programm):
        # Renderizar o chão
        glBindVertexArray(self.ground_vao)
        
        transform = self.transformation()
        
        transformLoc = glGetUniformLocation(shader_programm, "matriz")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, 6)
        
        return shader_programm