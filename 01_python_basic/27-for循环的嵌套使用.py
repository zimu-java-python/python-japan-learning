"""
演示for循环的嵌套使用
"""

x = 1

for x in range(1,101):
    print(f"今天是向小美表白的第{x}天")
    for j in range(1,11):
        print(f"送给小美的第{j}朵玫瑰花")
    print(f"小美，我喜欢你（第{x}天的表白结束）")

print(f"第{x}天，表白成功")
