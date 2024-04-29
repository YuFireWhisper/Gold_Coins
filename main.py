"""接金幣遊戲專案"""

import pygame
from screen_main_page import ScreenSetting
from coin import Game
from player import Player

# 初始化
pygame.init()

# 新增screen_setting
screen_main = ScreenSetting(pygame.display.Info())

# 初始化角色
player = Player(pygame.display.Info())

# 金幣列表
coins = []

while True:

    # 事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            screen_main.quit()

    # 玩家移動
    if event.type == pygame.KEYDOWN:
        player.update()

    # 生成金幣
    if pygame.time.get_ticks() % 100 == 0:
        coin = Game(pygame.display.Info())
        coins.append(coin)

    # 更新金幣
    for coin in coins:
        if coin.update():
            coins.remove(coin)

    # 背景
    screen_main.screen.blit(screen_main.background, (0, 0))

    # 繪製金幣
    for coin in coins:
        screen_main.screen.blit(coin.coin, coin.coin_rect)

    # 繪製玩家
    screen_main.screen.blit(player.player, player.player_rect)

    screen_main.clock.tick(screen_main.fps)
    pygame.display.update()
