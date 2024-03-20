import math
import brickpi3


class DriveTrain:
    #wheelRad = 7 / 2
    wheelRad = 8/2
    gRatio = 1
    degreeToCM = 1 / 360 * wheelRad * 2 * math.pi

    BP = None
    mPortL = None
    mPortR = None
    leftMult = None
    rightMult = None

    def __init__(self, BP, mPortL, mPortR, leftMult, rightMult):
        self.BP = BP
        self.mPortL = mPortL
        self.mPortR = mPortR
        self.leftMult = leftMult
        self.rightMult = rightMult

    def setCM(self, CMLeft, CMRight):
        self.BP.set_motor_dps(self.mPortL, self.leftMult * CMLeft / self.degreeToCM * self.gRatio)
        self.BP.set_motor_dps(self.mPortR, self.rightMult * CMRight / self.degreeToCM * self.gRatio)

    def setPower(self, left, right):
        self.BP.set_motor_power(self.mPortL, left * self.leftMult)
        self.BP.set_motor_power(self.mPortR, right * self.rightMult)

    def turnAngle(self, setpoint, currAngle):
        p = 0.4
        error = (setpoint - currAngle)
        power = error * p
        power = min(max(power, -3), 3)
        self.setCM(power, -power)
        return abs(error) < 0.5

    def resetEncoders(self):
        self.BP.offset_motor_encoder(self.mPortL, self.BP.get_motor_encoder(self.mPortL))
        self.BP.offset_motor_encoder(self.mPortR, self.BP.get_motor_encoder(self.mPortR))

    def getRightCM(self):
        return self.BP.get_motor_encoder(self.mPortR) * self.degreeToCM / self.gRatio
    
    def getLeftCM(self):
        return self.BP.get_motor_encoder(self.mPortL) * self.degreeToCM / self.gRatio
    
