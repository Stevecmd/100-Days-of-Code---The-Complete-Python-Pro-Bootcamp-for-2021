def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def corners():
    turn_right()
    move()
    turn_right()
    
def follow_right_wall():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()            

while not at_goal():
    follow_right_wall()

        


    
    






################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

