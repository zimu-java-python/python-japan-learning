"""
演示嵌套调用函数
"""

# 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a，并在内部调用func_b
def func_a():
    print("---1---")

    func_b()

    print("---3---")

# 调用函数func_a
func_a()
# 先执行a，执行过程中调用b的语句，会将b全部执行完成后，继续执行a的剩余内容
