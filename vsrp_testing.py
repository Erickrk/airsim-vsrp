# Adapted from airsim's hello_car
# connect to the AirSim simulator

import setup_path
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


for idx in range(5):
    # get state of the car
    car_state = client.getCarState()
    print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    # Go forward + steer right
    # then sleeps so car can drive alone
    car_controls.throttle = 0.5
    car_controls.steering = 1
    client.setCarControls(car_controls)
    time.sleep(3)  

    # go forward
    car_controls.throttle = 0.75
    car_controls.steering = 0
    client.setCarControls(car_controls)
    time.sleep(6)  

    # Go forward + steer left
    car_controls.throttle = 0.5
    car_controls.steering = -1
    client.setCarControls(car_controls)
    time.sleep(1)   

    # go forward
    car_controls.throttle = 2
    car_controls.steering = 0
    client.setCarControls(car_controls)
    time.sleep(5) 

    # Go forward + steer left
    car_controls.throttle = 0.5
    car_controls.steering = -1
    client.setCarControls(car_controls)
    # print("Go Forward, steer right")
    time.sleep(3)   # let car drive a bit
    car_controls.is_manual_gear = False # change back gear to auto
    car_controls.manual_gear = 0

    # apply brakes
    car_controls.brake = 1
    client.setCarControls(car_controls)
    time.sleep(3)  
    car_controls.brake = 0 #remove brake

#restore to original state
client.reset()

client.enableApiControl(False)
