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
        try:
            return -1 * self.BP.get_sensor(self.port)[0] + self.offset
        except:
            return 0
    
    def getValue(self):
        try:
            return [-1 * self.BP.get_sensor(self.port)[0],self.BP.get_sensor(self.port)[1]]
        except:
            return [0,0]
        
    def zeroGyro(self):
        self.offset = -1 * self.getYaw()
