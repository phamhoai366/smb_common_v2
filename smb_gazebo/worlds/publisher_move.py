#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2

class MoveToGoal:
    def __init__(self):
        rospy.init_node('move_to_goal_node', anonymous=True)
        
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.update_odom)
        
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        
        self.x_goal = 19
        self.y_goal = 5
        
    def update_odom(self, msg):
        self.x=msg.pose.pose.position.x
        self.y=msg.pose.pose.position.y
        orientation_q = msg.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, self.yaw) = euler_from_quaternion(orientation_list)
        
    def get_distance_to_goal(self):
        return ((self.x_goal-self.x)**2 + (self.y_goal-self.y)**2)**0.5
    
    def get_angle_to_goal(self):
        return atan2(self.y_goal-self.y, self.x_goal-self.x)
    
    def move_to_goal(self):
        twist = Twist()
        while self.get_distance_to_goal() > 0.1:
            angle=self.get_angle_to_goal()
            
            if abs(angle - self.yaw) > 0.1:
                twist.linear.x = 0
                twist.angular.z = 0.3
            else:
                twist.linear.x = 0.5
                twist.angular.z = 0
                
            self.cmd_vel_pub.publish(twist)
            rospy.sleep(0.2)
            
            
if __name__ == '__main__':
    # rospy.init_node("move_to_goal_node")
    move = MoveToGoal()
    move.move_to_goal()
    rospy.spin()