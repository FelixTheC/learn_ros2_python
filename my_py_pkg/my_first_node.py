#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 08.08.21
@author: felix
"""
import rclpy
from rclpy.node import Node
from concurrent.futures import ThreadPoolExecutor as PoolExecutor


class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self._counter = 0
        self.logger_info("Hello ROS2")
        self.create_timer(0.5, self.timer_consumer)

    def logger_info(self, text: str):
        self.get_logger().info(text)

    def timer_consumer(self):
        self._counter += 1
        self.logger_info(f"Hello {self._counter}")


def main(*args):
    rclpy.init(args=args)
    node = MyNode()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
