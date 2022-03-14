#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 22:16
# @Author  : 张大鹏
# @Site    : 
# @File    : z01_基本用法.py
# @Software: PyCharm
from zdppy_toml import Toml

t = Toml()
print(t)

# 追加配置
t.update_config({"aa": 111, "bb": [22, 33, 44]})
print(t)
