"""
取出列表内的偶数
"""

def list_while_func():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    index = 0
    while index < len(num_list):
        element = num_list[index]
        if element % 2 == 0:
            new_list.append(element)
        index += 1
    print(f"通过while循环，从列表：{num_list}中取出偶数，组成新列表：{new_list}")


def list_for_func():
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_list = []
    for element in num_list:
        if element % 2 == 0:
            new_list.append(element)
    print(f"通过for循环，从列表：{num_list}中取出偶数，组成新列表：{new_list}")

list_while_func()
list_for_func()