import rosbagpy.msgreader as msgreader
import rosbag
import cv2
from cv_bridge import CvBridge

bag = rosbag.Bag('YOUR_BAG_PATH.bag')
msgreader.print_bag_topics(bag)

image_topic = "/camera/image_raw" # Change this to your image topic
time_list, ros_time_list = msgreader.create_timelist(bag, image_topic)

n_idx = 10 # Read the n th image message
img_msg = msgreader.read_nth_msg(n_idx, bag, image_topic, ros_time_list)
bridge = CvBridge()
img = bridge.imgmsg_to_cv2(img_msg, desired_encoding="bgr8")

# save the image
cv2.imwrite("image.png", img)