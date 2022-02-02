import random
import numpy as np
import pygame

def start(robot): # <<<<==================== YOUR CODE  HERE ========================
    robot.move_fwd()
    lista_angulos = list(range(0,181,15))
    lista_sensores=robot.read_sensors()
    lis_dere=lista_sensores[:4]
    medio=lista_sensores[4:9]
    lis_izq=lista_sensores[9:]
    posicion=robot.get_pos()
    x=posicion[0]
    y=posicion[1]
    promIzquier=sum(lis_izq)/len(lis_izq)
    promDere=sum(lis_dere)/len(lis_dere)
    promMedio=sum(medio)/len(medio)
    if (y == 0) or (x==0) or (y==700) and (x!=1200):
        if robot.get_angle() >= 0:
            angulo = robot.get_angle() + 90
        else:
            angulo = robot.get_angle() + 270
        robot.spin(angulo)
    elif (x == 1200) :
        angulo = robot.get_angle()
        robot.spin(-angulo)
    #elif x<1000 and y>10:
    elif robot.get_collision():
        if promDere>=170 and promDere>=promIzquier:
            robot.spin(-90)
        elif promIzquier>=170 and promIzquier>promDere:
            robot.spin(90)
        else:
            robot.spin(120)
        # if lista_sensores[6]>115:
        #     robot.move_fwd()
        # elif(promDere)>(promIzquier) and (promDere)>(promMedio):
        #     robot.spin(30)
        # elif (promDere)<(promIzquier) and (promIzquier)>(promMedio):
        #     # if (promDere) > (promMedio):
        #     #     robot.spin(30)
        #     # elif (promDere) < (promMedio):
        #     #     robot.move_fwd()
        #     # else:
        #     robot.spin(-30)
        # # elif (sum(medio)/len(medio))==200:
        # #     robot.move_fwd()
        # elif (promMedio)> (promDere) and (promMedio)>(promIzquier):
        #     robot.move_fwd()
        # if robot.get_collision():
        #     robot.spin(-45)

    else:
        if y == 0:
            if robot.get_angle() >= 0:
                angulo = robot.get_angle() + 90
            else:
                angulo = robot.get_angle() - 270
            robot.spin(angulo)
        elif x == 1200:
            angulo = robot.get_angle()
            robot.spin(-angulo)
         # if robot.get_collision() and x==1200:
         #     robot.spin(90)
         # elif robot.get_collision() and y==0:
         #     robot.spin(-90)
         # else:
         #     robot.move_fwd()





































