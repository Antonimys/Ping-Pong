from pygame import *
from time import time as timer

win_height = 600
win_width = 500

RocketIMG = "r.png"
BallIMG = "b.png"

window = display.set_mode((win_height, win_width))
window.fill((200, 255, 255))
display.set_caption("Пинг понг")

FPS = 60
game = True
finish = False

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)


       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


rocket1 = Player(RocketIMG, 30, 200, 50, 150, 10)
rocket2 = Player(RocketIMG, 520, 200, 50, 150, 10)
ball = GameSprite(BallIMG, 200, 200, 50, 50, 10)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

speedX = 3
speedY = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill((200, 255, 255))
        rocket2.update()
        rocket1.update1()

        ball.rect.x += speedX
        ball.rect.y += speedY
        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speedX *= -1
            speedY *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speedY *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game = True
        rocket1.reset()
        rocket2.reset()
        ball.reset()
    display.update()
    time.delay(50)
