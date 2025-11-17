from OpenGL.GL import *
from object import Object

class Tree(Object):
    def __init__(self):
        super().__init__()
        self.trunk_vao = None
        self.leaves_vao = None
        
    def draw(self):
        # Draw the trunk (cube)
        self.trunk_vao = self.cubeInit(
            size=[0.1, 0.5, 0.1],
            face_colors=[
                self.rgbToFloat(139, 69, 19),  # Frente
                self.rgbToFloat(139, 69, 19),  # Trás
                self.rgbToFloat(139, 69, 19),  # Esquerda
                self.rgbToFloat(139, 69, 19),  # Direita
                self.rgbToFloat(160, 82, 45),  # Topo
                self.rgbToFloat(160, 82, 45)   # Fundo
            ]
        )
        
        # Draw the leaves (cube)
        self.leaves_vao = self.cubeInit(
            size=[0.4, 0.4, 0.4],
            face_colors=[
                self.rgbToFloat(34, 139, 34),  # Frente
                self.rgbToFloat(34, 139, 34),  # Trás
                self.rgbToFloat(34, 139, 34),  # Esquerda
                self.rgbToFloat(34, 139, 34),  # Direita
                self.rgbToFloat(0, 100, 0),    # Topo
                self.rgbToFloat(0, 100, 0)     # Fundo
            ]
        )
    
    def render(self, shader_programm):
        # Counts
        trunk_count = self.vertex_count[self.trunk_vao]
        leaves_count = self.vertex_count[self.leaves_vao]
        
        # Rendering the trunk
        glBindVertexArray(self.trunk_vao)
        
        transform = self.transformation(1.0, 0.25-.3, -1.0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, trunk_count)
        glBindVertexArray(0)
        
        # Rendering the leaves
        glBindVertexArray(self.leaves_vao)
        
        transform = self.transformation(1.0, 0.65-.3, -1.0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glDrawArrays(GL_TRIANGLES, 0, leaves_count)
        glBindVertexArray(0)
        
        return shader_programm
        