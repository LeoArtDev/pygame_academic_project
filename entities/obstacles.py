import pygame
from systems.settings import LARGURA, ALTURA

class Obstacle:
    
    def __init__(self):
        self.x = LARGURA / 2
        self.y = 100
        
        self.raio = 120
        
        self.velocidade = 600
        
    def draw(self, tela):
        pygame.draw.circle(
            tela,
            "blue",
            (self.x, self.y),
            self.raio
        )
        
    def atualizar(self, dt):
        self.y += self.velocidade * dt
        
    def restart(self, tela):
            self.x = LARGURA / 2
            self.y = 100
            self.draw(tela)
            