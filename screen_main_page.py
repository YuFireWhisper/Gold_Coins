import pygame
import sys

# 初始化
pygame.init()

# 背景圖
background = 'img/board.png'

class ScreenSetting:
    def __init__(self, screenInfo):

        # 設定視窗(全螢幕)
        self.screen = pygame.display.set_mode((screenInfo.current_w, screenInfo.current_h), pygame.FULLSCREEN)
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (screenInfo.current_w, screenInfo.current_h))

        self.fps = 60
        self.clock = pygame.time.Clock()

    def quit(self):
        pygame.quit()
        sys.exit()