def TurnTo(robot, angle):
    startAngle = robot.legoGyro.getYaw()
    while not robot.drive.turnAngle(startAngle, robot.legoGyro.getYaw() - angle):
            robot.update()
    robot.drive.setCM(0, 0)