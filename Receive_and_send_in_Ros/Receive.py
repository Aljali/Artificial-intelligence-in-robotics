import rospy 
from std_msgs.msg import String

rospy.init_node("node2")

def cb(msg):
	print (msg.data)

rospy.Subscriber('myTopic' , String , callback=cb)

rospy.spin()	
	
