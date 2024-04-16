import time

class LegoGyro():

    port = None
    BP = None
    offset = 0

    def __init__(self, BP, port):
        self.BP = BP
        self.port = port
        BP.set_sensor_type(port, BP.SENSOR_TYPE.EV3_GYRO_ABS_DPS)


    def getYaw(self):
        return self.BP.get_sensor(self.port) + self.offset
    
    def zeroAngle(self):
        start = self.getYaw()
        time.sleep(1)
        offset = (self.getYaw() - start)
