from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width, height=800,800

ojox, ojoy, ojoz=1,1,4

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

def dibujar_cara(vertices, color):
    glColor3f(*color)

    glBegin(GL_POLYGON)
    for v in vertices:
        glVertex3f(*v)
    glEnd()

def calcular_centro(radio):
    return [radio,math.cos(math.radians(72/2))*radio,0]

def pentagono(radio, color):
    
    vertices=[]

    for i in range(5):
        angle=math.radians(i*72)
        x=radio*math.cos(angle)
        y=radio*math.sin(angle)
        z=0
        vertices.append((x,y,z))
    dibujar_cara(vertices,color)


def dodecaedro(radio):
    centro=[0,0,0] # es el centro del pentagono central

    # pentagono centrla
    #glPushMatrix()
    #glRotate(17,0,0,1)
    pentagono(radio, (0,0,1))
    #glPopMatrix()
    for i in range(1):
        angle = math.radians(i * 72)
        x = centro[0] + radio * math.cos(angle)
        y = centro[1] + radio * math.sin(angle)
        z = 0
        # glPushMatrix()
        # glTranslatef(x, y, z)
        # glRotatef(36*i, 0, 0, 1)  # Rotar 36 grados para cada nuevo pentágono
        # pentagono(radio, centro,(0,0.1+0.3*i,1))
        # glPopMatrix()
    

    # pentagono derecho superio
    glPushMatrix()
    glTranslate((radio*math.sin(math.radians(72)))*(1+1/2),(2*radio*math.cos(math.radians(72))*(1+1/2)),0)
    glRotate(36,0,0,1)
    pentagono(radio,(0,0.4+0.3,1))
    glPopMatrix() 

    # pentagono derecho inferior
    glPushMatrix()
    glTranslate((radio*math.cos(math.radians(72))+radio),-((radio)),0)
    glRotate(36,0,0,1)
    pentagono(radio,(1,0,0))
    glPopMatrix()

    # pentagono inferior
    glPushMatrix()
    glTranslate(-radio*1/2,-(radio)*(1+1/2),0)
    #glTranslate(-(centro[0]),-(centro[1]),0)
    glRotate(-36,0,0,1)
    pentagono(radio,(0,1,0))
    glPopMatrix()

    # pentagono izquierdo inferior
    glPushMatrix()
    glTranslate(-(radio*math.cos(math.radians(72/2))*(1+1/2)),0,0)
    glRotate(36,0,0,1)
    pentagono(radio,(1,0,0))
    glPopMatrix()

    # pentagono izquierdo inferior
    # glPushMatrix()
    # glTranslate(-(radio*0.7),-(radio*0.7),0)
    # glRotate(40,0,0,1)
    # #pentagono(radio,centro,(0.6,0.2,0.5))
    # glPopMatrix()

    # # pentagono izquierdo superior
    # glPushMatrix()
    # glTranslate(-(radio*0.1),radio+radio*0.1,0)
    # glRotate(36,0,0,1)
    # #pentagono(radio, centro,(0.4,0.7,0.4))
    # glPopMatrix() 

    
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45,(width/height),0.1,50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox,ojoy,ojoz,0,0,0,0.0,1.0,0.0)

    ejes()
    dodecaedro(0.3)

    glutSwapBuffers()

def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutCreateWindow(b'Dodecaedro')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    
    glutMainLoop()

if __name__=='__main__':
    main()
