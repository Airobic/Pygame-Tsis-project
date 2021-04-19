import pygame, sys, time, random
from random import randrange
difficulty = 25

# Window size
frame_size_x = 720
frame_size_y = 480


# Checks for errors encountered
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 10]]

food_pos = [random.randrange(30, (frame_size_x//10)) * 10 - 50, random.randrange(30, (frame_size_y//10)) * 10 - 50]
food_spawn = True


direction = 'RIGHT'
change_to = direction

score = 0
font1 = pygame.font.SysFont('consolas', 20)
# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('GAME OVER', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    all_score = font1.render('Second score: ' + str(snake.score), True, red)
    game_window.blit(all_score, (frame_size_x/2 - 50, frame_size_y /4 + 300))
    pygame.display.flip()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10 + 10, 40)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
def is_in_walls():
    if snake_pos[0] < 30 or snake_pos[0] > frame_size_x - 40:
        game_over()
    if snake_pos[1] < 30 or snake_pos[1] > frame_size_y - 40:
        game_over()
    if snake.elements[0][0] > frame_size_x-40 or snake.elements[0][0] < 30:
        game_over()
wall_image = pygame.image.load('brickwall.png')
# def is_in_walls2():
#     return snake.elements[0][0] > frame_size_x-40 or snake.elements[0][0] < 30
def show_walls():
    for i in range(0,frame_size_x, 15):
        game_window.blit(wall_image,(i,0))
        game_window.blit(wall_image,(i,frame_size_y - 30))
        game_window.blit(wall_image,(0,i))
        game_window.blit(wall_image, (frame_size_x - 30, i))
# Main logic
class Snake():
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.elements = [[100,100],[120,100],[140,100]]
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(game_window, pygame.Color('green'), element, self.radius)
    def add_snake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0,0])
        self.is_add = False
    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
snake = Snake()
def show_score2(x,y,score):
    show = font1.render('Score2: ' + str(score), True, pygame.Color('orange'))
    game_window.blit(show, (x,y))
def colsision():
    if (food.x in range(snake.elements[0][0] - 20, snake.elements[0][0]) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1]))):
        snake.is_add = True
        food.x = random.randint(50, frame_size_x - 50)
        food.y = random.randint(50, frame_size_y - 50)
class Food:
    def __init__(self):
        self.x = random.randint(50, frame_size_x - 50)
        self.y = random.randint(50, frame_size_y - 50)
        self.image = pygame.image.load('pizza.png')
        # self.position = [random.randint(0, frame_size_x-100), random.randint(0,frame_size_y - 100  )]
    def draw(self):
        game_window.blit(self.image, (self.x, self.y))
food = Food()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_w:
                snake.dx = 0
                snake.dy = -5
            if event.key == pygame.K_s:
                snake.dx = 0
                snake.dy = 5
            if event.key == pygame.K_a:
                snake.dx = -5
                snake.dy = 0
            if event.key == pygame.K_d:
                snake.dx = 5
                snake.dy = 0
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # if is_in_walls2():
    #     game_over()
    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # eating snake
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(30, (frame_size_x//10))*10-50, random.randrange(30, (frame_size_y//10))*10-50]
    food_spawn = True

    # snake
    game_window.fill(pygame.Color('blue'))
    for pos in snake_body:
        # Snake body
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    colsision()
    show_walls()
    is_in_walls()
    snake.move()
    snake.draw()
    food.draw()
    show_score2(35,65, snake.score)
    pygame.display.update()
    fps_controller.tick(difficulty)