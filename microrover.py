# Imports go at the top
from microbit import *
from MicroRover import *

#inicializar Rover
robot = Micro_Rover()

while True:
    distancia = robot.get_distance()
    if distancia <= 10:
        robot.motor(0,0)
    else:
        robot.move_forward(8)
        robot.girarDerecha()
        robot.move_forward(8)
        robot.girarIzquierda()
        robot.move_forward(8)
        robot.girarIzquierda()
        robot.move_forward(8)
        robot.girarDerecha()
        robot.move_forward(8)
