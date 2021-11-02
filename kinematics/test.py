from forward_kinematics import RRrobot
from inverse import two_link_robot

'''myrobot = RRrobot(2)
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
print(myrobot.forward_kinematic(dh_table))'''

robot2=two_link_robot()
x,y,a1,a2=robot2.get_value()
theta1,theta2=robot2.inverse_kinematics(x,y,a1,a2)
print("JOINT ANGLE 1 = {0}, JOINT ANGLE 2 = {1}".format(theta1,theta2))
