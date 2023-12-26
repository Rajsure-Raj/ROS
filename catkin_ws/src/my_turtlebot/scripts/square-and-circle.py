#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def draw_square(length):
    rospy.init_node('draw_square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    for i in range(5):
        move = Twist()
        move.linear.x = length
        move.angular.z = 0
        pub.publish(move)
        rospy.sleep(2)
        move.linear.x = 0
        move.angular.z = 1.556
        pub.publish(move)
        rospy.sleep(2)

def draw_line(length):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()
    move.linear.x = -3.0
    move.angular.z = 0
    pub.publish(move)
    rospy.sleep(1)

def draw_circle(radius):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    move = Twist()
    move.linear.x = radius*4
    move.angular.z = 6.28
    pub.publish(move)
    rospy.sleep(1)




if __name__ == '__main__':
    try:
        value = int(input("Enter the dimension: "))
        draw_square(value)
        draw_line(value)
        draw_circle(value)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

    
