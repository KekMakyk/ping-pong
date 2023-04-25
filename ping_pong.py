from pygame import *

font.init()
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
        if KP[key1] and self.rect.y >0:
            self.rect.y -= self.speed
        if KP[key2] and self.rect.y < 400:
            self.rect.y += self.speed
class ball(gameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size):
        super().__init__(player_image, player_x, player_y, player_speed, size)
        self.speedx = self.speed
        self.speedy = self.speed
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.colliderect(pl1):
            self.speedx *= -1
            self.rect.x =70
        if self.rect.colliderect(pl2):
            self.speedx *= -1
            self.rect.x =590
        if self.rect.y <= 0 or self.rect.y >= 450:
            self.speedy *= -1


font = font.SysFont('Areal', 40)
ball = ball('ball.png', 350, 0, 3, (50, 50))
pl1 = PLAYER('platform.png', 50, 200, 3, (20, 100))
pl2 = PLAYER('platform.png', 640, 200, 3, (20, 100))
WINDOW = display.set_mode((700,500))
display.set_caption('ping-pong')
game = True
clock = time.Clock()
win = 'первый игрок'
while True:
    for ev in event.get():
        if ev.type == QUIT:
            exit()

    if game:
        WINDOW.fill((200,200,200))
        ball.update()
        ball.reset()
        pl1.update(K_w, K_s)
        pl1.reset()
        pl2.update(K_UP, K_DOWN)
        pl2.reset()
        if ball.rect.x >=700 or ball.rect.x <=-50:
            game = False
            if ball.rect.x <=-50:
                win = 'второй игрок'
    if not game:
        WINDOW.blit(font.render('Победил '+win, True, (20,20,20)), (230,100))

    display.update()
    clock.tick(60)
