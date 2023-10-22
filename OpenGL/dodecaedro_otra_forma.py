from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

width, height=800,800

ojox, ojoy, ojoz=3,1,4

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

def flor(largo):
    radio = (largo / (2 * math.sin(math.radians(72/2))))
    ap = largo/(2*math.tan(math.radians(72/2))) # apotema
    h = largo*math.sin(math.radians(72)) # distancia entre base y vertice de los costados
    a = largo*math.cos(math.radians(72)) # distancia horizontal entre el vertice superior y la punta del veritce de los costados

    vertices=[]
    
    vertices.append((0, 0, 0)) 
    vertices.append((largo, 0, 0))
    vertices.append((largo/2 + radio, h, 0))
    vertices.append((largo/2, ap + radio, 0))
    vertices.append((-(radio-largo/2), h, 0))

        ## FLOR 1 ##
    # pentagono central
    dibujar_cara(vertices, (1, 0, 0))
    # flor 2
    glPushMatrix()
    glTranslate(0,0,2*radio+ap)
    dibujar_cara(vertices, (1, 0.7, 0.3))
    glPopMatrix()
    
    
    # pentagono derecho inferior
    glPushMatrix()
    glTranslate(largo,0,0)
    glRotate(-36,0,0,1)
    dibujar_cara(vertices,(0,1,0))
    # flor 2
    glTranslate(0,0,(2*radio+ap))
    dibujar_cara(vertices,(0.8,1,0))
    glPopMatrix()

    #pentagono derecho superior
    glPushMatrix()
    #glTranslate(radio+largo/2,h,0)
    #glTranslate(radio+largo/2,h,0)
    #glRotate(36,0,0,1)
    glTranslate(largo/2, radio+ap,0)
    glRotate(324,0,0,1)
    dibujar_cara(vertices,(0,0,1))
    # flor 2
    glTranslate(0,0,2*radio+ap)
    dibujar_cara(vertices,(0,1,0.6))
    glPopMatrix()

    # pentagono inferior
    glPushMatrix()
    glRotate(180,1,0,0)
    dibujar_cara(vertices,(0.8,0.4,0))
    # flor 2
    glTranslate(0,0,-(2*radio+ap))
    dibujar_cara(vertices,(0.8,0.4,0.6))
    glPopMatrix()

    # pentagono derecho superior
    glPushMatrix()
    #glTranslate(-2*radio,-ap,0)
    #glRotate(36,0,0,1)
    glTranslate(-a,h,0)
    glRotate(36,0,0,1)
    dibujar_cara(vertices, (0.8,0.4,0.6))
    # flor 2
    glTranslate(0,0,2*radio+ap)
    dibujar_cara(vertices,(1,0.5,0.3))
    glPopMatrix()

    # pentagono derecho inferior
    glPushMatrix()
    glRotate(108,0,0,1)
    dibujar_cara(vertices, (0.4,0,0.6))
    # flor 2
    glTranslate(0,0,2*radio+ap)
    dibujar_cara(vertices,(0.4,0.2,0.8))
    glPopMatrix()

        ## FLOR 2 ##
    # pentagono central
    glPushMatrix()
    glTranslate(0,0,radio+ap)
    #dibujar_cara(vertices, (1, 0, 0.5))
    glPopMatrix()
    

    glFlush()

def dodecaedro(largo):
    radio = (largo / (2 * math.sin(math.radians(72/2))))
    ap = largo/(2*math.tan(math.radians(72/2))) # apotema
    h = largo*math.sin(math.radians(72)) # distancia entre base y vertice de los costados
    a = largo*math.cos(math.radians(72)) # distancia horizontal entre el vertice superior y la punta del veritce de los costados

    vertices=[]
    
    vertices.append((0, 0, 0)) 
    vertices.append((largo, 0, 0))
    vertices.append((largo/2 + radio, h, 0))
    vertices.append((largo/2, ap + radio, 0))
    vertices.append((-(radio-largo/2), h, 0))

    # pentagono central
    dibujar_cara(vertices, (1, 0, 0))
    # flor 2
    glPushMatrix()
    glTranslate(0,ap/2,2*radio+ap)
    glRotate(-36,0,0,1)
    
    dibujar_cara(vertices, (1, 0.7, 0.3))
    glPopMatrix()

    # pentagono derecho inferior
    glPushMatrix()
    glTranslate(largo,0,0)
    glRotate(-18,-1,0,0)
    glRotate(-30,0,0,1)
    glRotate(-70,0,1,0)
    dibujar_cara(vertices,(0,1,0))
    glPopMatrix()
    # flor 2
    glPushMatrix()
    #glRotate(180,1,0,0)
    glTranslate(largo,0,(2*radio+ap))
    glRotate(-36,1,0,0)
    glRotate(70,0,1,0)
    glRotate(-30,0,0,1)
    glRotate(18,1,0,0)
    #glRotate(36,0,1,0)
    #glTranslate(0,0,)
    #dibujar_cara(vertices,(0.8,1,0))
    glPopMatrix()

     # pentagono inferior
    glPushMatrix()
    #glRotate(180,1,0,0)
    glRotate(108,1,0,0)
    dibujar_cara(vertices,(0.8,0.4,0))
    glPopMatrix()
    # flor 2
    glPushMatrix()
    glRotate(180,1,0,0)
    glTranslate(0,-ap/2,-(2*radio+ap))
    glRotate(36,0,0,1)
    glRotate(72,1,0,0)
    dibujar_cara(vertices,(0.8,0.4,0.6))
    glPopMatrix()




    
    # pentagono derecho inferior
    glPushMatrix()
    #glTranslate(largo/2+radio,0,0)
    glRotate(18,1,-3,1)
    #glRotate(36,0,0,1)
    glRotate(-98,0,1,0)
    #dibujar_cara(vertices,(0,1,0))
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
    dodecaedro(0.3)
    #flor(0.3)

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
    glutCreateWindow(b'Dodecaedro')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    
    glutMainLoop()

if __name__=='__main__':
    main()
