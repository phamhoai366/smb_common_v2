#! /usr/bin/env python
import rospy
from visualization_msgs.msg import Marker

def publisher():
    rospy.init_node('visualization_marker_publisher', anonymous=True)
    
    visualize_marker_pub = rospy.Publisher('/visualization_marker', Marker, 10)
    # thiet lap thong tin marker
    marker = Marker()
    marker.header.frame_id = 'map'
    marker.type = Marker.SPHERE
    marker.action = Marker.ADD
    marker.pose.position.x = 20.0
    marker.pose.position.y = 5
    marker.pose.position.z = 0
    
    marker.pose.orientation.x = 0
    marker.pose.orientation.y = 0
    marker.pose.orientation.z = 0
    marker.pose.orientation.w = 1
    
    marker.scale.x = 0.5
    marker.scale.y = 0.5
    marker.scale.z = 0.5
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        visualize_marker_pub.publish(marker)
        rate.sleep()
        
if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass