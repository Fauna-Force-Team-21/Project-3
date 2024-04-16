def TurnTo(robot, angle):
    while not robot.drive.turnAngle(0, angle - robot.gyro.getYaw()):
            robot.update()