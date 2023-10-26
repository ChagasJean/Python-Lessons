'''
CONSTANT = "Variables" that will not change
'''

velocity_car = 61  # current speed of the car, which can exceed 61
locale_car = 100  # location where the car is on the road, which can also change

# Observation: "Variables" in capital letters will always indicate constant values.

RADAR_1 = 60  # maximum speed of a radar, and cannot exceed the assigned value
LOCALE_1 = 100  # location where radar number 1 is, and cannot be changed location
RADAR_RANGE = 1  # the area in which the radar can detect a car

vel_car_exceeded_radar_1 = velocity_car > RADAR_1
car_exceeded_radar_1 = locale_car >= (
    LOCALE_1 - RADAR_RANGE) and locale_car <= (LOCALE_1 + RADAR_RANGE)
car_fined = car_exceeded_radar_1 and vel_car_exceeded_radar_1

if vel_car_exceeded_radar_1:
    print('The speed of the car exceeded the radar 1.')

if car_fined:
    print('Car fined on radar 1.')
