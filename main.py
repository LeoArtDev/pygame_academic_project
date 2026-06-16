import pygame
from entities.player import Player
from entities.obstacles import Obstacle
from systems.settings import LARGURA, ALTURA, FPS
# pygame setup
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()
player = Player()
obstacle = Obstacle()

def main ():
    running = True
    player.morto = False
    
    def checar_colisao():
        dx = obstacle.x - player.x
        dy = obstacle.y - player.y

        distancia_quadrada = dx * dx + dy * dy

        soma_raios = player.raio + obstacle.raio

        if distancia_quadrada <= soma_raios * soma_raios:
            player.morto = True
            
    while running:
        dt = clock.tick(FPS) / 1000
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        tela.fill("#212040")
        #player.desenhar_player(tela)
        player.draw(tela)
        obstacle.draw(tela)

        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                
                if event.key == pygame.K_SPACE:
                    player.mudar_direcao()
                    
                if event.key == pygame.K_w:
                    player.morto = True
                    
                if player.morto == True and event.key == pygame.K_r:
                    player.restart(tela)
                    obstacle.restart(tela)
      
        if not player.morto:
            player.atualizar_rastro(dt)
            player.zigzag(dt)
            player.morte_lateral(dt)
            obstacle.atualizar(dt)
            checar_colisao()
        else:
            player.game_over(tela)
        
        

        
        # if not player.paused:
        #     player.subir(dt)
        #     player.zigzag(dt)
        #     player.morte_lateral(dt)
        # else:
        #     player.pause(dt)
        
        
        # flip() the display to put your work on screen
        pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    pygame.quit()


main()
