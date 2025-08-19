import pygame
import sys
import math

pygame.init()

WIDTH = 1200
HEIGHT = 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Test")
clock=pygame.time.Clock()

class Character:
    def __init__(self,name: str, health: int, speed: int, damage: int, fire_rate: int, width: int, height: int, turn_speed: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.fire_rate = fire_rate
        self.width = width
        self.height = height
        self.turn_speed = turn_speed

    def character_info(self):
        return  (f'Health:{self.health} '
                 f'Speed:{self.speed} '
                 f'turn speed:{self.turn_speed} '
                 f'Damage:{self.damage} '
                 f'Fire Rate:{self.fire_rate}')

    #def shooting(self):
        #to-do: create a definition that describes shooting the gun


Light_tank = Character(name="Light tank", health=80, speed=10, damage=20, fire_rate=2, width=30, height=40, turn_speed=5) #Want its gun to be a shotgun
Medium_tank = Character(name="Medium tank", health=100, speed=7, damage=10, fire_rate=5, width=35, height=50, turn_speed=3)
Heavy_tank = Character(name="Heavy tank", health=150, speed=5, damage=5, fire_rate=8, width=40, height=60, turn_speed=2)

class Item:
    def __init__(self, width: int, height: int, property: str, modifier: int, time: int):
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
player1_angle = 0

player2_character = Medium_tank
player2 = pygame.Rect(400, 400, player2_character.width, player2_character.height)
player2_angle = 0


Light_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2, 40,40)
Medium_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2-100, 40,40)
Heavy_tank_select = pygame.Rect(WIDTH/2,HEIGHT/2+100, 40,40)


menu_open = True
def draw_menu():
    screen.fill((98,232,218))

    pygame.display.update()
def draw_round():
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),Light_tank_select)
    pygame.draw.rect(screen,(255,0,0),Medium_tank_select)
    pygame.draw.rect(screen,(0,0,255),Heavy_tank_select)

    player1_surf = pygame.Surface((player1_character.width, player1_character.height), pygame.SRCALPHA)
    pygame.draw.rect(player1_surf, (0, 255, 0), player1_surf.get_rect())
    player1_surf_rotated = pygame.transform.rotate(player1_surf,player1_angle)

    player2_surf = pygame.Surface((player2_character.width, player2_character.height), pygame.SRCALPHA)
    pygame.draw.rect(player2_surf, (0, 255, 0), player2_surf.get_rect())
    player2_surf_rotated = pygame.transform.rotate(player2_surf,player2_angle)
    screen.blit(player1_surf_rotated, player1)
    screen.blit(player2_surf_rotated, player2)


    pygame.display.update()

while True:
    while menu_open:    #This is the loop for everything in the menu between rounds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys == pygame.K_LEFT:
            
        draw_menu()
        clock.tick(60)
    while not menu_open:  # This is the loop during an active round
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        rad1 = math.radians(player1_angle)
        rad2 = math.radians(player2_angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1_angle +=player1_character.turn_speed
        if keys[pygame.K_RIGHT]:
            player1_angle -=player1_character.turn_speed
        if keys[pygame.K_UP]:
            player1.x += player1_character.speed * math.sin(rad1)
            player1.y += player1_character.speed * math.cos(rad1)
        if keys[pygame.K_DOWN]:
            player1.x -= player1_character.speed * math.sin(rad1)
            player1.y -= player1_character.speed * math.cos(rad1)

        if keys[pygame.K_a]:
            player2_angle += player2_character.turn_speed
        if keys[pygame.K_d]:
            player2_angle -= player2_character.turn_speed
        if keys[pygame.K_w]:
            player2.x -= player2_character.speed * math.sin(rad2)
            player2.y -= player2_character.speed * math.cos(rad2)
        if keys[pygame.K_s]:
            player2.x += player2_character.speed * math.sin(rad2)
            player2.y += player2_character.speed * math.cos(rad2)



        if player1.colliderect(Light_tank_select):
            player1_character = Light_tank
        if player1.colliderect(Medium_tank_select):
            player1_character = Medium_tank
        if player1.colliderect(Heavy_tank_select):
            player1_character = Heavy_tank

        if player2.colliderect(Light_tank_select):
            player2_character = Light_tank
        if player2.colliderect(Medium_tank_select):
            player2_character = Medium_tank
        if player2.colliderect(Heavy_tank_select):
            player2_character = Heavy_tank
        draw_round()
        clock.tick(60)

