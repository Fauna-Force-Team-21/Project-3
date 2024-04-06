def DriveTo(robot, v, distance):
    robot.drive.setCM(v,v)
    start = robot.drive.getLeftCM()
    while abs(robot.drive.getLeftCM() - start) < distance:
        robot.update()
