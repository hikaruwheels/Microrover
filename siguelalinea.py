# Imports go at the top
from microbit import *
from MicroRover import *
rover = Micro_Rover()
while True:
    #sensor_value=pin14.read_digital()<<2|pin15.read_digital()<<1|pin16.read_digital()
    sensor_value = rover.infrared_sensor_value()   
    if sensor_value==4 or sensor_value==7:
        rover.all_led_show(255,0,255,0)
        rover.motor(110,110)
    elif sensor_value==6 or sensor_value==8:
        rover.all_led_show(255,255,0,0)
        rover.motor(25,110)
    elif sensor_value==3 or sensor_value==5:
        rover.all_led_show(255,0,0,255)
        rover.motor(110,25)
    else:
        rover.all_led_show(255,255,0,255)
        rover.motor(0,0)
