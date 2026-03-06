"""
演示数据容器字典的定义
"""

"""
字典的定义：
同样使用{}，不过存储的元素是一个个的：键值对
基础语法：{key:value,key:value,key:value,key:value,}
"""

#  定义字典
my_dict1 = {"王力宏":99,"周杰伦":88,"林俊杰":77} # 一个键值对组合在一起算一个元素

# 定义空字典
my_dict2 = {} # 空集合，set()
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1}，类型是：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2}，类型是：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3}，类型是：{type(my_dict3)}")

# 定义重复key的字典（字典不允许重复）
my_dict1 = {"王力宏":99,"王力宏":88,"林俊杰":77}
print(f"重复key字典的内容是{my_dict1}") # 新的覆盖旧的

"""
字典和集合一样不可以使用下标索引
但是字典可以通过key值来取得对应的value
语法：字典[]可以取到对应的value
"""
# 从字典中基于key获取value
my_dict1 = {"王力宏":99,"周杰伦":88,"林俊杰":77}
score = my_dict1["王力宏"]
print(f"王力宏的考试分数是：{score}")
score = my_dict1["周杰伦"]
print(f"周杰伦的考试分数是：{score}")

"""
字典的key和value可以是任意数据类型（key不可为字典）
所以字典可以嵌套
"""
# 定义嵌套字典
stu_score_dict = {
    "王力宏":{"语文":77,"数学":66,"英语":33},
    "周杰伦":{"语文":88,"数学":86,"英语":55},
    "林俊杰":{"语文":99,"数学":96,"英语":66}}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
score_wlh_Chinese = stu_score_dict["王力宏"]["语文"]
print(f"王力宏的语文成绩是：{score_wlh_Chinese}")