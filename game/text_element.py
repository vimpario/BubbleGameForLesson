# text_element.py
import pygame
from config.settings import BLUE


class TextElement:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.surface = self.font.render(self.text, True, BLUE)
        self.rect = self.surface.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.score = 0



    def update_text(self, new_text):
        self.text = new_text
        self.surface = self.font.render(self.text, True, BLUE)


    def draw(self, screen):
        screen.blit(self.surface, self.rect)
