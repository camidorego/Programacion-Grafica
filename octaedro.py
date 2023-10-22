from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

width, height=800,800

ojox, ojoy, ojoz=3,2,2

def ejes():
    largo=2

    glBegin(GL_LINES)

    # eje x
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(largo,0,0)

    # eje y
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,largo,0)

    # eje z
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,largo)

    glEnd()

def dibujar_cara(vertices, color):
    glColor(color[0],color[1],color[2])
    glBegin(GL_TRIANGLES)
    for v in vertices:
        glVertex3f(*v)
    glEnd()

def octaedro():
    largo=0.5
    vertices=[(0,0,0),(largo,0,0),(largo/2,largo,0)]

    # cara trasera 1 -> gris
    glPushMatrix()
    glRotate(30,1,0,0)
    dibujar_cara(vertices,[0.4,0.4,0.4])
    glPopMatrix()

    # cara trasera 2 -> gris
    glPushMatrix()
    glRotate(180,1,0,0)
    glRotate(-30,1,0,0)
    dibujar_cara(vertices,[0.2,0.4,0.4])
    glPopMatrix()

    # cara izquierda 1 -> verde
    glPushMatrix()
    glRotate(-90,0,1,0)
    glRotate(-30,1,0,0)
    dibujar_cara(vertices, (0.2,0.8,0.2))
    glPopMatrix()

    # cara izquierda 2 -> verde
    glPushMatrix()
    glRotate(-90,0,1,0)
    glRotate(-150,1,0,0)
    dibujar_cara(vertices, (0.4,0.8,0.2))
    glPopMatrix()

    # cara derecha 1 -> rosado
    glPushMatrix()
    glTranslate(largo,0,0)
    glRotate(-90,0,1,0)
    glRotate(30,1,0,0)
    dibujar_cara(vertices, (0.8,0.2,0.2))
    glPopMatrix()

    # cara derecha 2 -> rosado
    glPushMatrix()
    glTranslate(largo,0,0)
    glRotate(-90,0,1,0)
    glRotate(150,1,0,0)
    dibujar_cara(vertices, (0.8,0.2,0.4))
    glPopMatrix()

    # cara delantera 1
    glPushMatrix()
    glTranslate(0,0,largo)
    glRotate(-30,1,0,0)
    dibujar_cara(vertices,(0.2,0.2,0.8))
    glPopMatrix()

    # cara delantera 2
    glPushMatrix()
    glTranslate(0,0,largo)
    glRotate(-150,1,0,0)
    dibujar_cara(vertices,(0.2,0.4,0.8))
    glPopMatrix()

    glFlush()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45,(width/height),0.1,50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox,ojoy,ojoz,0,0,0,0.0,1.0,0.0)

    ejes()
    octaedro()

    glutSwapBuffers()

def buttons(key, x, y):
    global ojox,ojoz
    print(f'key={key}')
    if key == b'a':
        ojox += 0.1
    if key==b'd':
        ojox-=0.1
    if key==b'w':
        ojoz+=0.1
    if key==b'x':
        ojoz-=0.1
    glutPostRedisplay()
    
    

def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutCreateWindow(b'Octaedro')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__=='__main__':
    main()

    