from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ojox, ojoy, ojoz = 1, 1, 2

width, height= 800,800

light_position = [1.0, 1.0, 2.0, 0.0]  # posicion inicial de la fuente de luz
look_at_center = [0.0, 0.0, 0.0]  # punto hacia el que apunta la luz

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

def display():
    global ojox, ojoy, ojoz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, (width / height), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    ejes(2)


    # glEnable(GL_LIGHTING)
    # glEnable(GL_LIGHT0)

    # glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, look_at_center)
    # glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,1,1))
    # glMaterialfv(GL_FRONT, GL_SPECULAR, (1,0,0.2))
    # glMaterialfv(GL_FRONT, GL_AMBIENT, (1,0,0))
    # glShadeModel(GL_SMOOTH)

    glutSwapBuffers()
   


def main():
    # se inicializa glut
    glutInit(sys.argv)

    # se configura la visualizacion (buffer doble, modo rgb de colores,  Habilita el búfer de profundidad(z-buffer))
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(height, width)
    glutCreateWindow(b'Ventana 3D Vacia')

    glEnable(GL_DEPTH_TEST)
    
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == '__main__':
    main()
