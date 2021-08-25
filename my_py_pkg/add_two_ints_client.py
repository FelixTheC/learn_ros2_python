#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import partial

import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class AddTwoIntsClientNode(Node):

    def __init__(self):
        super().__init__("add_two_ints_client")
        self.logger_info("Hello ROS2")
        self.call_add_two_ints_server(6, 7)

    def call_add_two_ints_server(self, a: int, b: int):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.5):
            self.logger_warn("Waiting for Server AddTwoInts...")

        future = client.call_async(AddTwoInts.Request(a=a, b=b))
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            result = future.result()
            self.logger_info(f'{a} + {b} = {result}')
        except Exception as err:
            self.logger_error(f'{err}')

    def logger_info(self, text: str):
        self.get_logger().info(text)

    def logger_warn(self, text: str):
        self.get_logger().warn(text)

    def logger_error(self, text: str):
        self.get_logger().error(text)


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientNode()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
