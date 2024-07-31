import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 10
PADDLE_SPEED = 5
BALL_SPEED = 5

# Font
FONT = pygame.font.SysFont(None, 35)

def draw_window(paddle1, paddle2, ball, score1, score2):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, paddle1)
    pygame.draw.rect(WIN, WHITE, paddle2)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    score_text = FONT.render(f"{score1} | {score2}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.update()

def main():
    paddle1 = pygame.Rect(30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle2 = pygame.Rect(WIDTH - 30 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    paddle1_vel = 0
    paddle2_vel = 0
    ball_vel = [BALL_SPEED, BALL_SPEED]

    score1 = 0
    score2 = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1_vel = -PADDLE_SPEED
        elif keys[pygame.K_s]:
            paddle1_vel = PADDLE_SPEED
        else:
            paddle1_vel = 0

        if keys[pygame.K_UP]:
            paddle2_vel = -PADDLE_SPEED
        elif keys[pygame.K_DOWN]:
            paddle2_vel = PADDLE_SPEED
        else:
            paddle2_vel = 0

        paddle1.y += paddle1_vel
        paddle2.y += paddle2_vel

        ball.x += ball_vel[0]
        ball.y += ball_vel[1]

        if paddle1.colliderect(ball) or paddle2.colliderect(ball):
            ball_vel[0] = -ball_vel[0]

        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel[1] = -ball_vel[1]

        if ball.left <= 0:
            score2 += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_vel = [BALL_SPEED, BALL_SPEED]

        if ball.right >= WIDTH:
            score1 += 1
            ball.x = WIDTH // 2 - BALL_SIZE // 2
            ball.y = HEIGHT // 2 - BALL_SIZE // 2
            ball_vel = [-BALL_SPEED, BALL_SPEED]

        draw_window(paddle1, paddle2, ball, score1, score2)

        clock.tick(60)

if __name__ == "__main__":
    main()
