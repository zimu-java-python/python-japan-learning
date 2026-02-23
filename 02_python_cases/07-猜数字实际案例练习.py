"""
定义一个数字（1~10，随机产生），通过3此判断来猜出数字
"""

# 构建一个随机的数字变量

import random
num = random.randint(1,10)
print(num)

guess_num = int(input("输入你要猜测的数字（1~10）:"))
if guess_num == num:
    print("恭喜你猜对了。")
else:
    if guess_num > num:
        print("您猜的数字大了")
    else:
        print("您猜的数字小了")

    guess_num = int(input("输入继续你要猜测的数字（1~10）:"))
    if guess_num == num:
        print("恭喜你猜对了。")
    else:
        if guess_num > num:
            print("您猜的数字大了")
        else:
            print("您猜的数字小了")

        guess_num = int(input("输入再次你要猜测的数字（1~10）:"))
        if guess_num == num:
            print("恭喜你猜对了。")
        else:
            if guess_num > num:
                print("您猜的数字大了")
            else:
                print("您猜的数字小了")
            print("抱歉，您三次都没有猜对，正确答案是：%d" % num)
