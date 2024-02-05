# bubble.py
import pygame
import random
from config.settings import WIDTH, HEIGHT
from .text_element import TextElement


class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = "alive"
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(1, 5)

    def update(self):
        if self.status == "alive":
            self.x += self.speed_x
            self.y -= self.speed_y

            if self.x < 0 or self.x + 100 > WIDTH:
                self.speed_x = -self.speed_x

            if self.y < 0 or self.y + 100 > HEIGHT:
                self.speed_y = -self.speed_y

    def is_clicked(self, mouse_x, mouse_y):
        return (
            self.x <= mouse_x <= self.x + 100
            and self.y <= mouse_y <= self.y + 100
            and self.status == "alive"
        )

    def pop(self):
        if self.status == "alive":
            self.status = "popped"
            return 1
        return 0


def create_bubble(bubbles):
    bubble_x = random.randint(0, WIDTH - 100)
    bubble_y = random.randint(0, HEIGHT - 100)
    bubbles.append(Bubble(bubble_x, bubble_y))


def update_bubbles(bubbles):
    for bubble in bubbles:
        bubble.update()


def handle_clicks(bubbles, mouse_x, mouse_y, pop_sound, score_text, click_text):
    score_increase = 0
    click_increase = 0
    for bubble in bubbles:
        if bubble.is_clicked(mouse_x, mouse_y):
            score_increase += bubble.pop()
            pop_sound.play()
    click_increase += 1
    score_text.score+=score_increase
    click_text.score +=click_increase
    score_text.update_text(f"Счет: {score_text.score + score_increase}")
    click_text.update_text(f"Клики: {click_text.score + click_increase}")
