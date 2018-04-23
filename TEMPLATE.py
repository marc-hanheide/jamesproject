

def template(xIn, yIn, dist): # inputs, list of x coords, list of y coords, and distance in front of robot from laser
	
	xAv = 0 # average x position of all people
	yAv = 0 # average y position of all people
	length = len(xIn) # number of people
	
	for i in range(0, length): # sum all coords
		
		xAv = xAv + xIn[i]
		yAv = yAv + yIn[i]

	xAv = xAv / length # divide by number of people to give mean
	yAv = yAv / length
	
	lr = 0 # left right return variables
	fb = 0 # forwards backwards return variables
	
	# DO STUFF WITH xAv, yAv, and dist to create lr fb values
	
	return fb, lr # return movement values from behaviour