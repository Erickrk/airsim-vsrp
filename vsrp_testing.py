# Adapted from airsim's hello_car

#import setup_path
import airsim
import cv2
import numpy as np
import os
import time
import tempfile

client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)
print("API Control enabled: %s" % client.isApiControlEnabled())
car_controls = airsim.CarControls()

# steering possible values: 1 -> right
#                          -1 -> left
#                           0 -> none                         
def movement(direction, time = 1):
    if(direction == "forward"):
        car_controls.throttle = 0.75
        car_controls.steering = 0
        client.setCarControls(car_controls)
        
    elif(direction == "forward_right"):
        car_state = client.getCarState()
        car_controls.throttle = 0.5
        car_controls.steering = 1
        client.setCarControls(car_controls)
        
    elif(direction == "forward_left"):
        car_controls.throttle = 0.5
        car_controls.steering = -1
        client.setCarControls(car_controls)
        
for idx in range(1):
    # get state of the car
    car_state = client.getCarState()
    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    movement("forward_right", 3)
    time.sleep(3)  #TODO insert this inside the movement function
    movement("forward", 6)
    time.sleep(6)  
    movement("forward_left", 1)
    time.sleep(1)   
    movement("forward", 6)
    time.sleep(10) 
    movement("forward_left", 1)
    time.sleep(3)
       
    # Final brake
    car_controls.brake = 1
    client.setCarControls(car_controls)
    time.sleep(3)  
    car_controls.brake = 0 #remove brake
client.reset()

