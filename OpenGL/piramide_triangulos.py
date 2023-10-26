from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT import GLUT_KEY_RIGHT, GLUT_KEY_LEFT
import math

ojox, ojoy, ojoz = 4, 1, 2

width, height= 800,800

light_position = [1.0, 1.0, 2.0, 0.0]  # posicion inicial de la fuente de luz
look_at_center = [0.0, 0.0, 0.0]  # punto hacia el que apunta la luz

n=4 # cantidad de triangulos de la base

def ejes(largo):
    ## EJE X ##
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(largo,0,0)
    

    ## EJE Y ##
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,largo,0)

    ## EJE Z ##
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,largo)

    glEnd()

def triangulo(vertices, color):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for v in vertices:
        glVertex3f(*v)
    glEnd()


def piramide(cant_triangulos): # recibe como parametro la cantidad de triangulos de la base
    lado=0.25
    h=math.sqrt(lado**2-(lado/2)**2)

    vertices=[]
    vertices.append((0,0,0))
    vertices.append((lado,0,0))
    vertices.append((lado/2,h,0))

    color=(0.5,0,0.6)

    for i in range(cant_triangulos):
        # base
        for j in range(cant_triangulos-i):
            glPushMatrix()
            glTranslate(lado*(i),0,0)
            glTranslate((lado/2)*j,h*j,0)
            triangulo(vertices,color)
            glPopMatrix()



    # triangulo(vertices,color)

    # glPushMatrix()
    # glTranslate(0.25,0,0)
    # triangulo(vertices,color)
    # glPopMatrix()

    # glPushMatrix()
    # glTranslate(lado/2,h,0)
    # triangulo(vertices,color)
    # glPopMatrix()

    glFlush()


def display():
    global ojox, ojoy, ojoz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, (width / height), 0.1, 400)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    ejes(2)
    piramide(n)


    # glEnable(GL_LIGHTING)
    # glEnable(GL_LIGHT0)

    # glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, look_at_center)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,1,1))
    # glMaterialfv(GL_FRONT, GL_SPECULAR, (1,0,0.2))
    # glMaterialfv(GL_FRONT, GL_AMBIENT, (1,0,0))
    # glShadeModel(GL_SMOOTH)

    glutSwapBuffers()

def buttons(key, x, y):
    global ojox, ojoz, n  # Añade 'n' a la lista de variables globales
    print(key)
    print('key={key}')
    if key == b'a':
        ojox += 0.1
    if key == b'd':
        ojox -= 0.1
    if key == b'w':
        ojoz += 0.1
    if key == b'x':
        ojoz -= 0.1

    glutPostRedisplay()

def otros_botones(key,x,y):
    global n
    print(key)

    # con los botones de derecha e izquierda, aumenta o disminuye la cantidad de triangulos en la base
    if key == GLUT_KEY_RIGHT:
        n += 1
    if key == GLUT_KEY_LEFT:
        n -= 1

    glutPostRedisplay()


def main():
    # se inicializa glut
    glutInit(sys.argv)

    # se configura la visualizacion (buffer doble, modo rgb de colores,  Habilita el búfer de profundidad(z-buffer))
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(height, width)
    glutCreateWindow(b'Ventana 3D Vacia')

    glEnable(GL_DEPTH_TEST)
    
    glutDisplayFunc(display)
    glutSpecialFunc(otros_botones)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == '__main__':
    main()
