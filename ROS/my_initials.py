#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
yaw=0

def poseCallback(pose_message):
    global x, y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def move(speed, distance, is_forward):
    vel_msg = Twist()
    global x,y
    x0 = x 
    y0 = y

    if (is_forward):
        vel_msg.linear.x = abs(speed)
    else :
        vel_msg.linear.x = -abs(speed)

    distance_moved = 0.0
    loop_rate = rospy.Rate(200)
    cmd_vel_topic = '/turtle1/cmd_vel'
    vel_pub = rospy.Publisher(cmd_vel_topic,Twist,queue_size=10)

    while True :
        vel_pub.publish(vel_msg)

        loop_rate.sleep()

        distance_moved = distance_moved + abs(0.5*math.sqrt(((x-x0)**2)+ ((y-y0)**2)))
        if (distance_moved>distance):
            break
    
    vel_msg.linear.x = 0
    vel_pub.publish(vel_msg)

def rotate(ang_speed_degree, rel_ang_degree, clockwise):

    global yaw 
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    theta0 = yaw
    ang_speed = math.radians(abs(ang_speed_degree))

    if (clockwise):
        vel_msg.angular.z = -abs(ang_speed)
    else:
        vel_msg.angular.z = abs(ang_speed)

    angle_moved = 0.0
    loop_rate = rospy.Rate(100)
    cmd_vel_topic = '/turtle1/cmd_vel'
    vel_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)

    t0 = rospy.Time.now().to_sec()
    
    while True :
        vel_pub.publish(vel_msg)

        t1 = rospy.Time.now().to_sec()
        current_ang_degree = (t1-t0)*ang_speed_degree
        loop_rate.sleep()

        if (current_ang_degree>rel_ang_degree):
            break
    
    vel_msg.angular.z = 0
    vel_pub.publish(vel_msg)

if __name__ == '__main__':
    try:
        rospy.init_node('Painter')

        cmd_vel_topic = '/turtle1/cmd_vel'
        vel_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = '/turtle1/pose'
        pose_sub = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)

        move(1.0, 300.0, True)
        rotate(60, 90, False)
        move(1.0, 300.0, True)
        rotate(60, 90, False)
        move(1.0, 300.0, True)
        rotate(60, 90, False)
        move(2.0, 600.0, True)
    
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated")
