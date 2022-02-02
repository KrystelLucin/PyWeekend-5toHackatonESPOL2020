import random

def start(robot): # <<<<==================== YOUR CODE  HERE ========================
    robot.spin(random.randint(-20,20))
    robot.move_fwd()