"""
序列的切片实践
"""

# 有字符串："万过薪月，员序程马黑来，nohtyp学"
# 得到"黑马程序员"
my_str = "万过薪月，员序程马黑来，nohtyp学"

# 方法1
result1 = my_str[::-1][9:14]
print(result1)

# 方法2
result2 = my_str[5:10][::-1]
print(result2)

# 方法3
result3 = my_str.split("，")[1].replace("来","")[::-1]
print(result3)