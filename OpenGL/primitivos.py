from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

altura, ancho = 800, 800

ojox, ojoy, ojoz = 0.8, 0.8, 2

def ejes():
    # Eje x
    largo = 2
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(largo, 0, 0)
    glEnd()

    # Eje y
    glColor3f(0, 1, 0)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, largo, 0)
    glEnd()

    # Eje z
    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, largo)
    glEnd()

def cuadrado(color):
    glColor4f(color[0], color[1], color[2], 1)
    
    vertices = []
    ancho = 0.3

    vertices.append((0, 0, 0))
    vertices.append((ancho, 0, 0))
    vertices.append((ancho, ancho, 0))
    vertices.append((0, ancho, 0))

    glBegin(GL_QUADS)
    for v in vertices:
        glVertex3fv(v)
    glEnd()

def display():
    global ojox, ojoy, ojoz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Set the projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(35, altura / ancho, 0.1, 10.0)
    
    # Set the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    ojox += 0.2
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)
    
    cuadrado((0.8, 0.2, 0.5))
    
    ejes()

    glutSwapBuffers()

def buttons(key, x, y):
    global ojox
    print(f'key={key}')
    if key == b'a':
        ojox += 0.1
        print('hola')
        glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(altura, ancho)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Cubo pintado desde uno solo')
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

main()

