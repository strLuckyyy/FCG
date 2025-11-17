from object import Object
from window import Window as win
import numpy as np
from OpenGL.GL import *

class House(Object):
    def __init__(self):
        super().__init__()
        self.house_base_vao = None
        self.roof_vao = None
        self.door_vao = None
        
    def draw(self):
        # Draw the house base (cube)
        self.house_base_vao = self.cubeInit(
            size=[0.5, 0.5, 0.5],
            face_colors=[
                self.rgbToFloat(210, 180, 140),
                self.rgbToFloat(210, 180, 140), 
                self.rgbToFloat(210, 180, 140), 
                self.rgbToFloat(210, 180, 140), 
                self.rgbToFloat(222, 184, 135),
                self.rgbToFloat(139, 69, 19) 
            ]
        )
        
        # Draw the roof (pyramid)
        self.roof_vao = self.pyramidInit(
            base=0.6,
            height=0.4,
            face_colors=[
                self.rgbToFloat(178, 34, 34), 
                self.rgbToFloat(178, 34, 34), 
                self.rgbToFloat(139, 0, 0),
                self.rgbToFloat(139, 0, 0)  
            ]
        )
        
        # Draw the door (cube)
        self.door_vao = self.cubeInit(
            size=[0.2, 0.35, 0.02],
            face_colors=[
                self.rgbToFloat(160, 82, 45), 
                self.rgbToFloat(160, 82, 45), 
                self.rgbToFloat(160, 82, 45), 
                self.rgbToFloat(160, 82, 45),   
                self.rgbToFloat(139, 69, 19),  
                self.rgbToFloat(139, 69, 19)   
            ]
        )
    
    def render(self, shader_programm):
        # Counts
        base_count = self.vertex_count[self.house_base_vao]
        roof_count = self.vertex_count[self.roof_vao]
        door_count = self.vertex_count[self.door_vao]
        
        # Rendering the house base
        glBindVertexArray(self.house_base_vao)
        
        transform = self.transformation(0, 0.25-.3, 0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
         
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        glDrawArrays(GL_TRIANGLES, 0, base_count)
        
        # Rendering the roof
        glBindVertexArray(self.roof_vao)
        
        transform = self.transformation(0, 0.5-0.3, 0, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        glDrawArrays(GL_TRIANGLES, 0, roof_count)
        
        # Rendering the door
        glBindVertexArray(self.door_vao)
        
        transform = self.transformation(0, 0.18-0.3, 0.251, 0, 0, 0, 1, 1, 1)
        transformLoc = glGetUniformLocation(shader_programm, "transform")
        
        glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transform)
        glDrawArrays(GL_TRIANGLES, 0, door_count)
        
        # ----------------- #  
        
        return shader_programm
