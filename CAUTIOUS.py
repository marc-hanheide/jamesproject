# J Birdsall, 2018
# a behaviour to simulate cautiosness, to be called using srb.py
# takes an array of x positions of people as floats, another for y positions, and a float for laser distance directly in front
# returns a float for rotation, another for speed

def cautious(xIn, yIn, dist): # inputs, list of x coords, list of y coords, and distance in front of robot from laser

    xAv = 0 # average x position of all people
    yAv = 0 # average y position of all people
    length = len(xIn) # number of people

    for i in range(0, length): # sum all coords

        xAv = xAv + xIn[i]
        yAv = yAv + yIn[i]

    if length > 0:
        xAv = xAv / length # divide by number of people to give mean
        yAv = yAv / length

    print  xIn

    lr = 0 + yAv # left right return variables, proportional to position of average human
    fb = xAv - 3 # forwards backwards return variables, speed is proportional to distance from average, stopping at 3m, reversing if closer, moving away faster than approaching
    
    if fb > 0:
        
        fb = fb / 2
    

    if dist < 1:
        
        lr = 0
        fb = -0.5

    fb = max(min(fb, .4), -.25)
    lr = max(min(lr, 1), -1)

    return fb, lr # return movement values from behaviour
