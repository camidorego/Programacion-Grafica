from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Función para dibujar la curva de Bézier
def draw_bezier_curve(control_points, cant_lineas):

    glColor(1, 0, 0)  # Color rojo
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)

    # Dibuja la curva de Bézier
    for t in range(cant_lineas):
        t /= 100.0
        x, y = calculate_bezier_point(t, control_points)
        glVertex2f(x, y)

    glEnd()
    glFlush()

# Función para calcular un punto en la curva de Bézier
def calculate_bezier_point(t, control_points):
    x = (1 - t) ** 3 * control_points[0][0] + 3 * (1 - t) ** 2 * t * control_points[1][0] + 3 * (1 - t) * t ** 2 * control_points[2][0] + t ** 3 * control_points[3][0]
    y = (1 - t) ** 3 * control_points[0][1] + 3 * (1 - t) ** 2 * t * control_points[1][1] + 3 * (1 - t) * t ** 2 * control_points[2][1] + t ** 3 * control_points[3][1]
    return x, y

def hoja():
    # Puntos de control para la curva de Bézier
    control_points = ((-100, -100), (-200, 0), (-200, 100), (-100, 200))
    draw_bezier_curve(control_points, 100)

    control_points = ((-100, -100), (0, 0), (0, 100), (-100, 200))
    draw_bezier_curve(control_points,100)

    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(-100,-100)
    glVertex2f(-100,200)
    glEnd()
    

    glFlush()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # se configura la matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-400, 400, -400, 400)  # se ajusta la escala de la ventana
    #gluOrtho2D(-1, 1, -1, 1)

    # se selecciona e inicializa la matriz de visualización
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # # Puntos de control para la curva de Bézier
    # control_points = ((-100, -100), (-200, 0), (-200, 100), (-100, 200))
    # draw_bezier_curve(control_points, 100)
    hoja()
    glutSwapBuffers()

# Función principal
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'Curva de Bezier')
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
