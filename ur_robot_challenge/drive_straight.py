import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DriveStraightNode(Node):
    def __init__(self):
        super().__init__('drive_straight_node')
        # publisher za pošiljanje ukazov za premikanje
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # za  update hitrosti na 100ms robota uporabljamo timer
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = time.time()

    def timer_callback(self):
        msg = Twist()
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time <= 3.0:
            # Vozi 0.1 m/s
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        else:
            # stop po 3s
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DriveStraightNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
