import pygame
from systems.settings import LARGURA, ALTURA

player_sprite = pygame.image.load("assets/Maguinho.png")

class Player:
    
    def __init__(self):
        self.largura = 30
        self.altura = 25
        
        self.x = LARGURA / 2 #posicao no eixo x
        self.y = 600 #posicao no eixo y
        self.raio = 20
        self.velocidade = 800
        self.vertical = 280
        self.morto = False
        self.direcao_x = -1

        self.paused = False
        
        #self.pos = (self.x, self.y)
    
    def draw(self, tela):
        pygame.draw.circle(
            tela,
            "pink",
            (self.x, self.y),
            self.raio
        )
    
    def desenhar_player(self, tela):
        tela.blit(player_sprite, (self.x, self.y))
    
    def subir(self, dt):
        self.y -= self.vertical * dt
    
    # faz o jogador estar sempre se movendo na horizontal
    def zigzag(self, dt):
        self.x += self.direcao_x * self.velocidade * dt
    
    # muda o sentido em que o jogador está se movendo, esquerda e direita    
    def mudar_direcao(self, dt):
        self.direcao_x *= -1   
    
    # uma função que está constantemente verificando se a extremidade do lado esquerdo ou direito forem menores ou maiores que as extremidades esuqerda e direita (x = 0 e y = ALTURA, respectivamente)
    def morte_lateral(self, dt):
        self.lado_esquerdo = self.x - self.raio
        self.lado_direito = self.x + self.raio
        if self.lado_esquerdo <= 0:
            self.morto = True
        if self.lado_direito >= LARGURA:
            self.morto = True
    
    def game_over(self, tela):
        pygame.draw.circle(
            tela,
            "red",
            (self.x, self.y),
            40
        )
    
    def dispause(self, dt):
        self.paused = False
        self.velocidade = 800
        self.vertical = 280
    
    def pause(self, dt):
        self.paused = True
        self.velocidade = 0
        self.vertical = 0
        
    
    # fiz só pra brincar kk
    def restart(self, tela):
        self.morto = False
        self.x, self.y = LARGURA/2, 600
        self.draw(tela)
    
    # def move_up(self):
        
    #     self.y += self.velocidade



print(player_sprite.get_size())
