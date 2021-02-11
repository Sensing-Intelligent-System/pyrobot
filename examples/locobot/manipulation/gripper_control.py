# Copyright (c) Facebook, Inc. and its affiliates.

import hydra

from hydra.experimental import initialize, compose
from omegaconf import DictConfig

import numpy as np

from pyrobot import World, make_algorithm
from pyrobot.algorithms.kinematics import Kinematics

import copy


def main():

    world = World(config_name="locobot_arm_env")

    bot = world.robots.locobot

    print("Opening gripper")
    bot.gripper.open()

    print("Closing gripper")
    bot.gripper.close()

    print("Opening gripper")
    bot.gripper.open()


if __name__ == "__main__":
    main()
