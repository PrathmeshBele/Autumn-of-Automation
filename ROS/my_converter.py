#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import quaternion
from beginner_tutorials.msg import euler_ang
from math import *

q = quaternion()
e = euler_ang()

def q_to_e(q):


    sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
    cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
    e.r = atan2(sinr_cosp, cosr_cosp)

    sinp = 2 * (q.w * q.y - q.z * q.x)
    if abs(sinp) >= 1:
        e.p = copysign(pi/2, sinp)
    else:
        e.p = asin(sinp)

    siny_cosp = 2 * (q.w * q.z + q.x * q.y)
    cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
    e.y = atan2(siny_cosp, cosy_cosp)

    return e

def callback(data):
    rospy.loginfo(data)

def convert():
	rospy.init_node('my_converter')
	rospy.Subscriber("topic1", quaternion, callback)
	pub = rospy.Publisher('topic2', euler_ang, queue_size=10)
	rate = rospy.Rate(5)

	while not rospy.is_shutdown():

		e = q_to_e(q)

		rospy.loginfo(e)
		pub.publish(e)
		rate.sleep()


if __name__ == '__main__':
    try:
        convert()
    except rospy.ROSInterruptException:
        pass