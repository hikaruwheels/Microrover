# Imports go at the top
from microbit import *
from MicroRover import *

#inicializar Rover
robot = Micro_Rover()

# Code in a 'while True:' loop repeats forever
while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,0)
        sleep(1000)
    else:
        robot.motor(255,255)
