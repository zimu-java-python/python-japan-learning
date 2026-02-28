"""
从数据容器的角度学习字符串
"""

"""
字符串作为数据容器的特点：
只可以存储字符串
长度任意（取决于内存大小）
支持下标索引
允许重复字符串的存在
不可以修改（不可增加或删除）
支持for循环
"""

my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16] # 空格也算一个字符
print(f"从字符串{my_str}取下标为2的元素，值是：{value}，取下标为-16的元素是，值是：{value2}")

# 和元组一样，字符串无法修改
# my_str[2] = "H"

# index方法
index = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是：{index}")

"""
字符串的替换
语法：字符串.replace(字符串1,字符串2)
功能：将字符串的全部：字符串1，替换为字符串2
注意：不是修改字符串本身，而是得到了一个新的字符串（返回值）
"""
# replace方法
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}，进行替换后得到：{new_my_str}")

"""
字符串的分割
语法：字符串.split(分隔符字符串)
功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
注意：字符串本身不变，而是得到了一个列表对象
"""
# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到{my_str_list}，类型是{type(my_str_list)}")

"""
字符串的规整操作（去前后空格以及回车符）
语法：字符串.strip()
字符串的规整操作（去前后指定字符串）
语法：字符串.strip(字符串)
"""
# strip方法
my_str = "  itheima and itcast  "
new_my_str = my_str.strip() # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果是：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12") # 去除1和2
print(f"字符串{my_str}被strip('12')后，结果是：{new_my_str}")

# 统计字符串中某字符串的出现次数
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")

# 统计字符串的长度
my_str = "itheima and itcast"
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")