from pygame import *

class gameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__()
        self.image = transform.scale( image.load(player_image), size)
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))

class PLAYER(gameSprite):
    def update(self, key1, key2):
        KP = key.get_pressed()
        if KP[key1] and self.rect.x >0:
            self.rect.x -= self.speed
        if KP[key2] and self.rect.x < 625:
            self.rect.x += self.speed

WINDOW = display.set_mode((700,500))
WINDOW.fill((255,255,255))
display.set_caption('ping-pong')
game = True
clock = time.Clock()
while True:
    for ev in event.get():
        if ev.type == QUIT:
            exit()
    display.update()
    clock.tick(60)