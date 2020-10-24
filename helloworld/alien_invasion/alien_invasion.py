import sys
import pygame

# 12.3.1-2 创建Pygame窗口以及响应用户输入
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     screen = pygame.display.set_mode((1200, 800))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 设置背景色
#     bg_color = (230, 230, 230)
#
#     # 开始游戏的主循环
#     while True:
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 sys.exit()
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()

# 12.3.3-4
# 创建设置类, 提取公共组件配置信息
# 在屏幕上绘制飞船

from settings import Settings
from ship import Ship
#
#
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#         # 监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if (event.type == pygame.QUIT):
#                 sys.exit()
#
#         # 每次循环时都重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
#
#         # 让最近绘制的屏幕可见
#         pygame.display.flip()
#
#
# run_game()

# 12.5 重构:模块game_functions
import game_functions as gf

# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     ship = Ship(screen)
#
#     # 开始游戏的主循环
#     while True:
#         # 响应按键和鼠标事件
#         gf.check_events()
#
#         # 每次循环时都重绘屏幕
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()

# 12.6 驾驶飞船
# def run_game():
#     # 初始化游戏并创建一个屏幕对象
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(
#         (ai_settings.screen_width, ai_settings.screen_height))
#     pygame.display.set_caption("Alien Invasion")
#
#     # 创建一艘飞船
#     # ship = Ship(screen)
#     # 12.6.4调整飞船的速度
#     ship = Ship(ai_settings, screen)
#
#     # 开始游戏的主循环
#     while True:
#         # 响应按键和鼠标事件
#         gf.check_events(ship)
#
#         # 更新飞船位置
#         ship.update()
#
#         # 每次循环时都重绘屏幕
#         gf.update_screen(ai_settings, screen, ship)
#
#
# run_game()

# 12.8.3 将子弹存储到编组中
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    # ship = Ship(screen)
    # 12.6.4调整飞船的速度
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        # 响应按键和鼠标事件
        gf.check_events(ship)

        # 更新飞船位置
        ship.update()

        bullets.update()

        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings, screen, ship)


run_game()
