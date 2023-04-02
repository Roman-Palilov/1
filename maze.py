#создай игру "Лабиринт"!
from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (70, 70))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    
    def update(self):
        keys = key.get_pressed()

        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    
    def update(self):
        if self.rect.x <= 10:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Final(GameSprite):
    direction = 'left'
    
    def update(self):
        if self.rect.x <= 520:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета
       
        self.image = Surface((self.width, self.height))

        self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall(250, 205, 50, 100, 80 , 500, 10)
w2 = Wall(250, 205, 50, 100, 80, 10, 300)
w3 = Wall(250, 205, 50, 200, 200, 10, 300)
w4 = Wall(250, 205, 50, 200, 200, 400, 10)
w5 = Wall(250, 205, 50, 100, 100, 10, 300)
w6 = Wall(250, 205, 50, 300, 300, 400, 10)
w7 = Wall(250,205, 50, 400, 400, 10, 100)
w8 = Wall(250,205, 50, 480, 300, 10, 100)

#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажи игры:
player = Player('1055.png', 0, 430, 4)
monster = Enemy('kiborg.jpg', 610, 300, 8)
monster2 = Enemy('kiborg.jpg', 610, 100, 2)
final = Final('sokrovishe-PhotoRoom.png', 600, 420, 2)
aptechka = GameSprite('apteka.png', 0, 0, 0)

game = True
finish = False
clock = time.Clock()
FPS = 70

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background,(0, 0))

        player.update()
        player.reset()
        monster.update()
        monster.reset()
        monster2.update()
        monster2.reset()
        final.update()
        final.reset()
        aptechka.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        if sprite.collide_rect(player, final):
            print('Побэда!')
            finish = True
        if sprite.collide_rect(player, w1 ) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or  sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8):
            finish = True
        if sprite.collide_rect(player,  monster):
            finish = True
        if sprite.collide_rect(player,  monster2):
            finish = True
        display.update()
        clock.tick(FPS)




