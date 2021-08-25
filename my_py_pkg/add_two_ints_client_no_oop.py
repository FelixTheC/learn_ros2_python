#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client_no_oop")

    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(10):
        node.get_logger().warn("No Server! for AddTwoInts")

    req = AddTwoInts.Request()
    req.a = 3
    req.b = 8

    future_obj = client.call_async(req)  # secure way use client.call with caution
    rclpy.spin_until_future_complete(node, future_obj)

    try:
        node.get_logger().info(f'result: {future_obj.result()}')
    except Exception as err:
        node.get_logger().error("Service call failed %r" % err)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
