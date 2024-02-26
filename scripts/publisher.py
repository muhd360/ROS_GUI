#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32,Float32
import random

def simple_publisher():
    # Initialize ROS node
    rospy.init_node('simple_publisher')

    # Create publishers on the topics "numbers1" to "numbers4"
    pub1 = rospy.Publisher('numbers', Float32, queue_size=10)
    pub2 = rospy.Publisher('numbers2', Float32, queue_size=10)
    pub3 = rospy.Publisher('numbers3', Float32, queue_size=10)
    pub4 = rospy.Publisher('numbers4', Float32, queue_size=10)
    pub5 = rospy.Publisher('latitude', Float32, queue_size=10)
    pub6 = rospy.Publisher('longitude', Float32, queue_size=10)
    # Rate at which to publish messages (1 Hz in this example)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        # Choose a random number from 28.05 to 30
        num = 28.05 + random.uniform(0, 1.95)
        
        # Choose random numbers for the other variables
        num1 = 21 + random.uniform(0, 0.33)
        num2 = 18.44 + random.uniform(0, 2.7)
        num3 = 22+ random.uniform(0, 3.95)
        lat = 19.0222 
        longi = 72.8561
        # Create Float32 messages
        msg = Float32()
        msg1 = Float32()
        msg2 = Float32()
        msg3 = Float32()
        msg4 = Float32()
        msg5 = Float32()

        # Assign values to the messages
        msg.data = float(num)
        msg1.data = float(num1)
        msg2.data = float(num2)
        msg3.data = float(num3)
        msg4.data = float(lat)
        msg5.data = float(longi)
        # Publish the messages to the respective topics
        pub1.publish(msg)
        pub2.publish(msg1)
        pub3.publish(msg2)
        pub4.publish(msg3)
        pub5.publish(msg4)
        pub6.publish(msg5)
        #rospy.loginfo("numbers: {}, numbers2: {}, numbers3: {}, numbers4: {}".format(msg.data, msg1.data, msg2.data, msg3.data))
        rate.sleep()

if __name__ == '__main__':
    try:
        simple_publisher()
    except rospy.ROSInterruptException:
        pass
