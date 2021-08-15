#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String


class RobotNewsStationNode(Node):

    def __init__(self):
        super().__init__("robot_news_station")
        self.logger_info("Hello ROS2")

        self.robot_name = "C3PO"
        self.publisher_ = self.create_publisher(String, "robot_news", qos_profile=10)  # keep at max 10 messages
        self.timer_ = self.create_timer(0.5, self.publish_news)  # 0.5 means 2Hz
        self.logger_info("Robot News Station has been started.")

    def logger_info(self, text: str):
        self.get_logger().info(text)

    def publish_news(self):
        msg = String()
        msg.data = f"Hi this is {self.robot_name}, from Robot News Station."
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = RobotNewsStation()
    try:
        rclpy.spin(node)  # will hold/keep alive node
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
