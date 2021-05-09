from drone_interfaces.srv import Move
from std_srvs.srv import Empty

import rclpy
import time


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('drone_service_client')
    cli = node.create_client(Empty, 'takeoff')
    req = Empty.Request()
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("takeoff successful")

    time.sleep(5)

    cli = node.create_client(Move, 'move_forward')
    req = Move.Request()
    req.distance = 50
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("move forward successful")

    time.sleep(5)
    
    cli = node.create_client(Move, 'left')
    req = Move.Request()
    req.distance = 50
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("left successful")
        
    time.sleep(5)
    
    cli = node.create_client(Move, 'right')
    req = Move.Request()
    req.distance = 50
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("right successful")
        
    time.sleep(5)
    
    cli = node.create_client(Empty, 'battery')
    req = Empty.Request()
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("battery displayed successful", response.result.result)

    time.sleep(5)
    
    cli = node.create_client(Empty, 'land')
    req = Empty.Request()
    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    future = cli.call_async(req)
    rclpy.spin_until_future_complete(node, future)

    try:
        result = future.result()
    except Exception as e:
        node.get_logger().info('Service call failed %r' % (e,))
    else:
        node.get_logger().info("land successful")

        

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
