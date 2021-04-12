import pygame
import random
import time

pygame.init()

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen
WIDTH = 400
HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# Background
BACKGROUND = pygame.image.load("AnimatedStreet.png")

# FPS
FPS = 60
timer = pygame.time.Clock()

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

COINS = 0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface(self.image.get_size())

        center = (WIDTH // 2, HEIGHT - self.image.get_height() // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 300

    def move(self):
        pixels_per_frame = self.speed // FPS
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-pixels_per_frame, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(pixels_per_frame, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2),
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 600

    def move(self):
        global score
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            score += 1
            center = (random.randint(self.width // 2, WIDTH - self.width // 2),
                      -self.height // 2)
            self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(center=(random.randint(40, WIDTH - 40), 0))

        self.speed = 600

    def move(self):
        self.rect.move_ip(0, 4)
        global COINS
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
        if pygame.sprite.spritecollideany(player1, enemies2):
            pygame.mixer.Sound('./  rune.wav').play()
            COINS += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)


# Creating our own event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
cnt = 0
enemy1 = Enemy()
player1 = Player()
coin1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(enemy1)
enemies2 = pygame.sprite.Group()
enemies2.add(coin1)
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(enemy1)
all_sprites.add(coin1)

game_done = False
while not game_done:
    score = 0
    done = False
    while not done:
        timer.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                game_done = True

        if pygame.sprite.spritecollideany(player1, enemies):
            pygame.mixer.Sound('w10_crash.wav').play()
            DISPLAYSURF.fill(RED)
            txt_rect = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            DISPLAYSURF.blit(game_over, txt_rect)
            pygame.display.flip()
            choosen = False
            while not choosen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_done = True
                        choosen = True
                    if event.type == pygame.KEYDOWN:
                        choosen = True
                        if event.key == pygame.K_SPACE:
                            game_done = True
            done = True

        DISPLAYSURF.blit(BACKGROUND, (0, 0))

        scores = font_small.render('Score: ' + str(score), True, BLACK)
        DISPLAYSURF.blit(scores, (10, 10))
        coinsss = font_small.render('Coins: ' + str(COINS), True, BLACK)
        DISPLAYSURF.blit(coinsss, (300, 10))

        for entity in all_sprites:
            DISPLAYSURF.blit(entity.image, entity.rect)
            entity.move()

        pygame.display.flip()

pygame.quit()