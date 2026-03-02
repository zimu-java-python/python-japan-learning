"""
演示数据容器集合的使用
"""

"""
集合的特点
无序，不可重复，不支持下标索引
允许修改
"""

# 定义集合
my_set = {"传智教育","黑马程序员","itheima,","传智教育","黑马程序员","itheima,","传智教育","黑马程序员","itheima,"}
my_set_empty = set() # 定义空集合
print(f"my_set的内容是：{my_set}，类型是{type(my_set)}")
print(f"my_set的内容是：{my_set_empty}，类型是{type(my_set_empty)}")

"""
添加新元素
语法：集合.add(元素)，将指定元素，添加到集合内
结果：集合本身被修改，添加了新元素
"""
# 添加新元素
my_set.add("Python")
my_set.add("传智教育") # 去重
print(f"my_set添加元素后结果是：{my_set}")

"""
移除元素
"""