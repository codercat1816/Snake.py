import pygame
import random
from settings import *
from utils import show_score, game_over

def main():
    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption("Snake-az")
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake
    # body
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    # fruit position
    fruit_position = [
        random.randrange(1, (window_x // 10)) * 10,
        random.randrange(1, (window_y // 10)) * 10,
    ]
    fruit_spawn = True

    # setting default snake direction
    # towards right
    direction = "RIGHT"
    change_to = direction

    # initial score
    score = 0

    # Main Function
    while True:
        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                if event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                if event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                if event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        # If two keys pressed simultaneously
        # we don't want snake to move into two directions
        # simultaneously
        if change_to == "UP" and direction != "DOWN":
            direction = "UP"
        if change_to == "DOWN" and direction != "UP":
            direction = "DOWN"
        if change_to == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change_to == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"

        # Moving the snake
        if direction == "UP":
            snake_position[1] -= 10
        if direction == "DOWN":
            snake_position[1] += 10
        if direction == "LEFT":
            snake_position[0] -= 10
        if direction == "RIGHT":
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores will be
        # incremented by 10
        snake_body.insert(0, list(snake_position))
        if (
            snake_position[0] == fruit_position[0]
            and snake_position[1] == fruit_position[1]
        ):
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [
                random.randrange(1, (window_x // 10)) * 10,
                random.randrange(1, (window_y // 10)) * 10,
            ]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(
            game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10)
        )

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over(game_window, score, window_x, window_y, red)
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over(game_window, score, window_x, window_y, red)

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(game_window, score, window_x, window_y, red)

        # displaying score continuously
        show_score(game_window, score, 1, white, "arial", 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)

if __name__ == "__main__":
    main()