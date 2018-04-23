import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from people_msgs.msg import People
from CONTROL import control
from FRIENDLY import friendly
from CAUTIOUS import cautious

class SRB:

    def __init__(self):

        self.movePub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10) # publisher for move commands
        self.peopleSub = rospy.Subscriber('/people_tracker_filter/people', People, self.peopleCall) # subscribe to people tracker
        self.laserSub = rospy.Subscriber('/scan', LaserScan, self.laserCall) # subscribe to laser
        self.distance = 0 # variable to store distance from laser

        while True:
            print("select behaviour")
            print("1) control")
            print("2) friendly")
            print("3) cautious")
            self.choice = input("> ")
            if self.choice == "1" or self.choice == "2":
                break
            elif self.choice == "3":
                break
            print("started")

    def peopleCall(self, msg): # what to do with people data

        xCoords = [] # arrays to hold x, y coords of people from people tracker
        yCoords = []

        for i in msg.people:
            xCoords.append(i.position.x)
            yCoords.append(i.position.y)
            print(i.name)

        if self.choice == "1": # control

            (fb, lr) = control(xCoords, yCoords, self.distance) # get movement commands from behaviour function, forwards/backwards, left/right
            print('reacting')

        if self.choice == "2": # friendly

            (fb, lr) = friendly(xCoords, yCoords, self.distance)
            print('reacting')

        if self.choice == "3": # cautious

            (fb, lr) = cautious(xCoords, yCoords, self.distance)
            print('reacting')

            self.twist = Twist() # twist message to hold commands
            self.twist.angular.z = lr
            self.twist.linear.x = fb

            self.movePub.publish(self.twist) # send commands

    def laserCall(self, msg): # what to do with laser data

        self.distance = msg.ranges[90] # get range directly in front of robot


rospy.init_node('srb')
srb = SRB()
rospy.spin()
