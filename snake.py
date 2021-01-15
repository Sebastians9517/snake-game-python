from random import randrange
import pygame


# Game window

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640


# Colors

SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
FONT_COLOR = (255, 255, 255)


# Difficulty settings
DIFFICULTY = {
    'easy': 10,
    'medium': 25,
    'hard': 40
}

game = pygame
fps = pygame.time.Clock()
window = None


def init_game():
    global game, window
    game.init()
    game.display.set_caption('Snake')
    window = game.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    window.blit()


def draw_stage():
    window.fill(BACKGROUND_COLOR)

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
        snake_head = [snake_head[0], snake_head[1] - 10]
    elif snake_direction == "DOWN":
        snake_head = [snake_head[0], snake_head[1] + 10]
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


def draw_snake():
    global game, snake_body
    for part in snake_body:
        game.draw.rect(window, SNAKE_COLOR, game.Rect(part[0, part[1]], 10, 10)

# Food

food=[200, 200]

def food_respawn():
    global food
    food=[randrange((1, WINDOW_WIDTH // 10) * 10),
                    randrange((1, WINDOW_HEIGHT // 10) * 10)]

def draw_food():
    global game, food
    for part in snake_body:
        game.draw.rect(window, FOOD_COLOR, game.Rect(food[0], food[1], 10, 10))


# Score

score=0

def increase_score():
    global score
    score += 10

def draw_score():
    global game, score
    SCORE_FONT=game.font.SysFont('Times New Roman', 20)
    score_surface=SCORE_FONT.render('Score: {score}', True, FONT_COLOR)
    score_rect=score_surface.get_rect()
    score_rect.midtop=(WINDOW_WIDTH // 2, 15)
    window.blit(score_surface, score_rect)


# Game logic

def game_over():
    global snake_head, snake_body
    # Conditions:
    # Head hits the border of the screen
    if snake_head[0] < 0 or snake_head[0] > WINDOW_WIDTH:
        draw_game_over()
    elif snake_head[1] < 0 or snake_head[1] > WINDOW_HEIGHT:
        draw_game_over()
    # Snake hits it's own body
    for block in snake_body[1:]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            draw_game_over()

def draw_game_over():
    global game, score
    SCORE_FONT=game.font.SysFont('Times New Roman', 60)
    score_surface=SCORE_FONT.render(f'GAME OVER', True, FOOD_COLOR)
    window.fill(BACKGROUND_COLOR)
    score_rect=score_surface.get_rect()
    score_rect.midtop=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
    window.blit(score_surface, score_rect)


def exit_game():
    global game
    game.quit()
    sys.exit()


def turn()
    global snake_head, food
    snake_move()
    if snake_head[0] == food[0]

def run():
    global fps
    init_game()

    while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            exit_game()
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE:
                exit_game()
            else:
                if event.key == game.K_DOWN or event.key == game.K_s:
                    snake_change_direction('DOWN')
                if event.key == game.K_UP or event.key == game.K_w:
                    snake_change_direction('UP')
                if event.key == game.K_LEFT or event.key == game.K_a:
                    snake_change_direction('LEFT')
                if event.key == game.K_RIGHT or event.key == game.K_d:
                    snake_change_direction('RIGHT')
    draw_snake()
    snake_move()

    draw_snake()
    draw_food()
    draw_score()
    game.display.update()
    fps.tick(DIFFICULTY['easy'])
    sleep(5)

run()
