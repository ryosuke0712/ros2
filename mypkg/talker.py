import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node =  Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0


def cb():
    global n
    msg = Int16()
    msg.data = n
    pub.publish(msg)
    n += 1


def main():
    node.create_timer(0.5, cb)
    rclpy.spin(node)