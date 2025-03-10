import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20
BORDER_THICKNESS = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BACKGROUND_COLOR = pygame.Color("black")
SNAKE_COLOR = pygame.Color("green")
HEAD_COLOR = pygame.Color("yellow")
FOOD_COLOR = pygame.Color("red")
BORDER_COLOR = pygame.Color("white")
TEXT_COLOR = pygame.Color("white")

snake_x = 200
snake_y = 200

move_x = GRID_SIZE
move_y = 0

food_x = random.randint(1, 19) * GRID_SIZE
food_y = random.randint(1, 19) * GRID_SIZE

score = 0
clock = pygame.time.Clock()
running = True

snake_body_x = [200 - GRID_SIZE, 200, 200 + GRID_SIZE]
snake_body_y = [200, 200, 200]

font = pygame.font.Font(None, 30)

while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and move_y == 0:
                move_x = 0
                move_y = -GRID_SIZE
            if event.key == pygame.K_s and move_y == 0:
                move_x = 0
                move_y = GRID_SIZE
            if event.key == pygame.K_a and move_x == 0:
                move_x = -GRID_SIZE
                move_y = 0
            if event.key == pygame.K_d and move_x == 0:
                move_x = GRID_SIZE
                move_y = 0

    snake_x = snake_x + move_x
    snake_y = snake_y + move_y

    if snake_x < BORDER_THICKNESS or snake_x > WIDTH - BORDER_THICKNESS - GRID_SIZE or snake_y < BORDER_THICKNESS or snake_y > HEIGHT - BORDER_THICKNESS - GRID_SIZE:
        print("You Lose! Final Score:", score)
        running = False  

    if snake_x == food_x and snake_y == food_y:
        score = score + 1
        food_x = random.randint(1, 19) * GRID_SIZE
        food_y = random.randint(1, 19) * GRID_SIZE
    else:
        snake_body_x.pop(0)
        snake_body_y.pop(0)

    snake_body_x.append(snake_x)
    snake_body_y.append(snake_y)

    if score == 5:
        print("You Win! Final Score:", score)
        running = False

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, WIDTH, BORDER_THICKNESS))  
    pygame.draw.rect(screen, BORDER_COLOR, (0, HEIGHT - BORDER_THICKNESS, WIDTH, BORDER_THICKNESS))  
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, BORDER_THICKNESS, HEIGHT))  
    pygame.draw.rect(screen, BORDER_COLOR, (WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, HEIGHT))  

    for i in range(len(snake_body_x) - 1):
        pygame.draw.rect(screen, SNAKE_COLOR, (snake_body_x[i], snake_body_y[i], GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, HEAD_COLOR, (snake_x, snake_y, GRID_SIZE, GRID_SIZE))  
    pygame.draw.rect(screen, FOOD_COLOR, (food_x, food_y, GRID_SIZE, GRID_SIZE))

    score_text = font.render("Score: " + str(score), True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(35)

pygame.quit()
