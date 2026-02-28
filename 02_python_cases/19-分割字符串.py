"""
分割字符串
"""
# 定义一个字符串
my_str = "itheima itcast boxuegu"

# 统计字符串内有多少个"it"字符
count = my_str.count("it")
print(f"字符串{my_str}中有：{count}个it字符")

# 将字符串内的空格全部替换为字符："|"
new_my_str = my_str.replace(" ", "|")
print(f"字符串{my_str}，被替换空格后，结果：{new_my_str}")

# 按照"|"进行字符串分割，得到列表
my_list = new_my_str.split("|")
print(f"字符串{new_my_str}，按照|分隔后，得到：{my_list}")