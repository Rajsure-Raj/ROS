#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

    
def callback(data):
    rospy.loginfo("I heard %s",data.data)
    
def callback1(data):
    rospy.loginfo("new message : %s",data.data)


def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("messageTopic_1", String, callback)

    rospy.Subscriber("messageTopic_2", String, callback1)
    rospy.spin()


if __name__ == '__main__':
    listener()
    
