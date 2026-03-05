import pygame
import random

class Food:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.position = self.spawn()
    
    def spawn(self):
        x = round(random.randrange(0, self.width - self.block_size) / 10.0) * 10.0
        y = round(random.randrange(0, self.height - self.block_size) / 10.0) * 10.0
        return [x, y]
    
    def draw(self, surface, color):
        pygame.draw.rect(surface, color, [self.position[0], self.position[1], self.block_size, self.block_size])
