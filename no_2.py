import rospy
from std_msgs.msg import String
import no_1

rospy.init_node('no2')

def soma():
    print ('Soma = 24')

pub_2 = rospy.Publisher('/topico1', String, queue_size=1)


rospy.spin() 