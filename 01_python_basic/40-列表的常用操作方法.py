"""
列表的常用操作（方法）和特点
"""

"""
列表的常用操作（方法）
1：向列表中追加一个元素：列表.append(元素)
2：将数据容器的内容依次取出，追加到列表尾部：列表.extend(容器)
3：在指定下标处，插入指定的元素：列表.insert(下标，元素)
4：删除列表指定下标元素：del 列表[下标]
5：删除列表指定下标元素：列表.pop(下标)
6：从前向后，删除此元素的第一个匹配项：列表.remove(元素)
7：清空列表：列表.clear()
8：统计此元素在列表中出现的个数:列表.count(元素)
9：查找指定元素在列表的下标，找不到报错ValueError：列表.index(元素)
10：统计容器内有多少元素：len(列表)
"""

"""
列表的特点
可以容纳多个元素（上限为2**63-1、9223372036854775807个）
可以容纳不同类型的元素（混装）
数据是有序存储的（有下标序号）
允许重复数据存在
可以修改（增加或删除元素等）
"""

"""
列表的查询功能（方法）
-查找某元素的下标
功能：查找指定元素在列表的下标，如果找不到，报错ValueErrror
语法：列表.index(元素)
注意：index就是列表对象（变量）内置的方法（函数）
"""
my_list = ["itcast","itheima","python"]
# 查找某元素在列表的下标索引
index = my_list.index("itheima")
print(f"\"itheima\"在列表的下标索引值是：{index}")
# 如果被查找的元素不存在，会报错
# index = my_list.index("hello")
# print(f"\"hello\"在列表的下标索引值是：{index}")

"""
如何修改特定下标索引的值
语法：列表[下标] = 值
可以用如上语法，直接对指定下标（正向，反向下标均可）的值进行：重新赋值（修改）
"""
# 修改特定下标索引的值
my_list[0] = "传智教育"
print(f"列表被修改后，结果是{my_list}")

"""
如何在列表内插入元素
语法：列表.insert(下标,元素)，在指定的下标位置，插入指定的元素
"""
# 在指定下标位置插入新元素
my_list.insert(1,"best")
print(f"列表被修改后，结果是{my_list}")

"""
如何在列表内追加元素
语法：列表.append(元素)，将指定元素追加到列表的尾部（单个）
语法：列表.extend(其他数据容器)，将其他数据容器的内容取出，依次追加到列表尾部（多个）
"""
# 在列表的尾部追加“单个”新元素
my_list.append("黑马程序员")
print(f"列表被修改后，结果是{my_list}")

# 在列表的尾部追加“一批”新元素
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(f"列表被修改后，结果是{my_list}")

"""
如何删除列表内的元素
语法1：del 列表[下标]
语法2：列表.pop(下标)
"""
# 删除指定下标索引的元素（两种方式）
my_list = ["itcast","itheima","python"]
del my_list[2]
print(f"列表被修改后，结果是{my_list}")

my_list = ["itcast","itheima","python"]
element = my_list.pop(2) # 取出的元素作为返回值去得到
print(f"列表被修改后，结果是{my_list}，取出的元素是：{element}")

"""
删除某元素在列表中的第一个匹配项,从前往后
语法：列表.remove(元素)
"""
my_list = ["itcast","itheima","itcast","itheima","python"]
my_list.remove("itheima")
print(f"列表被修改后，结果是{my_list}")

"""
清空列表内容
语法：列表.clear()
"""
my_list = ["itcast","itheima","python"]
my_list.clear()
print(f"列表被修改后，结果是{my_list}")

"""
统计某元素在列表内的数量
语法：列表.count(元素)
"""
my_list = ["itcast","itheima","itcast","itheima","python"]
count = my_list.count("itheima")
print(f"列表中itheima的数量是：{count}")

"""
统计列表内一共有多少个元素
语法：len(列表)
"""
my_list = ["itcast","itheima","itcast","itheima","python"]
num = len(my_list)
print(f"列表中一共有{num}个元素")

