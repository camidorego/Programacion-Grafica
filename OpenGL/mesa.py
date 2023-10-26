from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

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

def dibujar_cara(vertices, color):
    glColor3f(*color)

    glBegin(GL_POLYGON)
    for v in vertices:
        glVertex3f(*v)
    glEnd()

def mesa(largo, angulo):
    vertices_mesa=[]

    vertices_mesa.append((0,0,0))
    vertices_mesa.append((largo/2,0,0))
    vertices_mesa.append((largo/2,largo,0))
    vertices_mesa.append((0,largo,0))

    # mesa cara 1
    glPushMatrix()
    glRotate(-angulo,1,0,0)
    dibujar_cara(vertices_mesa,(0.4,0,0.5))
    glPopMatrix()

    # mesa cara 2
    glPushMatrix()
    glRotate(-angulo,1,0,0)
    glTranslate(0,0,largo/10)
    dibujar_cara(vertices_mesa,(0.7,0,0.2))
    glPopMatrix()

    # costados de la mesa
    vertices_mesa_costado1=[]
    vertices_mesa_costado1.append((0,0,0))
    vertices_mesa_costado1.append((largo/10,0,0))
    vertices_mesa_costado1.append((largo/10,largo,0))
    vertices_mesa_costado1.append((0,largo,0))

    # costado izquierdo
    glPushMatrix()
    glRotate(-angulo,1,0,0)
    glRotate(-90,0,1,0)
    dibujar_cara(vertices_mesa_costado1,(0,0.4,1))
    glPopMatrix()

    # costado derecho
    glPushMatrix()
    glTranslate(largo/2,0,0)
    glRotate(-angulo,1,0,0)
    glRotate(-90,0,1,0)
    dibujar_cara(vertices_mesa_costado1,(0,1,0.4))
    glPopMatrix()

    vertices_mesa_costado2=[]
    vertices_mesa_costado2.append((0,0,0))
    vertices_mesa_costado2.append((largo/2,0,0))
    vertices_mesa_costado2.append((largo/2,largo/10,0))
    vertices_mesa_costado2.append((0,largo/10,0))

    # delantero
    glPushMatrix()
    glRotate(90-angulo,1,0,0)
    dibujar_cara(vertices_mesa_costado2,(0.9,0.2,0))
    glPopMatrix()

    # trasero
    glPushMatrix()
    glTranslate(0,largo*math.sin(math.radians(90-angulo)),-largo*math.cos(math.radians(90-angulo)))
    glRotate(90-angulo,1,0,0)
    dibujar_cara(vertices_mesa_costado2,(1,0,1))
    glPopMatrix()

    vertices_pata=[]
    vertices_pata.append((0,0,0))
    vertices_pata.append((largo/10,0,0))
    vertices_pata.append((largo/10,-largo/3,0))
    vertices_pata.append((0,-largo/3,0))

    # pata delantera izquierda
    glPushMatrix()
    glRotate(90-angulo,1,0,0)
    dibujar_cara(vertices_pata,(0,1,0))
    glPopMatrix()

    glPushMatrix()
    glTranslate(0,0,-largo/10)
    glRotate(90-angulo,1,0,0)
    dibujar_cara(vertices_pata,(0,0.5,0.5))
    glPopMatrix()

    glPushMatrix()
    glRotate(90-angulo,1,0,0)
    glRotate(90,0,1,0)
    dibujar_cara(vertices_pata,(0.4,0.4,0.8))
    glPopMatrix()

    glPushMatrix()
    glTranslate(largo/10*math.cos(math.radians(90-angulo)),(largo/10)*math.sin(math.radians(90-angulo)),0)
    glRotate(90-angulo,1,0,0)
    glRotate(90,0,1,0)
    dibujar_cara(vertices_pata,(0.4,0.4,0.8))
    glPopMatrix()

    glFlush()
    

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glClearColor(1.0, 1.0, 1.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    #gluPerspective(45,(width/height),0.1,50.0)
    gluPerspective(40., 1., 1., 40.)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(ojox,ojoy,ojoz,0,0,0,0.0,1.0,0.0)

    ejes()
    mesa(0.4,75)

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