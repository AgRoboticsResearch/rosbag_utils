import rosbagpy.msgreader as msgreader
import rosbag
import cv2
from cv_bridge import CvBridge

bag = rosbag.Bag('YOUR_BAG_PATH.bag')
msgreader.print_bag_topics(bag)

msg1_time_list, msg1_ros_time_list = msgreader.create_timelist(bag, "[TOPIC1]")
msg2_time_list, msg2_ros_time_list = msgreader.create_timelist(bag, "[TOPIC2]")

# sync 
msg1_time_list_synced, msg2_time_list_synced = msgreader.sync_msgs([msg1_time_list, msg2_time_list], dt_threshold=None)
msg1_ros_time_list_synced = [msg1_ros_time_list[i] for i in (msg1_time_list_synced[:, 1].astype(dtype=int))]
msg2_ros_time_list_synced = [msg2_ros_time_list[i] for i in (msg2_time_list_synced[:, 1].astype(dtype=int))]
