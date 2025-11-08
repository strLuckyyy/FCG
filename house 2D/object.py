from functools import singledispatchmethod
from OpenGL.GL import *
import numpy as np

class Object():
    # --------------------------------------------------------------
    # Métodos de cores
    
    def rgbToFloat(self, r, g, b):
        return [float(r) / 255.0, float(g) / 255.0, float(b) / 255.0] 

    def objColor(self, tri_amount, r, g, b):
        colors = [float(r), float(g), float(b),
                  float(r), float(g), float(b),
                  float(r), float(g), float(b)]
        
        if tri_amount > 1:
            colors *= int(tri_amount)
            
        return np.array(colors, dtype=np.float32) 
    
    # --------------------------------------------------------------
    # Métodos de inicialização das geometrias
    
    def squareInitialize(
        self, location = [-.5,-.5], size = [1,1], color = [1, 0, 0]
        ):
        
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)

        # position x e y 
        pos_x, pos_y = location[0], location[1]
        #position somada com o tamanho
        psum_x, psum_y = pos_x + size[0], pos_y + size[1]
        
        house_points = [ 
            # triângulo 1 
            psum_x, psum_y, 0.0, #vertice superior direito
            psum_x, pos_y, 0.0, #vertice inferior direito 
            pos_x, pos_y, 0.0, #vertice inferior esquerdo 
            # triângulo 2 
            pos_x, psum_y, 0.0, #vertice superior esquerdo
            psum_x, psum_y, 0.0, #vertice superior direito
            pos_x, pos_y, 0.0 #vertice inferior esquerdo
        ]      
                
        house_points = np.array(house_points, dtype=np.float32)
        
        pvbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, pvbo)
        glBufferData(GL_ARRAY_BUFFER, house_points, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        
        # Cores da casa (marrom claro)
        house_colors = self.objColor(2, r=color[0], g=color[1], b=color[2])
        
        cvbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, cvbo)
        glBufferData(GL_ARRAY_BUFFER, house_colors, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        
        glBindVertexArray(0)
        return vao
    
    
    def triagleInitialize(
        self, equilateral = False, location = [-.5,-.5], size = [1,1], color = [1, 0, 0]
        ):
        
        vao = glGenVertexArrays(1)
        glBindVertexArray(vao)
        
        h_x = size[0]/2 + location[0] if equilateral else location[0]

        # position x e y 
        pos_x, pos_y = location[0], location[1]
        #position somada com o tamanho
        psum_x, psum_y = pos_x + size[0], pos_y + size[1]

        roof_points = [
            h_x, psum_y, 0.0,  # cima
            pos_x, pos_y, 0.0,  # direita
            psum_x, pos_y, 0.0  # esquerda
        ]
        
        roof_points = np.array(roof_points, dtype=np.float32)
        
        pvbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, pvbo)
        glBufferData(GL_ARRAY_BUFFER, roof_points, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        
        # Cores do telhado (vermelho)
        roof_colors = self.objColor(1, r=color[0], g=color[1], b=color[2])
        
        cvbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, cvbo)
        glBufferData(GL_ARRAY_BUFFER, roof_colors, GL_STATIC_DRAW)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        
        glBindVertexArray(0)
        return vao
    
    # --------------------------------------------------------------
    # Matrizes de transformação    
    def translateDefault(self):
        return [0.0, 0.0, 0.0]
    
    def rotateDefault(self):
        return [0.0, 0.0, 0.0]
    
    def scaleDefault(self):
        return [1.0, 1.0, 1.0]
    
    def translate(self, x, y, z):
        return np.array([
            [1.0, 0.0, 0.0, x],
            [0.0, 1.0, 0.0, y],
            [0.0, 0.0, 1.0, z],
            [0.0, 0.0, 0.0, 1.0]], np.float32
        )
    
    def rotateX(self, angle):
        angle = np.radians(angle)
        cos = np.cos(angle)
        sen = np.sin(angle)
        
        return np.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, cos, -sen, 0.0],
            [0.0, sen, cos, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])
        
    def rotateY(self, angle):
        angle = np.radians(angle)
        cos = np.cos(angle)
        sen = np.sin(angle)
        
        return np.array([
            [cos, 0.0, sen, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [-sen, 0.0, cos, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])
        
    def rotateZ(self, angle):
        angle = np.radians(angle)
        cos = np.cos(angle)
        sen = np.sin(angle)
        
        return np.array([
            [cos, -sen, 0.0, 0.0],
            [sen, cos, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])
    
    def scale(self, x, y, z):
        return np.array([
            [x, 0.0, 0.0, 0.0],
            [0.0, y, 0.0, 0.0],
            [0.0, 0.0, z, 0.0],
            [0.0, 0.0, 0.0, 1.0]], np.float32
        )
    
    def transformation(self, translate=None, rotate=None, scale=None):
        # matriz de translação
        if translate is None:
            translate = self.translateDefault()
            
        translate = self.translate(
            translate[0], translate[1], translate[2]
        )
        
        # combinação das rotações
        if rotate is None:
            rotate = self.rotateDefault()
        
        rotation = self.rotateX(
            rotate[0]).dot(self.rotateY(rotate[1]).dot(self.rotateZ(rotate[2]))
        )
        
        # matriz de escala
        if scale is None:
            scale = self.scaleDefault()
            
        scale = self.scale(
            scale[0], scale[1], scale[2]
        )
        
        # combinando as transformacoes, multiplicando as matrizes
        transform = scale @ rotation @ translate
        
        return transform
    
    # --------------------------------------------------------------
    # Métodos abstratos para desenhar e renderizar objetos
    
    def draw(self):
        pass
    
    def render(self, shader_programm) -> int:
        return shader_programm