import pygame
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

# define the player snake function that draws the snake on the screen
def player_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])

# define the message function, which displays a message onto the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 6, dis_height / 3])

# define the main game function
def gameLoop():
    # initially set the game_over variable as false
    game_over = False
    # initially set the game_close variable as false
    game_close = False

    # set the x1 variable as half of the screen width
    x1 = dis_width / 2
    # set the y1 variable as half of the screen height
    y1 = dis_height / 2

    # set the change of x1 and y1 as 0
    x1_change = 0
    y1_change = 0

    # set the snake list as a list
    snake_List = []
    # initially set the length of the snake body as 1
    Length_of_snake = 1

    # set the position of the food at a random position in the screen
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # when the player lost the game
        while game_close == True:
            # set the screen to black
            display.fill(black)
            # display a message asking for player input
            message("You lost! Press Q-Quit or C-Play Again", white)
            # display the message
            pygame.display.update()

            # listen for player input
            for event in pygame.event.get():
                # when the player presses a specific key
                if event.type == pygame.KEYDOWN:
                    # if the player presses the q key
                    if event.key == pygame.K_q:
                        # set game_over as true
                        game_over = True
                        # set game_close as false
                        game_close = False
                    # if the player presses the c key
                    if event.key == pygame.K_c:
                        # call the gameLoop function again
                        gameLoop()

        # listen for player input during gameplay
        for event in pygame.event.get():
            # if the player quits, set game_over true
            if event.type == pygame.QUIT:
                game_over = True
            # if the player presses a specific key
            if event.type == pygame.KEYDOWN:
                # if the player presses left, move the snake left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                # if the player presses right, move the snake right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                # if the player presses up, move the snake up
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                # if the player presses down, move the snake down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # if the snake hits the screen edge
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            # set the game_close variable as True prompting if the player wants to play again
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        # fill the screen background as black
        display.fill(black)
        # set the snake and food as white
        pygame.draw.rect(display, white, [foodx, foody, snake_block, snake_block])
        # initialize the snake head as a list
        snake_Head = []
        # handles the position of the snake head during gameplay
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # if the snake head hits its body, prompt the player if they want to play again
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # draws the snake
        player_snake(snake_block, snake_List)

        # update the display
        pygame.display.update()

        # if the snake eats the food, randomize the next location of the food, increase the length of the snake body
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    # quits the game
    pygame.quit()
    quit()

# calls the gameLoop function to start the game
gameLoop()