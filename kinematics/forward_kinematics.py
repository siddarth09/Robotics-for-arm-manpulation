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




import numpy as np
from scipy.spatial.transform import Rotation as R
from math import *

from scipy.spatial.transform.rotation import Rotation 

class RRrobot:

    def __init__(self,n):
        self.theta=0
        self.d=0
        self.alpha=0
        self.a=0
        self.dh_table=[]
        self.number_of_links=n


    def dh_param(self):
        
        self.theta,self.d,self.alpha,self.a=input().split()
        dh_parameters=[float(self.theta),float(self.d),float(self.alpha),float(self.a)]
        return dh_parameters

    def DH(self):
        print("DH TABLE")
        for i in range(self.number_of_links):
            parameters=self.dh_param()
            self.dh_table.append(parameters)
        return self.dh_table
    
    def rotationz(self,theta):
        rotz=np.array([[cos(theta),sin(theta),0,0],
                    [-sin(theta),cos(theta),0,0],
                    [0,0,1,0],
                    [0,0,0,1]])
        #print(rotz)
        return rotz
    def translationz(self,offset_distance):
        trz=np.array([[1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,offset_distance],
                     [0,0,0,1]])
        #print(trz)
        return trz
    def rotationx(self,alpha):
        rotx=np.array([[1,0,0,0],
                      [0,cos(alpha),sin(alpha),0],
                      [0,-sin(alpha),cos(alpha),0],
                      [0,0,0,1]])
        #print(rotx)
        return rotx
    def translationx(self,linklength):
        trx=np.array([[1,0,0,linklength],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,1]])
        #print(trx)
        return trx

    def forward_kinematic(self,DH_table):
        Transformation=np.ones([4,4],dtype=np.float64)
        #print(DH_table)

        for i in range(self.number_of_links):
            self.theta=DH_table[i][0]
            self.d=DH_table[i][1]
            self.alpha=DH_table[i][2]
            self.a=DH_table[i][3]
            transform=self.rotationz(self.theta)*self.translationz(self.d)*self.rotationx(self.alpha)*self.translationx(self.a)
            Transformation*=transform
        return Transformation


if __name__=='__main__':
    myrobot = RRrobot(2)
    dh_table=myrobot.DH()
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++ DH PARAMETER TABLE FOR 2 LINK ROBOT+++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("FRAME||THETA||Dist||ALPHA||A")

    
    for i in range(2):
        print(i+1,"||",dh_table[i][0],"||",dh_table[i][1],"||",dh_table[i][2],"||",dh_table[i][3])
    print("++++++++++++++++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++++++++++++FORWARD KINEMATICS+++++++++++++++++")
    print(myrobot.forward_kinematic(dh_table))
        