def FrontAlign(robot):
    pid = 1.2 #0.8
    frontSpace = 5
    error = 100
    while error > .5:
        dist = robot.getFrontDistance()
        error = dist - frontSpace
        if abs(error) > 25:
            error = 0
        #print(error)
        power = pid * (error)
        robot.drive.setCM(power, power)
        robot.update()
    robot.drive.setCM(0, 0)