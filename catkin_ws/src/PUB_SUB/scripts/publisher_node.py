#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def messagePublisher():
    pub_1 = rospy.Publisher('messageTopic_1', String, queue_size =10)
    pub_2 = rospy.Publisher('messageTopic_2', String, queue_size =10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) #10hz 
    while not rospy.is_shutdown():
        hello_str =" Hello Sir" #% rospy.get_time()
        rospy.loginfo('Published: ' + hello_str)
        new_str = "This is Raj"
        rospy.loginfo('Published: ' + new_str)
        pub_1.publish(hello_str)
        rate.sleep()
        pub_2.publish(new_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        messagePublisher()
    except rospy.ROSInterruptException:
        pass
