import pygame
import ctypes
import numpy as np
from field import Board


WHITE = (255,255,255)
BLACK = (0,0,0)
SMOKE_WHITE = 0xD7DBDC
DARK_GREY = 0x3C3F41
VERY_DARK_GREY = 0x2B2B2B

Chess_Board = Board()

screen = pygame.display.set_mode((Chess_Board.board_length, Chess_Board.board_length))

king_img_raw = pygame.image.load("../figure_pictures/white_king.png")
king_img = pygame.transform.scale(king_img_raw, (80,80))

def FieldCoordinates(square: str) -> list:
    #Get the position in the Board array from the given square name
    arr_pos = np.where(Chess_Board.field['name'] == square)

    if not arr_pos[0] and not arr_pos[1]:
        print('Field not found')
        raise ValueError
    else:
        #get the x and y coordinates with from the given square name
        x = Chess_Board.field['x'] [arr_pos[0].item(0)] [arr_pos[1].item(0)]
        y = Chess_Board.field['y'] [arr_pos[0].item(0)] [arr_pos[1].item(0)]
        return [x, y]



def Main():
    pygame.init()

    pygame.display.set_caption('Chess.jaeggli')
    CLOCK = pygame.time.Clock()

    while True:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        screen.fill(VERY_DARK_GREY)
        DrawGrid()
        coordinates = FieldCoordinates('A4')
        x = coordinates[0]
        y = coordinates[1]
        screen.blit(king_img, (x,y))

        pygame.display.update()


def DrawGrid():
    BOARD_SIZE = Chess_Board.board_length
    rectangle_width = BOARD_SIZE / Chess_Board.board_square_number
    rectangle_height = rectangle_width

    for y in range (1, BOARD_SIZE + 1):
        for x in range(1, BOARD_SIZE + 1):
            if y % 2 == 1 and x % 2 == 1:
                pygame.draw.rect(screen, SMOKE_WHITE, [rectangle_width * (x - 1), rectangle_height * (y - 1), rectangle_width, rectangle_height])
            elif y % 2 == 0 and x % 2 == 0:
                pygame.draw.rect(screen, SMOKE_WHITE, [rectangle_width * (x - 1), rectangle_height * (y - 1), rectangle_width, rectangle_height])



Main()