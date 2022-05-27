import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        # 将图片缩小显示在屏幕上
        # self.image = pygame.transform.scale(self.image, (50, 40))
        # 将图片旋转一个直角
        self.image = pygame.transform.rotate(self.image, -90)  
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕左部的中央
        self.rect.midleft = self.screen_rect.midleft

        # 在飞船的属性y中存储小数值
        self.y = float(self.rect.y)

        # 移动标志
        self.moving_down = False
        self.moving_up = False

    
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的y值
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # 根据self.y更新rect对象
        self.rect.y = self.y

    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """让飞船在屏幕左端居中"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)


