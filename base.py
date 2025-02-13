import pygame
import time
import random

# initialize pygame
pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)

# define display dimensions
dis_width = 800
dis_height = 600

# create the display
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# define clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# define font
font_style = pygame.font.SysFont(None, 50)