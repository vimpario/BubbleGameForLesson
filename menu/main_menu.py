# main_menu.py
import pygame
from config.settings import WIDTH, HEIGHT
from .text_element import TextElement


class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.play_button = TextElement(WIDTH // 2, HEIGHT // 3, "Играть", self.font)
        self.settings_button = TextElement(WIDTH // 2, HEIGHT // 2, "Настройки", self.font)
        self.shop_button = TextElement(WIDTH // 2, 2 * HEIGHT // 3, "Магазин", self.font)
        self.message = TextElement(WIDTH // 2, 5 * HEIGHT // 6, "", self.font)

    def draw(self, screen):
        screen.fill((255, 255, 255))  # Заливка белым цветом
        self.play_button.draw(screen)
        self.settings_button.draw(screen)
        self.shop_button.draw(screen)
        self.message.draw(screen)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.play_button.rect.collidepoint(mouse_x, mouse_y):
                return "play"
            elif self.settings_button.rect.collidepoint(mouse_x, mouse_y):
                self.message.update_text("Скоро будет добавлено в игру - Настройки")
            elif self.shop_button.rect.collidepoint(mouse_x, mouse_y):
                self.message.update_text("Скоро будет добавлено в игру - Магазин")
        return None
