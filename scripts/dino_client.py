#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
import string
import random
from word_ro_dinoword.srv import *

def dino_client(word):
    rospy.wait_for_service('dino')
    try:
        dino_word = rospy.ServiceProxy('dino', GetDinosaurs)
        resp1 = dino_word(word)
        return resp1.dinosaurs
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    rospy.init_node('client', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        letters = string.ascii_lowercase
        word = ''.join(random.choice(letters) for i in range(10))
        print("Requesting dino-word from: ",word)
        print("%s -> %s"%(word, dino_client(word)))
        rate.sleep()


    
