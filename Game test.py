import pygame
import sys
pygame.init()

WIDTH=1000
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Test")
clock=pygame.time.Clock()

class Character:
    def __init__(self,name: str, health: int, speed: int, damage: int, fireRate: int, width: int, height: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.fireRate = fireRate
        self.width = width
        self.height = height

    #def shooting(self):
        #to-do: create a definition that describes shooting the gun


Light_tank = Character(name="Light tank", health=80, speed=30, damage=20, fireRate=2, width=40, height=40) #Want its gun to be a shotgun
Medium_tank = Character(name="Medium tank", health=100, speed=20, damage=10, fireRate=5, width=50, height=50)
Heavy_tank = Character(name="Heavy tank", health=150, speed=10, damage=5, fireRate=8, width=60, height=60)

class Item:
    def __init__(self, width: int, height: int, property, modifier: int, time):
        self.width = width
        self.height = height
        self.property = property
        self.modifier = modifier
        self.time = time

    def item_info(self):
        return f'Grants {self.modifier} more {self.property} for {self.time} seconds upon pickup'

    #def pickup(self):
        #to-do create a definition that describes picking up item

Speed_boost = Item(width=10, height=10, property='speed', modifier=10, time=5)
Health_boost = Item(width=10, height=10, property='health', modifier=50, time=1)


def draw():
    screen.fill((0,0,0))
    screen.blit(screen,test)
    pygame.draw.rect(screen,(255,255,255),test)
    pygame.draw.rect(screen,(255,255,255),player)
    pygame.display.update()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    test=pygame.Rect(WIDTH/2, HEIGHT/2, 100, 50)
    player=pygame.Rect(WIDTH/3, HEIGHT/3, Light_tank.width, Light_tank.height)

    draw()