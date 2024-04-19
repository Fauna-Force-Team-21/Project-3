from Timer import Timer
import math

def TurnTo(robot, angle):
    speed = 5
    mult = math.copysign(1, angle)
    r = 10.5
    t = math.radians(angle) * r / speed
    timer = Timer(t)
    robot.drive.setCM(mult * speed, -mult * speed)
    while not timer.isTime:
        robot.update()
    robot.drive.setCM(0, 0)
