from random import uniform

def control(xIn, yIn, dist): # inputs, list of x coords, list of y coords, and distance in front of robot from laser
    
    xAv = 0 # average x position of all people
    yAv = 0 # average y position of all people
    length = len(xIn) # number of people
    
    for i in range(0, length): # sum all coords
    
        xAv = xAv + xIn[i]
        yAv = yAv + yIn[i]
    
    if length > 0:
        xAv = xAv / length # divide by number of people to give mean
        yAv = yAv / length
        
    lr = uniform(-0.5, 0.5) # left right return variables, produced at random
    fb = uniform(0.2, 0.4) # forwards backwards return variables, produced at random
    
    if dist < 1: # anticollision
        
        lr = 1
        
    return fb, lr # return movement values from behaviour
