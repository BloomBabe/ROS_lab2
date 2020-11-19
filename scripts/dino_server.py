#!/usr/bin/env python

from __future__ import print_function

from word_ro_dinoword.srv import GetDinosaurs, GetDinosaursResponse
import rospy
import random

def make_dino(req):
    print("Original word: ",req.word)
    suffix = ['saurus', 'raptor', 'pteryx', 'stacator', 'rex', 'ceratops', 'gnathus', 'roides', 'draco', 'dromeus']
    random.shuffle(suffix)
    current_suffix = suffix[0]
    print("Dino- word: ",req.word+current_suffix)
    return GetDinosaursResponse(req.word+current_suffix)

def dino_server():
    rospy.init_node('dino_server')
    s = rospy.Service('dino', GetDinosaurs, make_dino)
    print("Ready to transform word to dino-word.")
    rospy.spin()

if __name__ == "__main__":
    dino_server()
