import pygame
import sys
import math

pygame.init()

WIDTH=1200
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Test")
clock=pygame.time.Clock()

class Character:
    def __init__(self,name: str, health: int, speed: int, damage: int, fireRate: int, width: int, height: int, turn_speed: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.fireRate = fireRate
        self.width = width
        self.height = height
        self.turn_speed = turn_speed

    #def shooting(self):
        #to-do: create a definition that describes shooting the gun


Light_tank = Character(name="Light tank", health=80, speed=10, damage=20, fireRate=2, width=30, height=40, turn_speed=5) #Want its gun to be a shotgun
Medium_tank = Character(name="Medium tank", health=100, speed=7, damage=10, fireRate=5, width=35, height=50, turn_speed=3)
Heavy_tank = Character(name="Heavy tank", health=150, speed=5, damage=5, fireRate=8, width=40, height=60, turn_speed=2)

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

player1_character = Light_tank
player1 = pygame.Rect(200, 200, player1_character.width, player1_character.height)
player_angle = 0


Light_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2, 40,40)
Medium_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2-100, 40,40)
Heavy_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2+100, 40,40)


def draw():
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),Light_tank_select)
    pygame.draw.rect(screen,(255,0,0),Medium_tank_select)
    pygame.draw.rect(screen,(0,0,255),Heavy_tank_select)
    player1_surf = pygame.Surface((player1_character.width, player1_character.height), pygame.SRCALPHA)

    pygame.draw.rect(player1_surf, (0, 255, 0), player1_surf.get_rect())
    player1_surf_rotated = pygame.transform.rotate(player1_surf,player_angle)
    screen.blit(player1_surf_rotated, player1)


    pygame.display.update()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle +=player1_character.turn_speed
    if keys[pygame.K_RIGHT]:
        player_angle -=player1_character.turn_speed
    if keys[pygame.K_UP]:
        rad = math.radians(player_angle)
        player1.x += player1_character.speed * math.sin(rad)
        player1.y += player1_character.speed * math.cos(rad)
    if keys[pygame.K_DOWN]:
        rad = math.radians(player_angle)
        player1.x -= player1_character.speed * math.sin(rad)
        player1.y -= player1_character.speed * math.cos(rad)

    if player1.colliderect(Light_tank_select):
        player1_character = Light_tank
    if player1.colliderect(Medium_tank_select):
        player1_character = Medium_tank
    if player1.colliderect(Heavy_tank_select):
        player1_character = Heavy_tank
    draw()
    clock.tick(60)