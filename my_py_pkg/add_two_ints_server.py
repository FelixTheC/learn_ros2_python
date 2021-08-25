#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsServerNode(Node):

    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_ = self.create_service(AddTwoInts, "add_two_ints", self.callback_add_two_ints)
        self.logger_info("Hello ROS2")

    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.logger_info(f"{request.a + request.b = }")
        return response

    def logger_info(self, text: str):
        self.get_logger().info(text)


def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
