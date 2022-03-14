#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 22:16
# @Author  : 张大鹏
# @Site    : 
# @File    : z01_基本用法.py
# @Software: PyCharm
import zdppy_toml as toml

print(toml.load("config/config.toml"))
print(toml.load(["config/config.toml", "config/secret/.config.toml"]))
print(toml.load(["config/secret/.config.toml", "config/config.toml"]))  # 后面的配置会覆盖前面的配置

# 将字典写入文件
d = {"username": "zhangdapeng", "mysql": {"host": "11.22.26.33"}}
with open("config/test.toml", "w") as f:
    r = toml.dump(d, f)
    print(r)

    # 将toml字符串转换为字典
    print(toml.loads(r))

    # 将字典转换为toml字符串
    r = toml.loads(r)
    print(toml.dumps(r))
