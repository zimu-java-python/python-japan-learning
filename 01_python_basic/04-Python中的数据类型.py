# 方式1：在print语句中用type()语句直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(13.14))

# 方式2：用变量存储type()语句的结果（返回值 ）
string_type = type("黑马程序员")
int_type = type(666)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)

# 方式3：type()可以查看变量中存储的数据类型
name = "黑马程序员"
name_type = type(name)
print(name_type)
