from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit
from OpenGL.GLUT import *


altura, ancho = 800, 800

ojox, ojoy, ojoz = 1, 1, 2


def cara(vertices, color):
    glColor(color[0], color[1], color[2], 1)
    glBegin(GL_POLYGON)
    for v in vertices:
        glVertex3fv(v)
    glEnd()


def display():
    global ojox, ojoy, ojoz
    #glEnable(GL_LIGHTING)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # Selecciona la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()  # Inicializar la matriz.

    # Ángulo, ratio, near, far
    gluPerspective(35, altura/ancho, 0.1, 10.0)

    # Seleccionar la matriz modelview
    glMatrixMode(GL_MODELVIEW)

    # Inicializar la matriz.
    glLoadIdentity()

    # Desde, Hacia, Dirección arriba
    ojox += 0.2
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)
    

    Piramide()


def ejes():
    # Eje x
    largo = 2
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(largo, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, largo, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, largo)

    glEnd()


def Piramide():
    vertices = []
    ancho = 0.3
    z = 0
    # Inferior izquierdo
    vertices.append((0, 0, z))
    # Inferior derecho
    vertices.append((ancho, 0, z))
    # Superior derecho
    vertices.append((ancho/2, ancho, z))
    

    ejes() # se dibujan los ejes

    # Cara trasera #gris
    glPushMatrix()
    glRotate(30,1,0,0)
    cara(vertices, (0.4, 0.4, 0.4))
    glPopMatrix()

    #Cara izquierda
    glPushMatrix()
    #glRotate(-40,1,0,0)
    glRotate(-30,0,0,1)
    glRotate(-90,0,1,0)
    cara(vertices,(0.8, 0.2, 0.5))
    glPopMatrix()

    #Cara derecha
    glPushMatrix()
    glTranslate(ancho,0,0)
    glRotate(30,0,0,1)
    #glRotate(20,0,0,1)
    glRotate(-90,0,1,0)
    cara(vertices,(0.2, 0.4, 0.8))
    glPopMatrix()

    #Cara Frontal
    glPushMatrix()
    glTranslate(0,0,ancho)
    glRotate(-30,1,0,0)
    #cara(vertices,(0.3, 0.1, 0.3))
    glPopMatrix()



    glFlush()


def buttons(key, x, y):
    global ojox
    print(f'key={key}')
    if key == b'a':
        ojox += 0.1

def main():
    glutInit(sys.argv)
    # glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(altura, ancho)
    # Borrar la pantalla
    

    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Piramide')
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

    # se configura la profundidad
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)


main()