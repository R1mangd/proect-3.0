import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализируем и задаём начальную позицию"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('imeges/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод врага на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемешает пришельца"""
        self.y += 0.04
        self.rect.y = self.y