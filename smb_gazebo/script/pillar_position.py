#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from tf2_geometry_msgs import PoseStamped
from math import atan2, degrees, sin, cos


pub = rospy.Publisher('/position_pillar', LaserScan, queue_size=10)
scann = LaserScan()

def get_pillar_pose(msg):
    goal_pose = PoseStamped()
    distance = min(msg.ranges)
    min_index = msg.ranges.index(distance)
    angle = msg.angle_min + min_index*msg.angle_increment
    goal_pose.header.frame_id = 'rslidar'
    goal_pose.header.stamp = rospy.Time.now()
    
    goal_pose.pose.position.x = distance* cos(angle)
    goal_pose.pose.position.y = distance* sin(angle)
    goal_pose.pose.position.z = 0
    goal_pose.pose.orientation.x = 0
    goal_pose.pose.orientation.y = 0
    goal_pose.pose.orientation.z = 0
    goal_pose.pose.orientation.w = 1.0
    
    # rospy.loginfo_throttle(2.0, f'Minimum range [m]: {distance}')
    # rospy.loginfo_throttle(2.0, f'Angle from the robot [degree]: {degrees(angle)}')
    # return goal_pose
    
    print('the smallest distance measurement', distance)
    print('Angle from the robot', degrees(angle))
    print('position of pillar: ', goal_pose.pose)
    

def main():
    rospy.init_node('position_pillar', anonymous=True)
    sub = rospy.Subscriber('/scan', LaserScan, get_pillar_pose)
    # rospy.on_shutdown(position.on_shutdown)
    rospy.spin()

if __name__ == "__main__":
    main()




