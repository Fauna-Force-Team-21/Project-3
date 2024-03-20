import time
import grovepi
import brickpi3
import math

from Gyroscope import Gyroscope
from Timer import Timer


# set up sys variables
startTime = time.time()
currTime = time.time()
UPDATERATE = 0.05

BP = brickpi3.BrickPi3()

# set up gyroscope
gyro = Gyroscope(5)
gyro.zeroGyro()
gyro.updateGyro()

#set up drive motors
pitchMotor = BP.PORT_C
rollMotor = BP.PORT_D

p1 = 10
p2 = 10

# run program here
try:
    time.sleep(1)
    while True:
        #drive.setCM(10,10)
        angles = gyro.getAngle()
        print(angles)

        BP.set_motor_dps(pitchMotor, p1 * angles["roll"] * -1)
        BP.set_motor_dps(rollMotor, p2 * angles["pitch"] * -1)

        gyro.updateGyro()
        time.sleep(UPDATERATE)




except IOError as error:
    print(error)
    BP.set_motor_dps(pitchMotor,0)
    BP.set_motor_dps(rollMotor,0)
    BP.reset_all()
except TypeError as error:
    print(error)
    BP.set_motor_dps(pitchMotor,0)
    BP.set_motor_dps(rollMotor,0)
    BP.reset_all()
except KeyboardInterrupt:
    print("You pressed ctrl+C...")
    BP.set_motor_dps(pitchMotor,0)
    BP.set_motor_dps(rollMotor,0)
    BP.reset_all()