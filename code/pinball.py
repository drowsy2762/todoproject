import pygame
import random
import math

# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pinball Game")

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 공 클래스
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, RED, [10, 10], 10)
        self.velocity = [random.randint(-5, 5), random.randint(-5, 5)]
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.x <= 0 or self.rect.x >= screen_width - 20:
            self.velocity[0] = -self.velocity[0]

        if self.rect.y <= 0 or self.rect.y >= screen_height - 20:
            self.velocity[1] = -self.velocity[1]

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([100, 20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > screen_width - 100:
            self.rect.x = screen_width - 100

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()

# 공과 패들 생성
ball = Ball()
all_sprites.add(ball)
balls.add(ball)

paddle = Paddle(screen_width // 2, screen_height - 30)
all_sprites.add(paddle)

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.spritecollide(paddle, balls, False):
        ball.velocity[1] = -ball.velocity[1]

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
