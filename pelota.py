from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

altura, ancho = 800, 800

ojox, ojoy, ojoz = 0, 1, 2

def cara(vertices, color):
    glColor(color[0], color[1], color[2], 1)
    glBegin(GL_POLYGON)
    for v in vertices:
        glVertex3fv(v)
    glEnd()

def display():
    global ojox, ojoy, ojoz
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(35, altura/ancho, 0.1, 10.0)
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    ojox += 0.2
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)
    
    #glEnable(GL_LIGHTING)
    #glEnable(GL_LIGHT0)
    
    # Dibuja la pelota de fútbol
    #Pentagono(0.1)  # Cambié el valor Z a 1.0 para colocarlo en el eje Z
    Pelota()
    
    glutSwapBuffers()

def ejes():
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

def calcular_centro_pentagono(radius):
    # El centro estará en el punto medio del eje Z y la altura será 0
    center = (radius,math.cos(math.radians(72/2))*radius,0)
    return center

def Hexagono(radius):
    #center=[0,0,0]
    center = calcular_centro_pentagono(radius)
    vertices = []
    for i in range(6):
        angle = math.radians(i * 60)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        z = center[2]
        vertices.append((x, y, z))
    return vertices



def Pentagono(radius):
    center = calcular_centro_pentagono(radius)
    #center=[0,0,0]
    vertices = []
    for i in range(5):
        angle = math.radians(i * 72)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        z = center[2]
        vertices.append((x, y, z))
    
    return vertices
    
    # ejes()
    # glPushMatrix()
    # glRotate(17,0,0,1)
    # cara(vertices, (0.4, 0.2, 0.5))
    # glPopMatrix()

    # glPushMatrix()
    # glTranslate(radius*2-radius/3,0,0)
    # #glRotate(54,0,0,1)
    # glRotate(17-30,0,0,1)
    
    # cara(vertices,(0.2, 0.4, 0.8))
    # glPopMatrix()

def Pelota():
    ejes()
    glPushMatrix()
    #glRotate(17,0,0,1)
    cara(Pentagono(0.1), (0.4, 0.2, 0.5))
    glPopMatrix()

    glPushMatrix()
    #glRotate(10,0,0,1)
    glTranslate(0.1*2,0,0)
    
    
    
    
    #glRotate(,0,0,1)
    cara(Hexagono(0.1),(0.2, 0.4, 0.8))
    glPopMatrix()

    glPushMatrix()
    #glRotate(10,0,0,1)
    glTranslate(-0.1*2,0,0)
    #glRotate(,0,0,1)
    #cara(Hexagono(0.1),(0.2, 0.4, 0.8))
    glPopMatrix()

   





def buttons(key, x, y):
    global ojox
    print(f'key={key}')
    if key == b'a':
        ojox += 0.1

def main():
    glutInit(sys.argv)
    glutInitWindowSize(altura, ancho)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b'Soccer Ball')
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

if __name__ == "__main__":
    main()

