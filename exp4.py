import time
import math
import numpy as np

Libraries=[time,math,np]

from lara.Neura_API import Neura_API
home_pose=[-90,0,-100,25,-110,10]
robot_obj= Neura_API(Libraries)
saved_pose = robot_obj.getL
input("enter to movej to homepose")
robot_obj.move_J(home_pose)
input("enter to move to savedpose")
robot_obj.move_L(saved_pose)