##      Informatica 3       ##
##  Camila Do Rego Barros   ##
##        Parcial           ##
##         2023             ##

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

ojox, ojoy, ojoz = 1, 1, 2

width, height= 800,800

light_position = [1.0, 1.0, 2.0, 0.0]  # posicion inicial de la fuente de luz
look_at_center = [0.0, 0.0, 0.0]  # punto hacia el que apunta la luz

largo=0.25
cant_triangulos=4
movEnX=0
anguloy=0
angulo_en_hipotenusa=0

vertices_hipotenusa=[(0,largo,0),(largo,0,0)]

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

def dibujar_cara(vertices, color):
    glColor3f(*color)

    glBegin(GL_TRIANGLES)
    for v in vertices:
        glVertex3f(*v)
    glEnd()

def triangulo(color):
    #largo=0.25
    vertices=[]
    vertices.append((0,0,0))
    vertices.append((largo,0,0))
    vertices.append((0,largo,0))

    dibujar_cara(vertices,color)
    glFlush()

def vector_direccion():
    global vertices_hipotenusa
    x1, y1, z1 = vertices_hipotenusa[0]
    x2, y2, z2 = vertices_hipotenusa[1]
    
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    
    longitud = math.sqrt(dx**2 + dy**2 + dz**2)
    
   
    if longitud != 0:
        dx /= longitud
        dy /= longitud
        dz /= longitud
    
    return (dx, dy, dz)

def piramide():
    colores=[(0.5,0,0.5),(0,1,0),(0.3,0.2,1),(0.5,0.8,0.9),(0.2,0.7,0.6)]
    angulo=360/cant_triangulos

    for i in range(cant_triangulos):
        color=(random.random(),random.random(),random.random())
        glPushMatrix()
        glRotate(angulo*i,0,1,0)
        #triangulo(color)
        triangulo(colores[i%5])
        glPopMatrix()

    # glPushMatrix()
    # glRotate(90*0,0,1,0)
    # triangulo(largo)
    # glPopMatrix()

    # glPushMatrix()
    # glRotate(90*1,0,1,0)
    # triangulo(largo)
    # glPopMatrix()
    
    # glPushMatrix()
    # glRotate(90*2,0,1,0)
    # triangulo(largo)
    # glPopMatrix()

    # glPushMatrix()
    # glRotate(90*3,0,1,0)
    # triangulo(largo)
    # glPopMatrix()

def piramide_rotando():
    componentes = vector_direccion()
    alpha = math.degrees(math.atan2(componentes[1], componentes[0]))
    #perpendicular = (-componentes[0], componentes[1], componentes[2])

    glPushMatrix()
    #glRotate(angulox,1,0,0)
    glTranslate(movEnX,0,0)
    glRotate(anguloy,0,1,0)
    #glRotate(alpha*angulo_en_hipotenusa,0,0,1)
    glRotate(alpha * angulo_en_hipotenusa, *componentes)
    piramide()
    glPopMatrix()

    glFlush()




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
    #triangulo()
    piramide_rotando()

    glutSwapBuffers()
   
def buttons(key, x, y):
    global ojox,ojoz,cant_triangulos,movEnX,anguloy,angulo_en_hipotenusa
    print(f'key={key}')
    
    if key == b'x':
        movEnX+=0.25
    elif key == b'y':
        anguloy+=10
    elif key==b'r':
        angulo_en_hipotenusa+=1
    
    elif key == b'm':
        cant_triangulos += 1

    glutPostRedisplay()


def main():
    # se inicializa glut
    glutInit(sys.argv)

    # se configura la visualizacion (buffer doble, modo rgb de colores,  Habilita el búfer de profundidad(z-buffer))
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(height, width)
    glutCreateWindow(b'Camila Do Rego Barros - Parcial')

    glEnable(GL_DEPTH_TEST)
    
    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    glutMainLoop()

if __name__ == '__main__':
    main()
