def trun_right():
    turn_left()
    turn_left()
    trun_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()

    else:
        turn_left()
        