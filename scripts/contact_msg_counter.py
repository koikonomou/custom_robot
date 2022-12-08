# ! /usr/bin/env python3
import sys
import rospy
import numpy as np
from std_msgs.msg import Float64
from  contact_republisher.msg import contacts_msg


class Contacts(object):
    def __init__(self):
        rospy.init_node('contact_msg_init', anonymous=True)
        self.cb_init = False
        self.rate = rospy.get_param("rate",10)
        self.pub = rospy.Publisher('/published/contacts', Float64, queue_size=1)
        self.sub = rospy.Subscriber('/forces', contacts_msg, self.callback, queue_size=10)
        self.counter = 0
        self.pub_msg = 0
        while not self.cb_init:
            continue
        rospy.loginfo("Finish Subscriber Init...")

    def callback(self,msg):
        if self.cb_init is False :
            self.cb_init = True
        l_gripper = "robotiq_c2_model::robotiq_85_left_finger_tip_link::robotiq_85_left_finger_tip_link_collision"
        r_gripper = "robotiq_c2_model::robotiq_85_right_finger_tip_link::robotiq_85_right_finger_tip_link_collision"
        box_c = "unit_box::link::table_goal_collision"
        ran = len(msg.contacts)
        for i in range(ran):
            for j in range(ran):
                if  r_gripper in msg.contacts[i].collision_2 and l_gripper in msg.contacts[j].collision_2:
                    # print("TRUE")
                    self.pub_msg = 1
                else:
                    self.counter +=1
                if self.counter == 2000:
                    self.counter = 0
                    self.pub_msg = 0
                    # print('False')

    def spin(self):
        rate = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            rate.sleep()
            try:
                cont_msg = Float64()
                cont_msg.data = self.pub_msg
                self.pub.publish(cont_msg)
            except ValueError:
                rospy.logwarn_throttle(2, "contact sensor message error")


if __name__=='__main__':
    node = Contacts()
    node.spin()