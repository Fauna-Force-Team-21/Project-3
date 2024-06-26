import math


def DriveLine(robot, v: float, distance: float):
    p = 0.40
    walMin = 5
    start = robot.odometry.getPosition()
    delta = 0
    while delta < distance:
        currPose = robot.odometry.getPosition()
        delta = math.sqrt((currPose[0] - start[0])**2 + (currPose[1] - start[1])**2)
        rot = 0
        if robot.leftD1.getDistance() < walMin:
            rot = walMin - robot.leftD1.getDistance()
        elif robot.rightD.getDistance() < walMin:
            rot = robot.rightD.getDistance() - walMin

        if abs(rot) > 2:
            rot = 0

        rot = rot * p
        robot.drive.setCM(v + rot, v - rot)
        robot.update()
    robot.drive.setCM(0,0)