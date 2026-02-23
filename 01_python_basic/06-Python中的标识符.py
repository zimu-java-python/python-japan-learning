# 规则1：内容限定，限定只能使用（英文，中文，数字，下划线_）,注意：不能以数字作为开头

# 错误的代码示范；1_name = "张三"
# 错误的代码示范：name_! = "张三"
name_ = "张三"
_name = "张三"
name_1 = "张三"
print(name_)
print(_name)
print(name_1)

# 规则2：大小写敏感

Itheima = "黑马程序员"
itheima = "666"
print(Itheima)
print(itheima)

# 规则3：不可使用关键字

# 错误的代码示范：class = 1
# 错误的代码示范：def = 1
Class = 1
print(Class)

# 规范

"""
变量名的命名规范
-1：见名知意
-2：多个单词组合变量名，要使用下划线做分隔
-3：英文字母全小写
"""

# 1
name = "张三"
age = 11
print(name)
print(age)
# 2
first_number = 1
student_nickname = "小明"
print(first_number)
print(student_nickname)
# 3
name_1 = "张三"
age_1 = 11
print(name_1)
print(age_1)
