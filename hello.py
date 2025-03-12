#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    """
    一个简单的Python测试脚本，用于展示Git的版本控制功能
    此函数打印问候语并遍历一个水果列表
    """
    print("你好，世界！")
    print("这是一个Git测试")
    
    # 创建并遍历一个中文水果列表
    水果列表 = ["苹果", "香蕉", "橙子", "葡萄", "西瓜"]
    print("我喜欢的水果有：")
    for 索引, 水果 in enumerate(水果列表, 1):
        print(f"{索引}. {水果}")
    
    # 计算并打印总数
    print(f"总共有 {len(水果列表)} 种水果")
        
if __name__ == "__main__":
    # 当脚本被直接执行时调用main函数
    main()
