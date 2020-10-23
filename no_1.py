import rospy
from std_msgs.msg import String
import no_2

rospy.init_node('no1')


def timerCallBack(event):
    msg = String()
    msg.data = 'Matricula: 2016000168'
    pub_1.publish(msg)
    no_2.soma()
    
pub_1 = rospy.Publisher('/topico1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin() 