# game.py
import random

import pygame
import sys
from config.settings import WIDTH, HEIGHT, WHITE, BLUE, FPS
from .bubble import create_bubble, update_bubbles, handle_clicks
from .text_element import TextElement

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bubble_image = pygame.image.load("resources/images/bubble.png")
    bubble_image = pygame.transform.scale(bubble_image, (100, 100))

    pop_sound = pygame.mixer.Sound("resources/sounds/pop.wav")

    score_text = TextElement(10, 10, "Счет: 0")
    click_text = TextElement(10, 40, "Клики: 0")

    bubbles = []

    def quit_app():
        pygame.quit()
        sys.exit()

    def draw_elements():
        screen.fill(WHITE)
        score_text.draw(screen)
        click_text.draw(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                handle_clicks(bubbles, mouse_x, mouse_y, pop_sound, score_text, click_text)

        if random.randint(1, 100) < 10:
            create_bubble(bubbles)

        draw_elements()
        update_bubbles(bubbles)

        for bubble in bubbles:
            if bubble.status == "alive":
                screen.blit(bubble_image, (bubble.x, bubble.y))

        pygame.display.flip()
        clock.tick(FPS)

    quit_app()
