import pygame
import random

# initialize pygame
pygame.init()

# define colors
white = (255, 255, 255)
gray = (137, 137, 137)
black = (0, 0, 0)

# define display dimensions
dis_width = 600
dis_height = 600
score_height = 50

# create the display
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# define clock
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 25

# define font
font_style = pygame.font.SysFont(None, 40)
# (V.2) define the font of the score board
score_font = pygame.font.SysFont(None, 35)

# define the player snake function that draws the snake on the screen
def player_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])

# define the message function, which displays a message onto the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 6, dis_height / 3])

# (V.2) define the score function
def show_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # border
    border_thickness = 2
    pygame.draw.rect(display, white, (x - border_thickness, y - border_thickness, w + 2 * border_thickness, h + 2 * border_thickness))

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "resume":
                return True
            elif action == "restart":
                gameLoop()
            elif action == "quit":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(display, ic, (x, y, w, h))

    smallText = pygame.font.SysFont(None, 20)
    textSurf = smallText.render(msg, True, white)
    display.blit(textSurf, (x + (w // 2 - textSurf.get_width() // 2), y + (h // 2 - textSurf.get_height() // 2)))

# (V.2) define a pause function
def pause_game():
    paused = True
    # setting the background of the pause screen to transparent
    overlay = pygame.Surface((dis_width, dis_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                #elif event.key == pygame.K_q:
                    #pygame.quit()
                    #quit()
                #elif event.key == pygame.K_c:
                    #gameLoop()

        display.blit(overlay, (0, 0))
        message("Paused", white)

        # Draw the buttons
        if button("Resume", 150, 400, 100, 50, black, gray, action="resume"):
            paused = False
        if button("Restart", 300, 400, 100, 50, black, gray, action="restart"):
            gameLoop()
        if button("Quit", 450, 400, 100, 50, black, gray, action="quit"):
            pygame.quit()
            quit()

        pygame.display.update()
        clock.tick(15)

# define the main game function
def gameLoop():
    # initially set the game_over variable as false
    game_over = False
    # initially set the game_close variable as false
    game_close = False

    # set the x1 variable as half of the screen width
    x1 = dis_width / 2
    # set the y1 variable as half of the screen height
    y1 = (dis_height + score_height) / 2

    # set the change of x1 and y1 as 0
    x1_change = 0
    y1_change = 0

    # set the snake list as a list
    snake_List = []
    # initially set the length of the snake body as 1
    Length_of_snake = 1

    # set the position of the food at a random position in the screen
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(score_height, dis_height - snake_block) / 10.0) * 10.0

    # (V.2) initialize the score as a value of 0
    score = 0
    
    while not game_over:

        # when the player lost the game
        while game_close == True:
            # set the screen to black
            display.fill(black)
            # display a message asking for player input
            message("You lost! Press Q-Quit or C-Play Again", white)
            # (V.2) show the score
            show_score(score)
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
                # (V.2) if the player presses ESC, pause the game
                elif event.key == pygame.K_ESCAPE:
                    pause_game()

        # if the snake hits the screen edge
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < score_height:
            # set the game_close variable as True prompting if the player wants to play again
            game_close = True
        
        x1 += x1_change
        y1 += y1_change

        x1 = round(x1 / 10.0) * 10.0
        y1 = round(y1 / 10.0) * 10.0

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
        # (V.2) show the score
        show_score(score)

        # update the display
        pygame.display.update()

        # if the snake eats the food, randomize the next location of the food, increase the length of the snake body
        if abs(x1 - foodx) < snake_block and abs(y1 - foody) < snake_block:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(score_height, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            # (V.2) add points to the player's score
            score += 100

        clock.tick(snake_speed)

    # quits the game
    pygame.quit()
    quit()

# calls the gameLoop function to start the game
gameLoop()

"""
Issues Risen
- After including the score safe area, the game is not operating correctly as when the snake reaches the food
  it does not eat the food and grows.

  > fixed by changing the if statement of the snake growth and food randomization, to use the absolute value
    of the difference between the location of the snake and the food.

- A visual bug is present when moving the snake horizontally to get the food. The snake appears to eat the food 
  at either a position above or below the food position. Getting food vertically is fine, just horizontally the
  visual is off. Was initially unsure if the issue is with the food or the snake.

  > Attempted to fix the bug for the food, through ensuring that the food is positioned in multiples of 10,
    however, the issue was not resolved. Decided to change the positioning of the snake movement to multiples
    of 10. This fixed the visual bug.
"""