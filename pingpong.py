from pygame import *

BLUE = (200,255,255)

width = 900
height = 700
win = display.set_mode((width, height))
display.set_caption("Ping-Pong")
win.fill(BLUE)
clock = time.Clock()
FPS = 60

class Player(GameSprite):
    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.y > height - 10:
            self.rect.x -= self.speed 
        if key_pressed[K_RIGHT] and self.rect.y > 5:
            self.rect.x += self.speed
        
    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.y > height - 100:
            self.rect.x -= self.speed 
        if key_pressed[K_RIGHT] and self.rect.y > 5:
            self.rect.x += self.speed

class Ball(GameSprite):
    def update(self):
        pass

ball = Ball('ball.png', width/2, height/2, 50, 50, 5)
pl_left = Player('platform.png', 875, 300, 20, 100, 5)
pl_left = Player('platform.png', 5, 300, 20, 100, 5)

game = True
while game:
    win.fill(BLUE)
    ball.reset()
    pl_right.reset()
    pl_left.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    ball.update()
    pl_left.update_left()
    display.update-right()
    clock.tick(FPS)
     