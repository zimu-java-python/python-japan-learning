"""
列表的下标索引
"""

"""
列表中的每一个元素都有其位置下标索引，顺序从前往后，从0开始依次递增
"""

# 语法：列表[下标索引]
my_list = ["tom","lily","rose"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 错误示范：通过下标索引去数据，一定不要超出范围
# print(my_list[3])

# 列表的下标索引-反向（最后一个元素为-1，从后往前依次递减）
my_list = ["tom","lily","rose"]
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 嵌套列表的下标索引
my_list = [[1,2,3],[4,5,6]]
print(my_list[0][0])
print(my_list[1][0])
print(my_list[-1][-1])
print(my_list[-2][-1])
