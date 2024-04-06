def TurnTo(robot, angle):
    while not robot.drive.turnAngle(angle, robot.gyro.getYaw()):
            robot.update()