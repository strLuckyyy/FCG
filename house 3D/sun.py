
from OpenGL.GL import *
from object import Object

class Sun(Object):
    def __init__(self):
        super().__init__()
        self.sun_vao = None
        
    def draw(self):
        self.sun_vao = self.cubeInit(
            size=[0.3, 0.3, 0.3],
            face_colors=[
                self.rgbToFloat(255, 223, 0),
                self.rgbToFloat(255, 223, 0),
                self.rgbToFloat(255, 223, 0),  
                self.rgbToFloat(255, 223, 0), 
                self.rgbToFloat(255, 223, 0), 
                self.rgbToFloat(255, 223, 0)
            ]
        )
    
    def render(self, shader_programm):
        sun_count = self.vertex_count[self.sun_vao]
        
        transform = self.transformation(1.5, 2.0, -3.0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        
        glBindVertexArray(self.sun_vao)
        glDrawArrays(GL_TRIANGLES, 0, sun_count)
        glBindVertexArray(0)
        
        return shader_programm