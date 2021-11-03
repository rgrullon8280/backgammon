import pygame
from pygame.event import get
from game.constants import BAR_WIDTH, LEFT_BOARD_MAX_X, RIGHT_BOARD_MIN_X, SIZE, TOP_ROW_MAX_HEIGHT, TOP_ROW_MIN_HEIGHT, WIDTH, HEIGHT
from game.game import Game
from typing import Tuple

FPS:int = 60
WIN:pygame.Surface = pygame.display.set_mode(SIZE)

def get_coor_from_mouse_click(pos:Tuple[float, float]):
    x, y = pos
    if x > LEFT_BOARD_MAX_X and x<RIGHT_BOARD_MIN_X:
        pass
    elif x>RIGHT_BOARD_MIN_X:
        if y < TOP_ROW_MAX_HEIGHT:
            return 18+int((x-RIGHT_BOARD_MIN_X)/((WIDTH-RIGHT_BOARD_MIN_X)/6))
        elif y > TOP_ROW_MIN_HEIGHT:
            return int((WIDTH-x)/((WIDTH-RIGHT_BOARD_MIN_X)/6))
    else:
        if y < TOP_ROW_MAX_HEIGHT:
            return 12 + int(x/(LEFT_BOARD_MAX_X/6))
        elif y > TOP_ROW_MIN_HEIGHT:
            return 6+int((LEFT_BOARD_MAX_X - x)/(LEFT_BOARD_MAX_X/6))

def main():
    running:bool = True
    clock:pygame.time.Clock = pygame.time.Clock()
    game:Game = Game(WIN)
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                point = get_coor_from_mouse_click(pygame.mouse.get_pos())
                game.select(point)
             
            game.update()


if __name__ == '__main__':
    main()
