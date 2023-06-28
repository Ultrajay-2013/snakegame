import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode([500,500])
clock = pygame.time.Clock()
fps = 60

snake = [[pygame.image.load("snakhead.png"),pygame.Rect([240, 240], [20, 20])]]
food = [pygame.image.load("fodd.png"),pygame.Rect([randint(0,480),randint(0,480)], [20, 20])]
x_change = 0
y_change = 0
addlength = False
direction = None

green = (0, 175, 0)
isRunning = True
while isRunning:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != "down":
                direction = "up"
            if event.key == pygame.K_a and direction != "right":
                direction = "left"
            if event.key == pygame.K_s and direction != "up":
                direction = "down"
            if event.key == pygame.K_d and direction != "left":
                direction = "right"
    screen.fill(green)
    screen.blit(food[0],food[1])
    for s in snake:
        if direction == "up":
            s[1].x += 0
            s[1].y += -5
        if direction == "left":
            s[1].x += -5
            s[1].y += 0
        if direction == "down":
            s[1].x += 0
            s[1].y += 5
        if direction == "right":
            s[1].x += 5
            s[1].y += 0
        if s[1].x > 485:
            s[1].x = 0
        if s[1].x < 0:
            s[1].x = 485
        if s[1].y > 485:
            s[1].y = 0
        if s[1].y < 0:
            s[1].y = 485
        screen.blit(s[0],s[1])
    if snake[0][1].colliderect(food[1]):
        food[1].x = randint(0, 480)
        food[1].y = randint(0, 480)
        addlength = True
    if addlength == True:
        lengthosnake = len(snake)
        if direction == "up":
            snake.append([pygame.image.load("snakboody.png"),pygame.Rect([snake[lengthosnake-1][1].x,snake[lengthosnake-1][1].y+20], [20, 20])])
        if direction == "down":
            snake.append([pygame.image.load("snakboody.png"),pygame.Rect([snake[lengthosnake-1][1].x,snake[lengthosnake-1][1].y-20], [20, 20])])
        if direction == "left":
            snake.append([pygame.image.load("snakboody.png"),pygame.Rect([snake[lengthosnake-1][1].x+20,snake[lengthosnake-1][1].y], [20, 20])])
        if direction == "right":
            snake.append([pygame.image.load("snakboody.png"),pygame.Rect([snake[lengthosnake-1][1].x-20,snake[lengthosnake-1][1].y], [20, 20])])
        addlength = False
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
quit()