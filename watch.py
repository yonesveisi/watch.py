import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from  math import sin,cos,pi,sqrt
import matplotlib.pyplot as plt
import random as rnd

def points():
    glPointSize(15)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 0)
    glVertex2f(0, 7)
    glVertex2f(4, 6)
    glVertex2f(6, 4)
    glVertex2f(7, 0)
    glVertex2f(6, -4)
    glVertex2f(4, -6)
    glVertex2f(0, -7)
    glVertex2f(-4, -6)
    glVertex2f(-6, -4)
    glVertex2f(-7, 0)
    glVertex2f(-4, 6)
    glVertex2f(-6, 4)
    glEnd()

teta1=pi/2
teta2=pi/2
teta3=pi/2
def line(teta1,teta2,teta3):
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)
    glVertex2f(0,0)
    r1 = 7
    x1 = r1 * cos(teta1)
    y1 = r1 * sin(teta1)
    glVertex2f(x1, y1)
    glColor3f(0, 1, 0)
    glVertex2f(0, 0)
    r2 = 6
    x2 = r2 * cos(teta2)
    y2 = r2 * sin(teta2)
    glVertex2f(x2, y2)
    glColor3f(1, 0, .7)
    glVertex2f(0, 0)
    r3 = 4
    x3 = r3 * cos(teta3)
    y3 = r3 * sin(teta3)
    glVertex2f(x3, y3)
    glEnd()

def main():
    pygame.init()
    display=(900,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(100,(display[0]/display[1]),0.1, 50.0)
    glTranslate(0.0,0.0,-10)
    teta1 = pi / 2
    teta2 = pi / 2
    teta3 = pi / 2
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #glRotatef(1,3,1,1)
        glClearColor(.97,.54,.75,2)
        glClear(GL_COLOR_BUFFER_BIT)
        #Cube()
        line(teta1,teta2,teta3)
        teta1 = teta1 - 0.0012
        teta2 = teta2 - 0.000010
        teta3 = teta3 - 0.0000017
        points()
        pygame.display.flip()
        pygame.time.wait(1000)
main()
