def DriveTo(robot, v, distance):
    robot.drive.setCM(v, v)
    start = robot.drive.getLeftCM()
    delta = 0
    while delta < distance:
        delta = robot.drive.getLeftCM() - start
        robot.update()
    robot.drive.setCM(0,0)
