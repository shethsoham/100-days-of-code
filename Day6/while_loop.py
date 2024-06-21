#Reeborg.py
def turn_right():
    turn_left()
    turn_left()
    turn left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
number_of_hurdeles = 6
while  number_of_hurdeles > 0:
    jump()
    number_of_hurdeles -= 1
    print(number_of_hurdeles)