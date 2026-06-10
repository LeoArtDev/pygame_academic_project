import pygame
import random

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class CameraGroup(pygame.sprite.Group):
    """Custom group to handle camera offsets."""
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def custom_draw(self, player):
        # Center camera on player
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        # Draw sprites relative to offset
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.Surface((50, 50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]: self.rect.x += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed

# Setup
camera_group = CameraGroup()
player = Player((400, 300), camera_group)
# Random objects to show movement
for _ in range(20):
    bg = pygame.sprite.Sprite(camera_group)
    bg.image = pygame.Surface((50, 50))
    bg.image.fill('green')
    bg.rect = bg.image.get_rect(topleft=(random.randint(0,1000), random.randint(0,1000)))

# Main Loop
while pygame.event.get(pygame.QUIT) == []:
    screen.fill('black')
    camera_group.update()
    camera_group.custom_draw(player)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
