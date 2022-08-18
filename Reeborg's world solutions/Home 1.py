def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def corners():
    turn_right()
    move()
    turn_right()
    
def follow_wall():
    if front_is_clear():
        move()
    else:
        turn_left()            

while not at_goal():
    follow_wall()

        


    
    






################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

