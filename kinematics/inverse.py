'''MIT License

Copyright (c) 2021 SIDDARTH.D

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
from forward_kinematics import RRrobot
import numpy as np
from math import *

class two_link_robot(RRrobot):
    def __init__(self):
        self.theta1=0
        self.theta2=0
        self.desired_x=0
        self.desired_y=0
        self.link1=0
        self.link2=0
       

    def  get_value(self):
        
        des_x,des_y,a1,a2=input().split()
        self.desired_x=des_x
        self.desired_y=des_y
        self.link1=a1
        self.link2=a2
        return float(des_x),float(des_y),float(a1),float(a2)

    def inverse_kinematics(self,x,y,a1,a2):
       
        if sqrt(x**2+y**2)>(a1+a2):
            self.theta2=0.0
        else:
            self.theta2=acos((x**2 + y**2 - a1**2 - a2**2) / (2 * a1 * a2))
            self.theta1=atan(y/x)-atan((a2*sin(self.theta2))/(a1+a2*cos(self.theta2)))

        if self.theta2<0.0:
            self.theta2=-self.theta2
            self.theta1=atan(y/x)-atan((a2*sin(self.theta2))/(a1+a2*cos(self.theta2)))



        q1,q2=self.theta1,self.theta2
        return q1,q2


            
