import pygame
from random import randrange

# Game window

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640


# Snake

snake_direction = 'RIGHT'
snake_head = [100, 50]
snake_body = [
    snake_head,
    [snake_head[0] - 10, snake_head[1]],
    [snake_head[0] - 20, snake_head[1]],

]

def snake_change_direction(new_snake_direction: str):
    global snake_direction
    if new_snake_direction == snake_direction:
        return
    if snake_direction == 'UP' and new_snake_direction == "DOWN":
        return
    if snake_direction == 'DOWN' and new_snake_direction == "UP":
        return
    if snake_direction == 'LEFT' and new_snake_direction == "RIGHT":
        return
    if snake_direction == 'RIGHT' and new_snake_direction == "LEFT":
        return
    snake_direction = new_snake_direction


def snake_move():
    global snake_direction, snake_head, snake_body
    if snake_direction == "UP":
        snake_head = [snake_head[0], snake_head[1] + 10]
    elif snake_direction == "DOWN":
        snake_head = [snake_head[0], snake_head[1] - 10]
    elif snake_direction == "RIGHT":
        snake_head = [snake_head[0] + 10, snake_head[1]]
    elif snake_direction == "LEFT":
        snake_head = [snake_head[0] - 10, snake_head[1]]
    snake_body.insert(0, snake_head)
    snake_body.pop()


def snake_grown():
    global snake_head, snake_body
    snake_body.insert(0, snake_head)
    snake_move()


# Food

food = [200, 200]

def food_respawn():
    global food
    food = [randrange((1, WINDOW_WIDTH // 10) * 10), randrange((1, WINDOW_HEIGHT // 10) * 10)]


# Score

score = 0

def increase_score():
    global score
    score += 10


# Game logic

def game_over():
    global snake_head, snake_body
    # Conditions:
    # Head hits the border of the screen
    if snake_head[0] < 0 or snake_head[0] > WINDOW_WIDTH:
        print("GAME OVER")
    elif snake_head[1] < 0 or snake_head[1] > WINDOW_HEIGHT:
        print("GAME OVER")
    # Snake hits it's own body
    for block in snake_body[1:]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            print("GAME OVER")
