
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#configuraciones iniciales
w= 400 # resolucion de ventana
h= 400 # resolucion de ventana

numberOfLines = 80 # cantidad de lineas para dibujar el ovalo

curvaturax = 0.5 # que tanto se curvan los bordes del cuadrado
curvaturay = 0.5 # que tanto se curvan los bordes del cuadrado

tamanoLado1 = 200 # tamano del lado 1 del cuadrado (con curvatura 0)
tamanoLado2 = 200 # tamano del lado 2 del cuadrado (con curvatura 0)

#Configuracion de ventana
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
#creacion de la ventana con glut
wind = glutCreateWindow(b'OpenGL Coding Practice')

# esta parte no entiendo tristin :'v
glViewport(0, 0, w, h)
glMatrixMode(GL_PROJECTION)
glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
glMatrixMode (GL_MODELVIEW)

#color para las lineas
glColor3f(1.0, 0.0, 3.0)

def cuadrado(x,y,l1,l2,px,py):

        #if p != 0: #si la curvatura no es 1

        #dibujar lado 1
        glBegin(GL_LINES)
        glVertex2f(x-l2/2, y-l1/2)
        glVertex2f(x-l2/2, y+l1/2)
        glEnd()
        glutSwapBuffers()

        #dibujar lado 2
        glBegin(GL_LINES)
        glVertex2f(x-l2/2, y+l1/2)
        glVertex2f(x+l2/2, y+l1/2)
        glEnd()
        glutSwapBuffers()

        #dibujar lado 3
        glBegin(GL_LINES)
        glVertex2f(x+l2/2, y+l1/2)
        glVertex2f(x+l2/2, y-l1/2)
        glEnd()
        glutSwapBuffers()

        #dibujar lado 4
        glBegin(GL_LINES)
        glVertex2f(x+l2/2, y-l1/2)
        glVertex2f(x-l2/2, y-l1/2)
        glEnd()
        glutSwapBuffers()

       # if p != 1: # si la curvatura no es 0
           #p2 = p
           #if p == 0 : # si la cuvatura es 1
           #    p2 = 1

    # radio para los ovalos
        
        radio1 = l2/2*(1-px)
        radio2 = l1/2*(1-py)

    # redondeando primer esquina (lados 1 y 2)

    #   xOvalo1 = x-l2/2*p
    #   yOvalo1 = y+l1/2*p
    #   ovalo(xOvalo1,yOvalo1,radio1,radio2,2)

    # redondeando segunda esquina (lados 2 y 3)

        xOvalo2 = x+l2/2*px
        yOvalo2 = y+l1/2*py

        octante7 = ovalo(xOvalo2,yOvalo2,radio1,radio2,7)
        ovalo(xOvalo2,yOvalo2,radio1,radio2,8)
        ovalo(xOvalo2,yOvalo2,radio1,radio2,1)
        ovalo(xOvalo2,yOvalo2,radio1,radio2,2)
        ovalo(xOvalo2,yOvalo2,radio1,radio2,3)
        octante4 = ovalo(xOvalo2,yOvalo2,radio1,radio2,4)


    # redondeando segunda esquina (lados 3 y 4)

    #   xOvalo3 = x+l2/2*p
    #   yOvalo3 = y-l1/2*p
    #   ovalo(xOvalo3,yOvalo3,radio1,radio2,4)

    # redondeando segunda esquina (lados 4 y 1)

        xOvalo4 = x-l2/2*px
        yOvalo4 = y-l1/2*py

        octante3 = ovalo(xOvalo4,yOvalo4,radio1,radio2,3)
        ovalo(xOvalo4,yOvalo4,radio1,radio2,4)
        ovalo(xOvalo4,yOvalo4,radio1,radio2,5)
        ovalo(xOvalo4,yOvalo4,radio1,radio2,6)
        ovalo(xOvalo4,yOvalo4,radio1,radio2,7)
        octante8    = ovalo(xOvalo4,yOvalo4,radio1,radio2,8)

        glBegin(GL_LINES)
        glVertex2f(octante7[0][0], octante7[0][1])
        glVertex2f(octante3[0][0], octante3[0][1])
        glEnd()
        glutSwapBuffers()

        glBegin(GL_LINES)
        glVertex2f(octante8[1][0], octante8[1][1])
        glVertex2f(octante4[1][0], octante4[1][1])
        glEnd()
        glutSwapBuffers()

def ovalo(x,y,r1,r2,octante=0):

    puntos = []

    if octante == 0:

        inicio = 0
        fin = numberOfLines

    else :

        inicio = int(numberOfLines*(octante-1)/8)
        fin = int(numberOfLines*(octante)/8)

    for i in range(inicio,fin):

        angle1 = i * ( 2*math.pi/numberOfLines)
        angle2 = ( i +1 ) * (2*math.pi/numberOfLines )
        x1 = x + r1 * math.cos(angle1)
        y1 = y + r2 * math.sin(angle1)
        x2 = x + r1 * math.cos(angle2)
        y2 = y + r2 * math.sin(angle2)
        
        if i == inicio:
            puntos.append((x1,y1))
        if i == fin-1:
            puntos.append((x2,y2))


        #dibujar recta
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()
        glutSwapBuffers()

    return puntos


def keyboard(key, x, y):
    global curvaturax 
    global curvaturay

    if key == b'd':
        curvaturax = curvaturax + 0.1
        if curvaturax > 1 :
            curvaturax = 1
    if key == b'a':
        curvaturax = curvaturax - 0.1
        if curvaturax < 0 :
            curvaturax = 0

    if key == b'w':
        curvaturay = curvaturay + 0.1
        if curvaturay > 1 :
            curvaturay = 1
    if key == b's':
        curvaturay = curvaturay - 0.1
        if curvaturay < 0 :
            curvaturay = 0
    clear()
    cuadrado(w/2,h/2,tamanoLado1,tamanoLado2,(1-curvaturax),(1-curvaturay))


def special(key, x, y):
    global tamanoLado1
    global tamanoLado2
    if key == GLUT_KEY_UP:
        tamanoLado1 = tamanoLado1 + 10 
    if key == GLUT_KEY_DOWN:
        tamanoLado1 = tamanoLado1 - 10 
        if tamanoLado1 < 0 :
            tamanoLado1 = 0
    if key == GLUT_KEY_RIGHT:
        tamanoLado2 = tamanoLado2 + 10 
    if key == GLUT_KEY_LEFT:
        tamanoLado2 = tamanoLado2 - 10 
        if tamanoLado2 < 0 :
            tamanoLado2 = 0

    clear()
    cuadrado(w/2,h/2,tamanoLado1,tamanoLado2,(1-curvaturax),(1-curvaturay))

def clear():
    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def dibujar():
    cuadrado(w/2,h/2,tamanoLado1,tamanoLado2,(1-curvaturax),(1-curvaturay))

glutSpecialFunc(special)
glutKeyboardFunc(keyboard)
glutDisplayFunc(dibujar)


glutMainLoop()