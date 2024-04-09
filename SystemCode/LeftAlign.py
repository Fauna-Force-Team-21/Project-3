def LeftAlign(robot):
    pid = 1.2 #0.8
    error = 100
    while error > .5:
        d1 = robot.leftD1.getDistance()
        d2 = robot.leftD2.getDistance()
        error = d1-d2
        if abs(error) > 25:
            error = 0
        #print(error)
        power = pid * (error)
        robot.drive.setCM(-power, power)
        robot.update()
    robot.drive.setCM(0, 0)