import pygame

pygame.init()

WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
BORDER_THICKNESS = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND_COLOR = pygame.Color("black")
SNAKE_COLOR = pygame.Color("green")
HEAD_COLOR = pygame.Color("yellow")
BORDER_COLOR = pygame.Color("red")

snake_x = int(WIDTH / 2)
snake_y = int(HEIGHT / 2)
snake_body = [(snake_x, snake_y)]  

move_x = 0
move_y = 0

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_x = 0
                move_y = -GRID_SIZE
            if event.key == pygame.K_s:
                move_x = 0
                move_y = GRID_SIZE
            if event.key == pygame.K_a:
                move_x = -GRID_SIZE
                move_y = 0
            if event.key == pygame.K_d:
                move_x = GRID_SIZE
                move_y = 0

    snake_x += move_x
    snake_y += move_y

    if snake_x < BORDER_THICKNESS or snake_x >= WIDTH - BORDER_THICKNESS or snake_y < BORDER_THICKNESS or snake_y >= HEIGHT - BORDER_THICKNESS:
        running = False  

    snake_body.append((snake_x, snake_y))  

    if len(snake_body) > 5:  
        snake_body.pop(0)

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, WIDTH, BORDER_THICKNESS))  
    pygame.draw.rect(screen, BORDER_COLOR, (0, HEIGHT - BORDER_THICKNESS, WIDTH, BORDER_THICKNESS))  
    pygame.draw.rect(screen, BORDER_COLOR, (0, 0, BORDER_THICKNESS, HEIGHT))  
    pygame.draw.rect(screen, BORDER_COLOR, (WIDTH - BORDER_THICKNESS, 0, BORDER_THICKNESS, HEIGHT))  

    for x, y in snake_body[:-1]:  
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, HEAD_COLOR, (snake_x, snake_y, GRID_SIZE, GRID_SIZE))  

    pygame.display.update()

    clock.tick(30)

pygame.quit()
