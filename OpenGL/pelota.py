from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
auto_camera_move_interval = 0.5

width, height = 800, 800

ojox, ojoy, ojoz = 1, 1, 2

light_position = [1.0, 1.0, 2.0, 0.0]  # Posición inicial de la fuente de luz
look_at_center = [0.0, 0.0, 0.0]  # Punto hacia el que apunta la luz

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

def Pentagono(largo):
    radio_p = (largo / (2 * math.sin(math.radians(72/2))))
    ap_p = largo/(2*math.tan(math.radians(72/2))) # apotema
    d_p = largo*math.sin(math.radians(72)) # distancia entre base y vertice de los costados
    a_p = largo*math.cos(math.radians(72)) # distancia horizontal entre el vertice superior y la punta del veritce de los costados

    vertices_p=[]
    
    vertices_p.append((0, 0, 0)) 
    vertices_p.append((largo, 0, 0))
    vertices_p.append((largo/2 + radio_p, d_p, 0))
    vertices_p.append((largo/2, ap_p + radio_p, 0))
    vertices_p.append((-(radio_p-largo/2), d_p, 0))
    # pentagono central
    dibujar_cara(vertices_p, (1, 0, 0))
    glFlush()

def Hexagono(largo):
    radio_h = (largo / (2 * math.sin(math.radians(60/2))))
    ap_h = largo/(2*math.tan(math.radians(60/2))) # apotema
    d_h = largo*math.cos(math.radians(60)) # distancia horizontal entre el vertice superior y el vertice del costado
    vertices_h=[]

    vertices_h.append((0,0,0))
    vertices_h.append((largo,0,0))
    vertices_h.append((largo/2+radio_h, ap_h, 0))
    vertices_h.append((largo,2*ap_h,0))
    vertices_h.append((0,2*ap_h,0))      
    vertices_h.append((-(radio_h-largo/2),ap_h,0))

    dibujar_cara(vertices_h, (1,0,0))

