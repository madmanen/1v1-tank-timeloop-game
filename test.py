import pygame
import sys
import math

pygame.init()
pygame.font.init()
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Test")
clock = pygame.time.Clock()
title_font = pygame.font.Font('Copixel-Demo.otf', 20)

def render_text(text: str, x: int, y: int, font, color, surface, line_spacing=5):
    lines = text.split('\n')  # Split text into lines using newline character
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x, y + i * (font.get_height() + line_spacing)))

menu_font = pygame.font.SysFont('calibri', 20)

class Character:
    def __init__(self, name: str, health: int, speed: int, damage: int, fire_rate: int, width: int, height: int,
                 turn_speed: int):
        self.name = name
        self.health = health
        self.speed = speed
        self.damage = damage
        self.fire_rate = fire_rate
        self.width = width
        self.height = height
        self.turn_speed = turn_speed

    def character_info(self):
        return f"Name:{self.name}\nHealth:{self.health}\nSpeed:{self.speed}\nturn speed:{self.turn_speed}\nDamage:{self.damage}\nFire Rate:{self.fire_rate}"

    # def shooting(self):
    # to-do: create a definition that describes shooting the gun


Light_tank = Character(name="Light tank", health=80, speed=10, damage=20, fire_rate=2, width=30, height=40,
                       turn_speed=5)  # Want its gun to be a shotgun
Medium_tank = Character(name="Medium tank", health=100, speed=7, damage=10, fire_rate=5, width=35, height=50,
                        turn_speed=3)
Heavy_tank = Character(name="Heavy tank", health=150, speed=5, damage=5, fire_rate=8, width=40, height=60, turn_speed=2)



class Item:
    def __init__(self, width: int, height: int, stat: str, modifier: int, time: int):
        self.width = width
        self.height = height
        self.stat = stat
        self.modifier = modifier
        self.time = time

    def item_info(self):
        return f'Grants {self.modifier} more {self.stat} for {self.time} seconds upon pickup'

    # def pickup(self):
    # to-do create a definition that describes picking up item


Speed_boost = Item(width=10, height=10, stat='speed', modifier=10, time=5)
Health_boost = Item(width=10, height=10, stat='health', modifier=50, time=1)

player1_character = Light_tank
player1_item = Speed_boost
player1 = pygame.Rect(200, 200, player1_character.width, player1_character.height)
player1_angle = 0

player2_character = Medium_tank
player2_item = Health_boost
player2 = pygame.Rect(400, 400, player2_character.width, player2_character.height)
player2_angle = 0

Light_tank_select = pygame.Rect(WIDTH / 2, HEIGHT / 2, 40, 40)
Medium_tank_select = pygame.Rect(WIDTH / 2, HEIGHT / 2 - 100, 40, 40)
Heavy_tank_select = pygame.Rect(WIDTH / 2, HEIGHT / 2 + 100, 40, 40)

menu_open = True
timer = 0

#boxes til menu layout
player1_menu = pygame.Rect(WIDTH / 2, 0, WIDTH / 2, HEIGHT)
player2_menu = pygame.Rect(0, 0, WIDTH / 2, HEIGHT)


def draw_menu():

    player1_menu_surface = pygame.Surface((player1_menu.width, player1_menu.height), pygame.SRCALPHA)
    player1_menu_surface.fill((200, 50, 50))
    player2_menu_surface = pygame.Surface((player2_menu.width, player2_menu.height), pygame.SRCALPHA)
    player2_menu_surface.fill((50,50,200))

    render_text(Character.character_info(player1_character), 20, 100, menu_font,'white', player1_menu_surface, 5)
    render_text(Character.character_info(player2_character), 20, 100, menu_font,'white', player2_menu_surface, 5)
    screen.blit(player2_menu_surface, player2_menu)
    screen.blit(player1_menu_surface, player1_menu)

    pygame.display.update()


def draw_round():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), Light_tank_select)
    pygame.draw.rect(screen, (255, 0, 0), Medium_tank_select)
    pygame.draw.rect(screen, (0, 0, 255), Heavy_tank_select)

    player1_surf = pygame.Surface((player1_character.width, player1_character.height), pygame.SRCALPHA)
    pygame.draw.rect(player1_surf, (0, 255, 0), player1_surf.get_rect())
    player1_surf_rotated = pygame.transform.rotate(player1_surf, player1_angle)

    player2_surf = pygame.Surface((player2_character.width, player2_character.height), pygame.SRCALPHA)
    pygame.draw.rect(player2_surf, (0, 255, 0), player2_surf.get_rect())
    player2_surf_rotated = pygame.transform.rotate(player2_surf, player2_angle)
    screen.blit(player1_surf_rotated, player1)
    screen.blit(player2_surf_rotated, player2)

    pygame.display.update()


while True:

    while menu_open == True and timer <= 0:  # This is the loop for everything in the menu between rounds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_open = False
                    timer = 600

                if event.key == pygame.K_UP and player1_character == Light_tank:
                    player1_character = Medium_tank
                elif event.key == pygame.K_UP and player1_character == Medium_tank:
                    player1_character = Heavy_tank
                elif event.key == pygame.K_DOWN and player1_character == Heavy_tank:
                    player1_character = Medium_tank
                elif event.key == pygame.K_DOWN and player1_character == Medium_tank:
                    player1_character = Light_tank

                if event.key == pygame.K_w and player2_character == Light_tank:
                    player2_character = Medium_tank
                elif event.key == pygame.K_w and player2_character == Medium_tank:
                    player2_character = Heavy_tank
                elif event.key == pygame.K_s and player2_character ==Heavy_tank:
                    player2_character = Medium_tank
                elif event.key == pygame.K_s and player2_character == Medium_tank:
                    player2_character = Light_tank
        draw_menu()
        clock.tick(60)
    while timer !=0:  # This is the loop during an active round
        timer = timer-1
        print(timer)
        if menu_open == False and timer <= 0:
            player1 = pygame.Rect(200, 200, player1_character.width, player1_character.height)
            player1_angle = 0

            player2 = pygame.Rect(400, 400, player2_character.width, player2_character.height)
            player2_angle = 0

            timer = 600
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                menu_open = True
                print(menu_open)
        rad1 = math.radians(player1_angle)
        rad2 = math.radians(player2_angle)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player1_angle += player1_character.turn_speed
        if keys[pygame.K_RIGHT]:
            player1_angle -= player1_character.turn_speed
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
