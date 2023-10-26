from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

vertice_recta=[]

def semi_circulo(center_x, center_y, radiusx, radiusy, cant_lineas, angulo_deg):
    angulo = math.radians(angulo_deg)
    glBegin(GL_LINES)
    for i in range(math.floor(cant_lineas / 2)):
        glColor3f(0.6, 0, 0.4)
        alpha = (2.0 * math.pi * i) / cant_lineas
        x1 = center_x + radiusx * math.cos(alpha)
        y1 = center_y + radiusy * math.sin(alpha)

        # se rota
        x1_rotated = center_x + (x1 - center_x) * math.cos(angulo) - (y1 - center_y) * math.sin(angulo)
        y1_rotated = center_y + (x1 - center_x) * math.sin(angulo) + (y1 - center_y) * math.cos(angulo)
        
        alpha = (2.0 * math.pi * (i + 1)) / cant_lineas
        x2 = center_x + radiusx * math.cos(alpha)
        y2 = center_y + radiusy * math.sin(alpha)

        # se rota
        x2_rotated = center_x + (x2 - center_x) * math.cos(angulo) - (y2 - center_y) * math.sin(angulo)
        y2_rotated = center_y + (x2 - center_x) * math.sin(angulo) + (y2 - center_y) * math.cos(angulo)

        # se guardan vertices de las rectas
        if i == 0:
            vertice_recta.append(x1_rotated)
            vertice_recta.append(y1_rotated)
        elif i == (math.floor(cant_lineas / 2) - 1):
            vertice_recta.append(x1_rotated)
            vertice_recta.append(y1_rotated)

        glVertex2f(x1_rotated, y1_rotated)
        glVertex2f(x2_rotated, y2_rotated)

    glEnd()



def hoja():
    # circulo 1
    semi_circulo(-100, 80, 80, 30, 100, 75)

    # circulo 2
    semi_circulo(-100, 80, 80, 30, 100, -105)

    glBegin(GL_LINES)
    glVertex2f(vertice_recta[0],vertice_recta[1])
    glVertex2f(vertice_recta[2],vertice_recta[3])
    glEnd()

    # se unen los semi circulos
    # glBegin(GL_LINES)
    # glVertex2f(vertice_recta[0],vertice_recta[1])
    # glVertex2f(vertice_recta[4],vertice_recta[5])
    # glVertex2f(vertice_recta[2],vertice_recta[3])
    # glVertex(vertice_recta[6],vertice_recta[7])

    # glEnd()

def rama():
    # rama
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    glVertex2f(-150,0)
    glVertex2f(200,0)
    glEnd()

    # hojas
    hoja()
    glPushMatrix()
    glTranslate(100,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glTranslate(200,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glTranslate(300,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glRotate(180,1,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glTranslate(100,0,0)
    glRotate(180,1,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glTranslate(200,0,0)
    glRotate(180,1,0,0)
    hoja()
    glPopMatrix()

    glPushMatrix()
    glTranslate(300,0,0)
    glRotate(180,1,0,0)
    hoja()
    glPopMatrix()

def rama_con_hojas(angulo):
    glPushMatrix()
    glRotate(angulo,1,0,0)
    rama()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # se configura la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)  # se ajusta la escala de la ventana

    # se selecciona e inicializa la matriz de visualización
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    rama()
    #hoja()  
    #semi_circulo(-1, 1.3, 0.5, 0.5, 100, 45)
    #semi_circulo(1, -1, 0.5, 0.5, 100, -135) 
    #rama_con_hojas()


    glutSwapBuffers()

def main():
    # se inicializa glut
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # buffer doble y esquema de colores

    # configuraciones de la ventana
    glutInitWindowSize(800, 800)
    glutCreateWindow(b'Rama con Hojas-Camila')

    glutDisplayFunc(display)  # se especifica la función display
    glutMainLoop()  # se inicia el loop

if __name__ == '__main__':
    main()
