def FrontAlign(robot):
    pid = 1.5 #0.8
    frontSpace = 11.5
    power = 1
    while abs(power) > .25:
        dist = robot.getFrontDistance()
        error = dist - frontSpace
        if abs(error) > 25:
            error = 0
        #print(error)
        power = pid * (error)
        robot.drive.setCM(power, power)
        robot.update()
    robot.drive.setCM(0, 0)