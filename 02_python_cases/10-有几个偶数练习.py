num = int(input("请输入一个数字："))
count = 0
count_1 = 0

for x in range(1,num):
    if x % 2 == 0:
        count += 1
    else:
        count_1 += 1

print(f"从1到{num}（不含{num}本身）范围内，有{count}个偶数。")
print(f"从1到{num}（不含{num}本身）范围内，有{count_1}个奇数。")
