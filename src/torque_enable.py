import roslib
roslib.load_manifest('darwin_leg_tb')
import rospy, time
from dynamixel_controllers.srv import TorqueEnable, SetSpeed





dynamixel_namespace = rospy.get_namespace()
if dynamixel_namespace == '/':
    dynamixel_namespace = rospy.get_param('~dynamixel_namespace', '/dynamixel_controller')
dynamixels = rospy.get_param(dynamixel_namespace + '/dynamixels', dict())

servo_torque_enable = list()
servo_set_speed = list()

for name in sorted(dynamixels):
    torque_enable_service = dynamixel_namespace + '/' + name + '/torque_enable'
    rospy.wait_for_service(torque_enable_service)
    servo_torque_enable.append(rospy.ServiceProxy(torque_enable_service, TorqueEnable))
    set_speed_service = dynamixel_namespace + '/' + name + '/set_speed'
    rospy.wait_for_service(set_speed_service)
    servo_set_speed.append(rospy.ServiceProxy(set_speed_service, SetSpeed))

    for set_speed in servo_set_speed:
        set_speed(2)

        # Relax all servos to give them a rest.
    for torque_enable in servo_torque_enable:
        torque_enable(False)



print dynamixel_namespace
print dynamixels
