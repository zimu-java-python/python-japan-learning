"""
演示python中
if else的组合判断语句
"""

print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")

age = int(input("请输入你的年龄："))

if age >= 18:
    print("您已成年，游玩需要补票10元。")
else: # 和if同级
    print("您未成年，可以免费游玩。")

print("祝你游玩愉快。")
