from OpenGL.GL import *
from object import Object


class Ground(Object):
    def __init__(self):
        super().__init__()
        self.ground_vao = None
        
    def draw(self):
        self.ground_vao = self.cubeInit(
            size=[5., 0.1, 5.],
            face_colors=[
                self.rgbToFloat(34, 139, 34),
                self.rgbToFloat(34, 139, 34),
                self.rgbToFloat(34, 139, 34), 
                self.rgbToFloat(34, 139, 34), 
                self.rgbToFloat(34, 139, 34), 
                self.rgbToFloat(34, 139, 34)  
            ]
        )
    
    def render(self, shader_programm):
        ground_count = self.vertex_count[self.ground_vao]
        
        transform = self.transformation(0.0, -0.3, 0.0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glBindVertexArray(self.ground_vao)
        glDrawArrays(GL_TRIANGLES, 0, ground_count)
        glBindVertexArray(0)
        
        return shader_programm