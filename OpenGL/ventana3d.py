from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ojox, ojoy, ojoz = 1, 1, 2

width, height= 800,800

def ejes(largo):
    ## EJE X ##
    # configuramos que se dibujen lineas en este bloque
    glBegin(GL_LINES)

    # definimos el color de la linea (rojo)
    glColor3f(1,0,0)

    # definimos la posicion del primer vertice de la linea
    glVertex3f(0,0,0)

    # definimos el segundo vertice de la linea
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

def display():
    global ojox, ojoy, ojoz

    # se borra el buffer de color de los pixeles de la ventana para que no interfiera con los nuevos colores y se borra el buffer de profundidad
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # se selecciona la matriz de proyeccion. Utilizada para definir como se proyectaran los objetos (cómo se representan los objetos en la ventana gráfica desde el punto de vista de la cámara)
    glMatrixMode(GL_PROJECTION)

    # se reestablece a la matriz identidad (para aplicar las configuraciones)
    glLoadIdentity()

     # se configura la perspectiva (angulo de apertura, relacion de aspecto(width/height), distancia mas cercana de la camara, distancia mas lejana de la camara)
    gluPerspective(45, (width / height), 0.1, 50.0)

    # se selecciona la matriz modelo-vista. Utilizada para controlar la posicion, transformaciones, etc de los objetos (cómo se transforman y colocan los objetos en la escena en sí)
    glMatrixMode(GL_MODELVIEW)

    # se reestablece a una matriz identidad
    glLoadIdentity()
    
    gluLookAt(ojox, ojoy, ojoz, 0, 0, 0, 0.0, 1.0, 0.0)

    ejes(2)

    # se cambia entre el buffer dibujo y buffer de visualizacion
    glutSwapBuffers()
   


def main():
    # se inicializa glut
    glutInit(sys.argv)

    # se configura la visualizacion (buffer doble, modo rgb de colores,  Habilita el búfer de profundidad(z-buffer))
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    # se define el tamanho de la ventana
    glutInitWindowSize(800, 600)

    # se crea la ventana con  el titulo
    glutCreateWindow(b'Ventana 3D Vacia')
    
    # se habilita la prueba de profundidad, que es una técnica que compara las profundidades de los objetos en la escena para determinar cuál objeto se encuentra delante y cuál detrás
    glEnable(GL_DEPTH_TEST)
    
    # se configura una función de devolución de llamada (callback) que se llama cada vez que se necesita redibujar la ventana.
    glutDisplayFunc(display)
    
    # inicia el ciclo de eventos de GLUT
    glutMainLoop()

if __name__ == '__main__':
    main()