def Pelota(largo):
    ## PENTAGONO ##
    radio_p = (largo / (2 * math.sin(math.radians(72/2))))
    ap_p = largo/(2*math.tan(math.radians(72/2))) # apotema
    d_p = largo*math.sin(math.radians(72)) # distancia entre base y vertice de los costados
    a_p = largo*math.cos(math.radians(72)) # distancia horizontal entre el vertice superior y la punta del veritce de los costados

    vertices_p=[]
    
    vertices_p.append((0, 0, 0)) 
    vertices_p.append((largo, 0, 0))
    vertices_p.append((largo/2 + radio_p, d_p, 0))
    vertices_p.append((largo/2, ap_p + radio_p, 0))
    vertices_p.append((-(radio_p-largo/2), d_p, 0))
    # pentagono central
    dibujar_cara(vertices_p, (0, 0, 1))

    ## HEXAGONO ##
    radio_h = (largo / (2 * math.sin(math.radians(60/2))))
    ap_h = largo/(2*math.tan(math.radians(60/2))) # apotema
    d_h = largo*math.cos(math.radians(60)) # distancia horizontal entre el vertice superior y el vertice del costado
    vertices_h=[]

    vertices_h.append((0,0,0))
    vertices_h.append((largo,0,0))
    vertices_h.append((largo/2+radio_h, ap_h, 0))
    vertices_h.append((largo,2*ap_h,0))
    vertices_h.append((0,2*ap_h,0))      
    vertices_h.append((-(radio_h-largo/2),ap_h,0))

    # hexagono inferior derecho
    glPushMatrix()
    glTranslate(radio_h,0,0)
    glRotate(40,0,1,0)
    glRotate(-45,0,0,1)
    
    dibujar_cara(vertices_h, (1,0,0))
    glPopMatrix()

    # hexagono inferior
    glPushMatrix()
    glRotate(220,1,0,0)
    dibujar_cara(vertices_h,(1,0,0))
    glPopMatrix()

    # hexagono inferior izquierdo
    glPushMatrix()
    glRotate(-40,-0.3,1,0)
    glRotate(-255,0,0,1)
    dibujar_cara(vertices_h,(1,0,0))
    glPopMatrix()

    # hexagono superior derecho
    glPushMatrix()
    glTranslate(largo/2,radio_p+ap_p,0)
    glRotate(40,-1,1,0)
    glRotate(-40,0,0,1)
    dibujar_cara(vertices_h,(1,0,0))
    glPopMatrix()

    # hexagono superior izquierdo
    glPushMatrix()
    glTranslate(d_h,radio_p+ap_p,0)
    glRotate(-40,1,1,0)
    glRotate(-260,0,0,1)
    dibujar_cara(vertices_h,(1,0,0))
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
    #Pentagono(0.3)
    #Hexagono(0.3)
    Pelota(0.1)
    
    #Habilita el cálculo de iluminación en OpenGL.
    glEnable(GL_LIGHTING)
    
    # Habilita una fuente de luz específica, en este caso 0
    glEnable(GL_LIGHT0)

    #La posición de una fuente de luz en OpenGL se establece mediante 
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # La dirección de una fuente de luz direccional se configura con
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, look_at_center)

    # La propiedad difusa de un material controla cómo reacciona la superficie del objeto a la luz incidente.
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1,1,1))

    #La propiedad especular controla los reflejos de alta luz en objetos con superficies brillantes
    glMaterialfv(GL_FRONT, GL_SPECULAR, (1,0,0.2))

    #La propiedad ambiente controla la iluminación uniforme que se produce en la escena
    glMaterialfv(GL_FRONT, GL_AMBIENT, (1,0,0))

    #La propiedad de emisión controla si un objeto emite su propia luz.
    #glMaterialfv(GL_FRONT, GL_EMISSION, (0,1,0))

    # Establece el modo de sombreado suave. Los colores se interpolan entre los vértices de un polígono, lo que resulta en una apariencia suave y más realista.
    glShadeModel(GL_SMOOTH)


    glutSwapBuffers()

# def buttons(key, x, y):
#     global ojox,ojoz
#     print(f'key={key}')
#     if key == b'a':
#         ojox += 0.1
#     if key==b'd':
#         ojox-=0.1
#     if key==b'w':
#         ojoz+=0.1
#     if key==b'x':
#         ojoz-=0.1
#     glutPostRedisplay()
def buttons(key, x, y):
    global ojox, ojoz, light_position, look_at_center

    if key == b'a':
        ojox += 0.1
        light_position[0] += 0.1
    elif key == b'd':
        ojox -= 0.1
        light_position[0] -= 0.1
    elif key == b'w':
        ojoz += 0.1
        light_position[2] += 0.1
    elif key == b'x':
        ojoz -= 0.1
        light_position[2] -= 0.1

    # Actualiza la dirección de la luz para que siga apuntando al centro
    look_at_center = [0.0 - light_position[0], 0.0 - light_position[1], 0.0 - light_position[2]]

    glutPostRedisplay()

def update_camera_position(_):
    global ojox, ojoz, light_position, look_at_center

    # Actualiza la posición de la cámara y la luz automáticamente
    ojox += 0.1
    ojoz += 0.1
    light_position[0] += 0.1
    light_position[2] += 0.1

    # Actualiza la dirección de la luz para que siga apuntando al centro
    look_at_center = [0.0 - light_position[0], 0.0 - light_position[1], 0.0 - light_position[2]]

    glutPostRedisplay()


def main():
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(width,height)
    glutCreateWindow(b'Dodecaedro')

    glEnable(GL_DEPTH_TEST)

    glutDisplayFunc(display)
    glutKeyboardFunc(buttons)
    #glutTimerFunc(int(auto_camera_move_interval * 1000), update_camera_position, 0)
    
    glutMainLoop()

if __name__=='__main__':
    main()

