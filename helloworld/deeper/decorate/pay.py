import time

isLogin = False


def login_require(fun):
    def wrapper(*args, **kwargs):
        global isLogin
        if isLogin:
            print("--------- 付款 --------")
            fun(*args, **kwargs)
        else:
            # 调转到登录页
            print("------ 用户未登录，不能付款 ------")
            isLogin = login()
            print("result", isLogin)

    return wrapper

def login():
    username = input("输入用户名：")
    password = input("输入密码：")
    if username == 'admin' and password == '123456':
        return True
    else:
        return False


@login_require
def pay(money):
    print("----- 准备付款 -------")
    time.sleep(2)
    print("----- 成功付款{} -------".format(money))


pay(100)
pay(200)
