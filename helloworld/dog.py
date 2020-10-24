class Dog():  # 根据约定，在Python中，首字母大写的名称指的是类。 这个类定义中的括号是空的，因为我们要从空白创建这个类
    """一次模拟小狗的简单尝试"""

    # __init__()是一个特殊的方法，每当你根据Dog类创建新实 例时，Python都会自动运行它
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    # 每个与类相关联的方法 调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
