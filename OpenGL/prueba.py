from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
auto_camera_move_interval = 0.5

width, height = 800, 800

ojox, ojoy, ojoz = 1, 1, 2

def ejes():
    largo=2

    glBegin(GL_LINES)

    # ejes x -> rojo
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(largo,0,0)

    # eje y -> verde
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,largo,0)

    #eje z -> azul
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,largo)

    glEnd()

def triangulo(vertices,color):
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    for v in vertices:
        glVertex(*v)
    glEnd()

def recta_con_inclinacion(angulo):
    vertices=[(-0.5,0,0),(0.5,0,0),(0,0.5,0)]
    glPushMatrix()
    glRotatef(50, 0, 0, 1)
    triangulo(vertices,(1,0,0))
    glPopMatrix()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    recta_con_inclinacion(90)  # Llama a la función con el ángulo de inclinación deseado
    glutSwapBuffers()

# Inicialización de GLUT
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b'Recta con Inclinacion')

# Establece la función de dibujo
glutDisplayFunc(draw)

# Inicia el bucle de GLUT
glutMainLoop()