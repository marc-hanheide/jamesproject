# J Birdsall, 2018
# a behaviour to simulate friendliness, to be called using srb.py
# takes an array of x positions of people as floats, another for y positions, and a float for laser distance directly in front
# returns a float for rotation, another for speed

def friendly(xIn, yIn, dist): # inputs, list of x coords, list of y coords, and distance in front of robot from laser

    xAv = 0 # average x position of all people
    yAv = 0 # average y position of all people
    length = len(xIn) # number of people

    for i in range(0, length): # sum all coords

        xAv = xAv + xIn[i]
        yAv = yAv + yIn[i]

    if length > 0:
        xAv = xAv / length # divide by number of people to give mean
        yAv = yAv / length
    
    lr = max(min(0 + yAv, 1), -1) # left right return variables, rate of turn is proportional to position of average human
    fb = max(min(xAv - 1.5, .5) , -.5) # forwards backwards return variables, speed is proportional to distance from average human, stopping at 1.5m, reversing if closer

    print yAv

    if dist < 1:
        
        fb = -0.2
        lr = 0

    return fb, lr # return movement values from behaviour
