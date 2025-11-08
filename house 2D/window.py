
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np


class Window():
    def __init__(self, width = 1080, height = 800) -> None:
        self.Window = None
        self.shader_programm = None
        self.WIDTH = width
        self.HEIGHT = height
        
    def redimensionCallback(self, window, w, h):
        self.WIDTH = w
        self.HEIGHT = h
        
    def initializeOpenGL(self):
        #Inicializa GLFW
        glfw.init()

        #Criação de uma janela
        self.Window = glfw.create_window(self.WIDTH, self.HEIGHT, "Cena 2D - Casa e Árvore", None, None)
        if not self.Window:
            glfw.terminate()
            exit()

        glfw.set_window_size_callback(self.Window, self.redimensionCallback)
        glfw.make_context_current(self.Window)
        
    def initializeShaders(self):
        # Especificação do Vertex Shader:
        vertex_shader = """
            #version 400
            layout(location = 0) in vec3 vertex_posicao;
            layout(location = 1) in vec3 vertex_cores;

            uniform mat4 matriz;

            out vec3 cores;

            void main() {
                cores = vertex_cores;
                gl_Position = matriz * vec4(vertex_posicao, 1.0);
            }
        """
        vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
        if not glGetShaderiv(vs, GL_COMPILE_STATUS):
            infoLog = glGetShaderInfoLog(vs, 512, None)
            print("Erro no vertex shader:\n", infoLog)

        # Especificação do Fragment Shader:
        fragment_shader = """
            #version 400
            in vec3 cores;
            out vec4 frag_colour;
            void main () {
                frag_colour = vec4 (cores, 1.0);
            }
        """
        fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
        if not glGetShaderiv(fs, GL_COMPILE_STATUS):
            infoLog = glGetShaderInfoLog(fs, 512, None)
            print("Erro no fragment shader:\n", infoLog)

        # Especificação do Shader Programm:
        self.shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
        if not glGetProgramiv(self.shader_programm, GL_LINK_STATUS):
            infoLog = glGetProgramInfoLog(self.shader_programm, 512, None)
            print("Erro na linkagem do shader:\n", infoLog)

        glDeleteShader(vs)
        glDeleteShader(fs)
        
    def initializeRender(self, objects):
        while not glfw.window_should_close(self.Window):            
            glClear(GL_COLOR_BUFFER_BIT)
            glClearColor(0.5, 0.7, 1.0, 1.0)  # Cor de fundo (céu azul claro)
            glViewport(0, 0, self.WIDTH, self.HEIGHT)
            
            glUseProgram(self.shader_programm)

            for obj in objects:
                self.shader_programm = obj.render(self.shader_programm)
            
            glfw.poll_events()
            glfw.swap_buffers(self.Window)
            
            if (glfw.PRESS == glfw.get_key(self.Window, glfw.KEY_ESCAPE)): #trata os eventos de mouse e teclado
                glfw.set_window_should_close(self.Window, True)

        glfw.terminate()