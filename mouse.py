import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定螢幕
screen = pygame.display.set_mode((1920, 1080))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 獲取鼠標座標
    x, y = pygame.mouse.get_pos()
    print(f'鼠標座標: X: {x}, Y: {y}')

    # 更新螢幕
    screen.fill((255, 255, 255))
    pygame.display.flip()
