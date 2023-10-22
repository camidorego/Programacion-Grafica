from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# VENTANA 2D

def ejes(largo):
    glBegin(GL_LINES)

    glColor3f(1, 0, 0)
    glVertex2f(-largo, 0)  # Eje X
    glVertex2f(largo, 0)

    glColor3f(0, 1, 0)
    glVertex2f(0, -largo)  # Eje Y
    glVertex2f(0, largo)

    glEnd()

# La función display es un lugar donde se definen las operaciones de renderización, es decir, donde se dibujan los objetos y se configuran las propiedades de visualización.
def display():
    # se borra el buffer de color de los pixeles de la ventana para que no interfiera con los nuevos colores
    glClear(GL_COLOR_BUFFER_BIT)

    # se selecciona la matriz de proyección. Utilizada para definir cómo se proyectarán los objetos (cómo se representan los objetos en la ventana gráfica desde el punto de vista de la cámara)
    glMatrixMode(GL_PROJECTION)

    # se reestablece a la matriz identidad (para aplicar las configuraciones)
    glLoadIdentity()

    # se establece la proyección ortográfica en 2D. Los cuatro argumentos son left, right, bottom, top.
    gluOrtho2D(-400, 400, -300, 300)

    # se selecciona la matriz modelo-vista. Utilizada para controlar la posición, transformaciones, etc de los objetos (cómo se transforman y colocan los objetos en la escena en sí)
    glMatrixMode(GL_MODELVIEW)

    # se reestablece a una matriz identidad
    glLoadIdentity()

    # ACA SE DEBEN REALIZAR LAS FUNCIONES DE LOS OBJETOS
    
    ejes(200)
    # se cambia entre el buffer dibujo y buffer de visualización
    glutSwapBuffers()


def main():
    # se inicializa glut
    glutInit(sys.argv)
    
    # se configura el modo de visualización (buffer doble y el esquema de colores RGB)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

    # Se establece el tamaño de la ventana
    glutInitWindowSize(800, 600)

    # se establece la posición de la ventana
    glutInitWindowPosition(100, 100)

    # se crea la ventana con un título
    glutCreateWindow(b'Ventana 2D')

    # se define la función display. se establece el callback
    glutDisplayFunc(display)

    # inicia un ciclo de eventos (llama a la función display)
    glutMainLoop()

if __name__ == "__main__":
    main()
