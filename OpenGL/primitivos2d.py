from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width,height=800,800

def poligono():
    glBegin(GL_POLYGON)
    glColor3f(0.4,0.2,0.5)
    glVertex2f(0,0)
    glVertex2f(0,-200)
    glVertex2f(200,-200)
    glVertex2f(100,-100)
    glVertex2f(200,0)

    glEnd()

def triangulo():
    glBegin(GL_TRIANGLES)
    glColor(0.3,1,0)
    glVertex2f(0,0)
    glVertex2f(-200,0)
    glVertex2f(-100,200)
    glEnd()


def cuadrado():
    glBegin(GL_QUADS)
    glColor3f(1,0.3,0)
    glVertex2f(0,0)
    glVertex2f(200,0)
    glVertex2f(200,200)
    glVertex2f(0,200)
    glEnd()

def linea():
    glBegin(GL_LINES)
    glColor(0,0,1)
    glVertex2f(0,0)
    glVertex2f(-200,-200)
    glEnd()

def ejes():
    largo=400

    glBegin(GL_LINES)

    #eje x
    glColor3f(1,0,0)
    glVertex2f(-largo,0)
    glVertex2f(largo,0)

    #eje y
    glColor3f(0,1,0)
    glVertex2f(0,-largo)
    glVertex2f(0,largo)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluOrtho2D(-400,400,-300,300)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ejes()
    cuadrado()
    triangulo()
    linea()
    poligono()
    

    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'Primitivos')
    glutDisplayFunc(display)
    glutMainLoop()

if __name__=='__main__':
    main()
