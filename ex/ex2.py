import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLUE = (100, 150, 255)
WHITE = (255, 255, 255)
GREEN = (50, 200, 50)
YELLOW = (255, 220, 0)


def create_bird():
    return {
        "x": 80,
        "y": 300,
        "w": 30,
        "h": 30,
        "vel_y": 0
    }


def create_pipe():
    gap_y = random.randint(150, 400)
    gap_height = 130

    return {
        "x": WIDTH,
        "top_h": gap_y - gap_height // 2,
        "bottom_y": gap_y + gap_height // 2,
        "w": 50,
        "speed": 3,
        "passed": False
    }


def check_pipe_collision(bird, pipe):
    bird_right = bird["x"] + bird["w"]

    if bird_right > pipe["x"] and bird["x"]<pipe["x"]+pipe["w"]  :
        if bird["y"] < pipe["top_h"] or bird["y"] + bird["h"] > pipe["bottom_y"]:
            return True

    return False


def main():
    bird = create_bird()
    pipes = []
    score = 0
    spawn_timer = 0

    font = pygame.font.SysFont("Arial", 30)

    gravity = 0.5
    jump_strength = -8

    running = True

    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird["vel_y"]  = jump_strength

        bird["vel_y"] += gravity
        bird["y"] += bird["vel_y"]

        if bird["y"] + bird["h"] >= HEIGHT:
            running = False

        spawn_timer += 1

        if spawn_timer % 90 == 0:
            pipes.append(create_pipe())

        pipes_to_remove=[]

        for i in range(len(pipes)):
            p=pipes[i]
            p["x"] -= p["speed"]

            if not p["passed"] and p["x"]+p["w"] < bird["x"]:
                score += 1
                p["passed"] = True

            if check_pipe_collision(bird, p):
                print("Game Over! Score:", score)
                running = False

            if p["x"] + p["w"] <=0:
                pipes_to_remove.append(i)

        for pipe in pipes_to_remove:
            pipes.pop (pipe)



        pygame.draw.rect(
            screen,
            YELLOW,
            (bird["x"], bird["y"], bird["w"], bird["h"])
        )

        for p in pipes:
            pygame.draw.rect(
                screen,
                GREEN,
                (p["x"], 0, p["w"], p["top_h"])
            )

            pygame.draw.rect(
                screen,
                GREEN,
                (p["x"], p["bottom_y"], p["w"], HEIGHT - p["bottom_y"])
            )


        score_txt = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_txt, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()