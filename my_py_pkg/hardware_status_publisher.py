#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import HardwareStatus


class HardwareStatusPublisherNode(Node):

    def __init__(self):
        super().__init__("hardware_status_publisher")
        self.hw_status_publisher = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_hw_status)
        self.logger_info("hardware_status_publisher started...")

    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 45
        msg.are_motors_ready = True
        msg.debug_message = "Nothing special here"
        self.hw_status_publisher.publish(msg)

    def logger_info(self, text: str):
        self.get_logger().info(text)


def main(args=None):
    rclpy.init(args=args)
    node = HardwareStatusPublisherNode()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
