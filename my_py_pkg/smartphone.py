#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time

import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class SmartphoneNode(Node):

    def __init__(self):
        super().__init__("smartphone")
        self.subscriber_ = self.create_subscription(String, "robot_news", self.callback_robot_news, qos_profile=10)
        self.logger_info("Smartphone has been started.")

    def logger_info(self, text: str):
        self.get_logger().info(text)

    def callback_robot_news(self, msg: String):
        self.logger_info(f'Received: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
