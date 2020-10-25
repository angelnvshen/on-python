#  装饰器

# def fun():
#     a = 100
#
#     def inner_fun():
#         b = 99
#         print(a, b)
#
#     return inner_fun
#
#
# #  内部函数 的引用
# '''
# 闭包
# 1：外部函数中定义了内部函数
# 2：外部函数有返回值
# 3：返回值是 内部函数名
# 4：内部函数引用外部函数的变量
# '''
# x = fun()
#
# print(x)
# x()
#
#
# def decorate(fun):
#     a = 100
#
#     def wrapper(*args, **kwargs):  # 多个参数，关键字参数 |（）， {}
#         print("--------> start ")
#         fun(*args, **kwargs)
#         print("--------> end " + str(a))
#
#     return wrapper
#
#
# # decorate(fun2)()
#
# # 装饰
# @decorate
# def fun2():
#     print(" ===  ")
#
#
# fun2()
#
#
# @decorate
# def fun3(num, clazz='xx'):
#     print(num, clazz)
#
#
# fun3(4, clazz='yy')

# 装饰器多层
'''
多层装饰器，先执行最靠近函数的装饰函数
装饰器带参数，相当于在加一层嵌套，传入装饰器的参数
'''


# def decOne(fun):
#     print("----- decOne start ----")
#
#     def wrapper(*args, **kwargs):
#         print("--- 粉刷")
#         fun(*args, **kwargs)
#
#     print("----- decOne end ----")
#
#     return wrapper
#
#
# def decTwo(fun):
#     print("----- decTwo start ----")
#
#     def wrapper(*args, **kwargs):
#         print("--- 铺地板")
#         fun(*args, **kwargs)
#
#     print("----- decTwo end ----")
#
#     return wrapper
#
#
# @decTwo
# @decOne
# def house():
#     print("毛坯房")
#
#
# house();

# def outter(a):
#     def decorate(fun):
#         def wrapper(*args, **kwargs):
#             fun()
#             print("-- 铺地砖{}块 --".format(a))
#
#         return wrapper
#
#     return decorate
#
#
# @outter(100)
# def street():
#     print("新街道 --- ")
#
#
# street()
