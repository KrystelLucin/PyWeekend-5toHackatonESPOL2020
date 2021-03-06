"""
Pyweekend - 5th Hackathon ESPOL 2020: ROBOTICA

Press ESC to exit, spacebar to teleoperate (arrows for steps in each direction,
'r' to rotate clockwise, 'e' counterclockwise), 'w' to perform a random walk with
random turns when bumping into walls/obstacles, 'a' for autonomous operation
(not implemented, it's the same as W right now), and 't' to toggle the trace
visibility.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, pygame
from pygame.locals import *
from simulation import *
import math
import time
import random as rnd
from reto1 import start

def main():
    clock = pygame.time.Clock()
    screen.fill((255,255,255)) 

    robot = init_simulation(obstacles=rnd.choice([10,17,25])) # <== Retorna ROBOT, recibe  parametro: numero de obstaculos (por defecto 10) o ambiente
    display_obstacles()

    allsprites = pygame.sprite.RenderPlain((robot))

    robot.draw_rays(screen)  
    pygame.display.flip()   

    going = True
    pasos = 0
    while going:
        clock.tick(fps)
        pasos = pasos + 1
        #print(robot.get_pos())  #retorna tupla (x,y)
        #print(robot.get_angle())#retorna angulo (0 es hacia arriba)
        #print(robot.get_collision()) #hay choque: booleano
        #print(robot.read_sensors()) #lista 13 valores de distancia (max 200)
        #print(robot.get_traces())  #lista de tuplas con las posiciones recorridas por el robot

        for event in pygame.event.get():
            if event == QUIT:
                going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    going = False
                if event.key == K_r:        #r is for rotation clockwise
                    robot.spin(-r_step_theta)
                if event.key == K_e:        #e for rotation counterclockwise
                    robot.spin(r_step_theta) 
                if event.key == K_f:        #f is for moving forward
                    robot.move_fwd()    
                if event.key == K_SPACE:
                    robot.opmode = 0            
                if event.key == K_s: #s is for start
                    robot.opmode = 1
        if robot.opmode:
                start(robot)   
        allsprites.update()
        screen.fill((255,255,255)) 
        display_obstacles()
        robot.draw_rays(screen)
        draw_traces(robot,screen)
        if robot.target():
                report(robot, pasos)
                going = False
        allsprites.draw(screen)
        pygame.display.flip()
    pygame.quit()  

def report(robot, pasos): 
    print(robot.get_time())
    print(pasos)
			  
if __name__ == '__main__':
    main()

