import time
import brickpi3

class ColorSensor:

    port = None
    BP = None
    siteNum = None
    lastState = None
    sensorValues = [0,0,0,0,0,0,0,0,0,0]

    def __init__(self, BP, port: int):
        self.port = port
        self.BP = BP



    def getSensorValue(self):
        self.BP.set_sensor_type(self.port, self.BP.SENSOR_TYPE.EV3_COLOR_COLOR)
        try:
            return self.BP.get_sensor(self.port)
        except brickpi3.SensorError:
            return 7
    
    def flashColor(self, ledColor):
        if ledColor == "red":
            self.BP.set_sensor_type(self.port, self.BP.SENSOR_TYPE.EV3_COLOR_REFLECTED)
        elif ledColor == "blue":
            self.BP.set_sensor_type(self.port, self.BP.SENSOR_TYPE.EV3_COLOR_AMBIENT)
        
        
        time.sleep(0.5)
        self.BP.set_sensor_type(self.port, self.BP.SENSOR_TYPE.EV3_COLOR_COLOR)
        
        time.sleep(0.25)
