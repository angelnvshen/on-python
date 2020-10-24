# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# print(10 / 0)

# message = "hello world "
# print(message.title()) # 单词第一个字母大写
# print(message.strip()) # 去除开头和结尾的空白
# # print "hello"  python2 语法
#
# print(100 ** 2) #乘方运算
# 100 * 10
# print(0.2 + 0.1)
# print(3 * 0.1)
# print(3 / 0.1)
# print(3 / 2)
#
# import this

# ========== 4: 列表 ==========
# ---- 4. 1 base operation----
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# # print(bicycles[5]) list index out of range
# print(bicycles[-1]) #访问最后一个列表元素提供了一种特殊语法
# bicycles[2] = bicycles[2] + "----"  # 修改
# bicycles.append('ducati')           # 添加
# # bicycles[6] = 'xxx' # 添加 error : list assignment index out of range
# bicycles.insert(0, "fducati")       #插入
# del bicycles[0]                     # 1. 使用del语句删除元素
# bicycles.pop()                      # 2. 使用方法pop()删除元素, 可删除列表末尾的元素
# bicycles.pop(0)                     # 3. 弹出列表中任何位置处的元素
# # bicycles.remove('redline')          # 4. 根据值删除元素 error : list.remove(x): x not in list
# bicycles.remove('redline----')      # 4. 根据值删除元素
# print(bicycles)

#  ---- sort ----
# bicycles.sort()
# print(bicycles)
# bicycles.sort(reverse=True)
# print(bicycles)
#  --
# print(sorted(bicycles)) # 临时排序
# print(len(bicycles))
# print(bicycles)

#  ---- 4.2 iterator ----
# for b in bicycles :
#     print(b)
#     print('-')  #  Python根据缩进来判断代码行与前一个代码行的关系

#  ---- 4. 3创建数值列表 ----
# for i in range(0, 10):
#     print(i)
#
# tmpList = list(range(0, 5));
# print(list(range(0, 5)))  # 使用range()创建数字列表
# 对数字列表执行简单的统计计算
# print(min(tmpList))
# print(max(tmpList))
# print(sum(tmpList))
# # 列表解析
# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

#  ---- 4.4 使用列表的一部分 ----
# print(squares[0: 3])
# print(squares[3:])
# print(squares[-3:])  # 负数索引返回离列表末尾相应距离的元素
# for num in squares[: 3]:
#     print(num)
#
# copyList = squares[:]
# print(copyList)
#  ---- 4.5 元组 ----
#  Python将不能修改的值称为不可变的，而不可变的列表被称为元组。
#  使用圆括号而不是方括号来标识
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
# dimensions = (10, 20)
# print(dimensions[0])
# dimensions = (400, 100)
# print(dimensions[0])

# ========== 5: IF ==========
# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw' and len(car) == 3:
#         print(car.upper())
#     else:
#         print(car.title())
#
# car = 'bmw'
# if car not in cars:
#     print(car)

# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")

# 确定列表不是空的
# if cars:
#     print(cars)

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for req in requested_toppings:
#     if req in available_toppings:
#         print("Adding " + req + ".")
#     else:
#         print("Sorry, we don't have " + req + ".")

# ========== 6: 字典 ==========
# alien_0 = {'color': 'green', 'point': 5}
# # print(alien_0['color'])
# print(alien_0)
# alien_0['color'] = 'yellow'
# alien_0['x_position'] = 20
# del alien_0['point']
# print(alien_0)
#
# for key, value in alien_0.items():
#     print(str(key) + " - " + str(value))

# ========== 7: input and while ==========
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

# print(10 % 3)

# cur = 1
# while cur < 5:
#     print(cur)
#     cur += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# ========== 8: 函数 ==========
# def greet_user():
#     """显示简单的问候语"""
#     print('hello')
#
# greet_user()

# def describe_pet(animal_type='dog', pet_name=''):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet()
# # 一条名为Willie的小狗
# describe_pet('willie')
# describe_pet(pet_name='willie')
# # 一只名为Harry的仓鼠
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# def modifyList(infoList):
#     infoList.append('xx')
#     return infoList
#
#
# car = ['bma', 'audi']
# car2 = modifyList(car)
# print(car)
# print(car2)
#
# car2 = modifyList(car[:]) # 禁止函数修改列表, 可向函数传 递列表的副本而不是原件
# print(car)
# print(car2)

# 任意数量实参
# def make_pizza(size, *toppings):
#     """打印顾客点的所有配料"""
#     print("\nMaking a " + str(size) +
#           "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(topping)
#
#
# make_pizza(10, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 将函数编写成能够接受任意数量的键—值对
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#
#     return profile
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton',
#                              field='physics')
# print(user_profile)

# 将函数存储在模块中
# 8.6.1 导入整个模块
# 如果你使用这种import语句导入了名为module_name.py的整个模块，就可使 用下面的语法来使用其中任何一个函数:
# module_name.function_name()
# import pizza
#
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.6.2 导入特定的函数
# 还可以导入模块中的特定函数，这种导入方法的语法如下:
# from module_name import function_name
# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数:
# from module_name import function_0, function_1, function_2
# from pizza import make_pizza
#
# make_pizza(16, 'pepperoni')
#
# # 8.6.3 使用as给函数指定别名
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
#
# # 8.6.4 使用as给模块指定别名
# import pizza as p
# p.make_pizza(16, 'pepperoni')
#
# # 8.6.5 导入模块中的所有函数 使用星号(*)运算符可让Python导入模块中的所有函数:
# from pizza import *
#
# make_pizza(16, 'pepperoni')

# ========== 9: 类 ==========
# from dog import *
#
# my_dog = Dog('tom', 6)
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.roll_over()

# ========== 10: 文件和异常 ==========
# Python在当前执行的文件所在的目录中查找指定的文件。
# with open("pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents)
