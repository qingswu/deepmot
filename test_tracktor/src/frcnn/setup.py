#==========================================================================
# This file is under License LGPL-3.0 (see details in the license file).
# This file is a part of implementation for paper:
# How To Train Your Deep Multi-Object Tracker.
# This contribution is headed by Perception research team, INRIA.
# Contributor(s) : Yihong Xu
# INRIA contact  : yihong.xu@inria.fr
# created on 16th April 2020.
# the code is modified based on:
# https://github.com/phil-bergmann/tracking_wo_bnw/tree/iccv_19
# https://github.com/jwyang/faster-rcnn.pytorch/
# Faster R-CNN Written by Ross Girshick,
# MIT licence, Copyright (c) 2015 Microsoft
#==========================================================================
from setuptools import setup, find_packages

setup(name='frcnn',
      packages=['frcnn'],
      package_dir={'frcnn':'frcnn'},)
