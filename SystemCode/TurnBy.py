def TurnTo(robot, angle):
    startAngle = robot.legoGyro.getYaw()
    while not robot.drive.turnAngle(0.0, angle - startAngle):
            robot.update()