import pygame
from pygame import *
from pygame import mixer
import pygame.freetype
import time
import sys
from Button import Button
from random import randint


SCREEN_SIZE = pygame.Rect((0, 0, 1280, 720))
TILE_SIZE = 32
MAP_BORDER = (1000, 500)
GRAVITY = pygame.Vector2((0, 0.4))


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))


BG = pygame.image.load("Background.png")
CHARACTER_SKINS = ("Sprites/SpriteBasic.png")
INVENTORY_ITEMS = []

ALLOWED_LEVELS = 0
COINS = 0

def random_number():
    segment_choice(RANDOM_NUMBER=randint(1,7))
    free_play_music()

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def not_completed():
    SCREEN.fill((0, 255, 255))
    my_font = pygame.font.SysFont('Comic Sans MS', 100)
    font_render = my_font.render('Complete The Levels ', False, (0, 0, 0))
    font_render2 = my_font.render(' Before To Access', False, (0, 0, 0))
    SCREEN.blit(font_render, (200, 150))
    SCREEN.blit(font_render2, (200, 400))
    pygame.display.update()
    time.sleep(1.5)

def not_enough_money():
    SCREEN.fill((255, 0, 0))
    my_font = pygame.font.SysFont('Comic Sans MS', 100)
    font_render = my_font.render('Not Enough Money To', False, (0, 0, 0))
    font_render2 = my_font.render('Purchase A New Character', False, (0, 0, 0))
    SCREEN.blit(font_render, (0, 150))
    SCREEN.blit(font_render2, (0, 400))
    pygame.display.update()
    time.sleep(1.5)

def sold():
    SCREEN.fill((0, 255, 255))
    my_font = pygame.font.SysFont('Comic Sans MS', 450)
    font_render = my_font.render('SOLD', False, (0, 0, 0))
    SCREEN.blit(font_render, (0, 0))
    pygame.display.update()
    time.sleep(1)

def character_selected():
    SCREEN.fill((0, 255, 255))
    my_font = pygame.font.SysFont('Comic Sans MS', 150)
    font_render = my_font.render('CHARACTER', False, (0, 0, 0))
    font_render2 = my_font.render('SELECTED', False, (0, 0, 0))
    SCREEN.blit(font_render, (200, 150))
    SCREEN.blit(font_render2, (200, 400))
    pygame.display.update()
    time.sleep(1)

def inventory_choice(item):
    sprite_images = ["Sprites/SpriteBasic.png",
                     "Sprites/Sprite1.png",
                     "Sprites/Sprite2.png",
                     "Sprites/Sprite2.png",
                     "Sprites/Sprite3.png",
                     "Sprites/Sprite4.png"]
    global INVENTORY_ITEMS
    print(INVENTORY_ITEMS)
    INVENTORY_ITEMS.append((sprite_images[item]))
    print(INVENTORY_ITEMS)

def not_owned():
    SCREEN.fill((255, 0, 0))
    my_font = pygame.font.SysFont('Comic Sans MS', 75)
    font_render = my_font.render('You Dont Own This Character', False, (0, 0, 0))
    font_render2 = my_font.render('It Can Be Bought In The Shop', False, (0, 0, 0))
    SCREEN.blit(font_render, (200, 150))
    SCREEN.blit(font_render2, (200, 400))
    pygame.display.update()
    time.sleep(2)


def inventory_window():

    global CHARACTER_SKINS
    sprite1 = "Not Owned"
    sprite2 = "Not Owned"
    sprite3 = "Not Owned"
    sprite4 = "Not Owned"
    sprite5 = "Not Owned"


    while True:
        SCREEN.fill("black")
        pygame.display.set_caption("Inventory")
        INVENTORY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("INVENTORY", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        for i in INVENTORY_ITEMS:
            if i == "Sprites/SpriteBasic.png":
                sprite1 = "Owned"
                if "Sprites/SpriteBasic.png" == CHARACTER_SKINS:
                    sprite1 = "Selected"
            elif i == "Sprites/Sprite1.png":
                sprite2 = "Owned"
                if "Sprites/Sprite1.png" == CHARACTER_SKINS:
                    sprite2 = "Selected"
            elif i == "Sprites/Sprite2.png":
                sprite3 = "Owned"
                if "Sprites/Sprite2.png" == CHARACTER_SKINS:
                    sprite3 = "Selected"
            elif i == "Sprites/Sprite3.png":
                sprite4 = "Owned"
                if "Sprites/Sprite3.png" == CHARACTER_SKINS:
                    sprite4 = "Selected"
            elif i == "Sprites/Sprite4.png":
                sprite5 = "Owned"
                if "Sprites/Sprite4.png" == CHARACTER_SKINS:
                    sprite5 = "Selected"




        sprite1_img = pygame.image.load("Sprites/SpriteBasic.png")
        sprite2_img = pygame.image.load("Sprites/Sprite1.png")
        sprite3_img = pygame.image.load("Sprites/Sprite2.png")
        sprite4_img = pygame.image.load("Sprites/Sprite3.png")
        sprite5_img = pygame.image.load("Sprites/Sprite4.png")
        sprite1_img = pygame.transform.scale(sprite1_img, (128, 128))
        sprite2_img = pygame.transform.scale(sprite2_img, (128, 128))
        sprite3_img = pygame.transform.scale(sprite3_img, (128, 128))
        sprite4_img = pygame.transform.scale(sprite4_img, (128, 128))
        sprite5_img = pygame.transform.scale(sprite5_img, (128, 128))

        SPRITE_BUTTON1 = Button(image=sprite1_img, pos=(200, 400),
                             text_input=sprite1, font=get_font(20), base_color="red", hovering_color="White")
        SPRITE_BUTTON2 = Button(image=sprite2_img, pos=(400, 400),
                                text_input=sprite2, font=get_font(20), base_color="red", hovering_color="White")
        SPRITE_BUTTON3 = Button(image=sprite3_img, pos=(600, 400),
                                text_input=sprite3, font=get_font(20), base_color="red", hovering_color="White")
        SPRITE_BUTTON4 = Button(image=sprite4_img, pos=(800, 400),
                                text_input=sprite4, font=get_font(20), base_color="red", hovering_color="White")
        SPRITE_BUTTON5 = Button(image=sprite5_img, pos=(1000, 400),
                                text_input=sprite5, font=get_font(20), base_color="red", hovering_color="White")


        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [QUIT_BUTTON, SPRITE_BUTTON1, SPRITE_BUTTON2, SPRITE_BUTTON3, SPRITE_BUTTON4, SPRITE_BUTTON5]:
            button.changeColor(INVENTORY_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.checkForInput(INVENTORY_MOUSE_POS):
                    shop_menu_window()
                if SPRITE_BUTTON1.checkForInput(INVENTORY_MOUSE_POS):
                    if sprite1 == "Owned" or sprite1 == "Selected":
                        CHARACTER_SKINS = "Sprites/SpriteBasic.png"
                        character_selected()
                    else:
                        not_owned()
                if SPRITE_BUTTON2.checkForInput(INVENTORY_MOUSE_POS):
                    if sprite2 == "Owned" or sprite2 == "Selected":
                        CHARACTER_SKINS = "Sprites/Sprite1.png"
                        character_selected()
                    else:
                        not_owned()
                if SPRITE_BUTTON3.checkForInput(INVENTORY_MOUSE_POS):
                    if sprite3 == "Owned" or sprite3 == "Selected":
                        CHARACTER_SKINS = "Sprites/Sprite2.png"
                        character_selected()
                    else:
                        not_owned()
                if SPRITE_BUTTON4.checkForInput(INVENTORY_MOUSE_POS):
                    if sprite4 == "Owned" or sprite4 == "Selected":
                        CHARACTER_SKINS = "Sprites/Sprite3.png"
                        character_selected()
                    else:
                        not_owned()
                if SPRITE_BUTTON5.checkForInput(INVENTORY_MOUSE_POS):
                    if sprite5 == "Owned" or sprite5 == "Selected":
                        CHARACTER_SKINS = "Sprites/Sprite4.png"
                        character_selected()
                    else:
                        not_owned()


            pygame.display.update()


def shop_window2():
    pygame.display.set_caption("SHOP WINDOW 2")
    level_music(level=0)
    while True:
        SHOP_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        MENU_TEXT = get_font(150).render("SHOP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(440, 100))
        SHOP_TEXT = get_font(50).render("coins:", True, "#b68f40")
        SHOP_RECT = SHOP_TEXT.get_rect(center=(900, 100))
        COINS_TEXT = get_font(50).render(str(COINS), True, "#b68f40")
        COINS_RECT = SHOP_TEXT.get_rect(center=(1200, 100))

        sprite1 = pygame.image.load("Sprites/Sprite3.png")
        sprite2 = pygame.image.load("Sprites/Sprite4.png")

        sprite1 = pygame.transform.scale(sprite1, (200, 200))
        sprite2 = pygame.transform.scale(sprite2, (200, 200))

        SKIN1_BUTTON = Button(image=sprite1, pos=(350, 300),
                              text_input="80", font=get_font(75), base_color="red", hovering_color="White")
        SKIN2_BUTTON = Button(image=sprite2, pos=(980, 300),
                              text_input="160", font=get_font(75), base_color="red", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(350, 550),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        NEXT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="NEXT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [SKIN1_BUTTON, SKIN2_BUTTON, QUIT_BUTTON, NEXT_BUTTON]:
            button.changeColor(SHOP_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(SHOP_TEXT, SHOP_RECT)
        SCREEN.blit(COINS_TEXT, COINS_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN1_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    if COINS >= 80:
                        cash(money=-80)
                        sold()
                        inventory_choice(item=4)
                    else:
                        not_enough_money()

                if SKIN2_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    if COINS >= 160:
                        cash(money=-160)
                        sold()
                        inventory_choice(item=5)
                    else:
                        not_enough_money()
                if QUIT_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    shop_window1()

                if NEXT_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    continue
                    #shop_window3()

        pygame.display.update()

def shop_window1():
    pygame.display.set_caption("SHOP WINDOW 1")
    level_music(level=0)
    while True:

        SHOP_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        MENU_TEXT = get_font(150).render("SHOP", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(440, 100))
        SHOP_TEXT = get_font(50).render("coins:", True, "#b68f40")
        SHOP_RECT = SHOP_TEXT.get_rect(center=(900, 100))
        COINS_TEXT = get_font(50).render(str(COINS), True, "#b68f40")
        COINS_RECT = SHOP_TEXT.get_rect(center=(1200, 100))

        sprite1 = pygame.image.load("Sprites/Sprite1.png")
        sprite2 = pygame.image.load("Sprites/Sprite2.png")

        sprite1 = pygame.transform.scale(sprite1, (200, 200))
        sprite2 = pygame.transform.scale(sprite2, (200, 200))

        SKIN1_BUTTON = Button(image=sprite1, pos=(350, 300),
                             text_input="20", font=get_font(75), base_color="red", hovering_color="White")
        SKIN2_BUTTON = Button(image=sprite2, pos=(980, 300),
                                text_input="40", font=get_font(75), base_color="red", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(350, 550),
                                   text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        NEXT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="NEXT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")



        for button in [SKIN1_BUTTON, SKIN2_BUTTON, QUIT_BUTTON, NEXT_BUTTON]:
            button.changeColor(SHOP_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)
        SCREEN.blit(SHOP_TEXT, SHOP_RECT)
        SCREEN.blit(COINS_TEXT,COINS_RECT)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN1_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    if COINS >= 20:
                        cash(money=-20)
                        sold()
                        inventory_choice(item=1)
                    else:
                        not_enough_money()

                if SKIN2_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    if COINS >= 40:
                        cash(money=-40)
                        sold()
                        inventory_choice(item=2)
                    else:
                        not_enough_money()
                if QUIT_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    shop_menu_window()

                if NEXT_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    shop_window2()


        pygame.display.update()


def levels_window():
    pygame.display.set_caption("Level Selection")

    map_choice(level=0)
    while True:
        LEVELS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")

        LEVEL1_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 100),
                             text_input="LeveL 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL2_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 250),
                                text_input="LeveL 2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL3_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 400),
                             text_input="LeveL 3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL4_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(320, 550),
                               text_input="LeveL 4", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL5_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 100),
                               text_input="LeveL 5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL6_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 250),
                               text_input="LeveL 6", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        LEVEL7_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(950, 400),
                               text_input="LeveL 7", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                               text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")


        for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, LEVEL4_BUTTON, LEVEL5_BUTTON, LEVEL6_BUTTON, LEVEL7_BUTTON, BACK_BUTTON]:
            button.changeColor(LEVELS_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    map_choice(level=1)
                if LEVEL2_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 1:
                        map_choice(level=2)
                    else:
                        not_completed()

                if LEVEL3_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 2:
                        map_choice(level=3)
                    else:
                        not_completed()
                if LEVEL4_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 3:
                        map_choice(level=4)
                    else:
                        not_completed()
                if LEVEL5_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 4:
                        map_choice(level=5)
                    else:
                        not_completed()
                if LEVEL6_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 5:
                        map_choice(level=6)
                    else:
                        not_completed()
                if LEVEL7_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    if ALLOWED_LEVELS >= 6:
                        map_choice(level=7)
                    else:
                        not_completed()
                if BACK_BUTTON.checkForInput(LEVELS_MOUSE_POS):
                    play_window()

        pygame.display.update()

def shop_menu_window():
    pygame.display.set_caption("Shop Menu")
    level_music(level=0)
    while True:
        SHOP_MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        MENU_TEXT = get_font(100).render("SHOP MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        Inventory_button = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 250),
                             text_input="Inventory", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        shop_button = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 450),
                                   text_input="Shop", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 650),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [Inventory_button, shop_button, QUIT_BUTTON]:
            button.changeColor(SHOP_MENU_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Inventory_button.checkForInput(SHOP_MENU_MOUSE_POS):
                    inventory_window()
                if shop_button.checkForInput(SHOP_MENU_MOUSE_POS):
                    shop_window1()
                if QUIT_BUTTON.checkForInput(SHOP_MENU_MOUSE_POS):
                    play_window()


        pygame.display.update()

def play_window():
    pygame.display.set_caption("Game Mode Selection")
    level_music(level=0)
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        MENU_TEXT = get_font(100).render("GAME MODES", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))


        Free_Play_button = Button(image=pygame.image.load("Map Rect.png"), pos=(350, 300),
                             text_input="Free Play", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        level_play_button = Button(image=pygame.image.load("Map Rect.png"), pos=(980, 300),
                                text_input="Levels", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        shop_button = Button(image=pygame.image.load("Map Rect.png"), pos=(350, 550),
                                   text_input="Shop", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        for button in [Free_Play_button, level_play_button, shop_button, QUIT_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_play_button.checkForInput(PLAY_MOUSE_POS):
                    levels_window()
                if Free_Play_button.checkForInput(PLAY_MOUSE_POS):
                    free_play_music()
                    random_number()
                if shop_button.checkForInput(PLAY_MOUSE_POS):
                    shop_menu_window()
                if QUIT_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu_window()


        pygame.display.update()


def credits_window():
    pygame.display.set_caption("Credits")
    while True:
        SCREEN.fill("black")
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()
        CREDIT_TEXT = get_font(150).render("CREDITS", True, "#b68f40")
        CREDIT_RECT = CREDIT_TEXT.get_rect(center=(640, 100))
        INFO_TEXT = get_font(40).render("Made by Sean Steinberg", True, "#b68f40")
        INFO_RECT = CREDIT_TEXT.get_rect(center=(750, 380))
        SCREEN.blit(CREDIT_TEXT, CREDIT_RECT)
        SCREEN.blit(INFO_TEXT,INFO_RECT)
        BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(950, 550),
                             text_input="BACK", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        BACK_BUTTON.changeColor(CREDITS_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(CREDITS_MOUSE_POS):
                    main_menu_window()

        pygame.display.update()




def main_menu_window():
    pygame.display.set_caption("Main Menu")
    map_choice(level=0)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("Map Rect.png"), pos=(640, 400),

                                text_input="Credits", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_window()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits_window()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()




class CameraAwareLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self, target, world_size):
        super().__init__()
        self.target = target
        self.cam = pygame.Vector2(0, 0)
        self.world_size = world_size
        if self.target:
            self.add(target)

    def update(self, *args):
        super().update(*args)
        if self.target:
            x = -self.target.rect.center[0] + SCREEN_SIZE.width / 2
            y = -self.target.rect.center[1] + SCREEN_SIZE.height / 2
            self.cam += (pygame.Vector2((x, y)) - self.cam) * 0.5
            self.cam.x = max(-(self.world_size.width - SCREEN_SIZE.width), min(0, self.cam.x))
            self.cam.y = max(-(self.world_size.height - SCREEN_SIZE.height), min(0, self.cam.y))

    def draw(self, surface):
        spritedict = self.spritedict
        surface_blit = surface.blit
        dirty = self.lostsprites
        self.lostsprites = []
        dirty_append = dirty.append
        init_rect = self._init_rect
        for spr in self.sprites():
            rec = spritedict[spr]
            newrect = surface_blit(spr.image, spr.rect.move(self.cam))
            if rec is init_rect:
                dirty_append(newrect)
            else:
                if newrect.colliderect(rec):
                    dirty_append(newrect.union(rec))
                else:
                    dirty_append(newrect)
                    dirty_append(rec)
            spritedict[spr] = newrect
        return dirty

def map_choice(level):
    level_music(level)
    if level == 1:
        main(Map = (open("maps/map1")))
    if level == 2:
        main(Map = (open("maps/map2")))
    if level == 3:
        main(Map = (open("maps/map3")))
    if level == 4:
        main(Map = (open("maps/map4")))
    if level == 5:
        main(Map = (open("maps/map5")))
    if level == 6:
        main(Map = (open("maps/map6")))
    if level == 7:
        main(Map = (open("maps/map7")))

def segment_choice(RANDOM_NUMBER):
    if RANDOM_NUMBER == 1:
        free_play(segment = (open("map_segments/segment_1")))
    if RANDOM_NUMBER == 2:
        free_play(segment=(open("map_segments/segment_2")))
    if RANDOM_NUMBER == 3:
        free_play(segment=(open("map_segments/segment_3")))
    if RANDOM_NUMBER == 4:
        free_play(segment=(open("map_segments/segment_4")))
    if RANDOM_NUMBER == 5:
        free_play(segment=(open("map_segments/segment_5")))
    if RANDOM_NUMBER == 6:
        free_play(segment=(open("map_segments/segment_6")))
    if RANDOM_NUMBER == 7:
        free_play(segment=(open("map_segments/segment_7")))
    if RANDOM_NUMBER == 8:
        free_play(segment=(open("map_segments/segment_8")))
    if RANDOM_NUMBER == 9:
        free_play(segment=(open("map_segments/segment_9")))
    if RANDOM_NUMBER == 10:
        free_play(segment=(open("map_segments/segment_10")))

def allowed_maps(completed_maps, level):
    if (completed_maps+1) >= level:
        global ALLOWED_LEVELS
        ALLOWED_LEVELS = completed_maps
        return ALLOWED_LEVELS

def cash(money):
    global COINS
    COINS += money





def free_play(segment):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Free Play Mode")
    timer = pygame.time.Clock()

    platforms = pygame.sprite.Group()
    player = Player(platforms, (TILE_SIZE, TILE_SIZE))
    level_width = MAP_BORDER[0] * TILE_SIZE
    level_height = MAP_BORDER[1] * TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))


    hex1 = randint(0,252)
    hex2 = randint(0, 252)
    hex3 = randint(0, 252)

    # build the map_border
    x = y = 0
    for row in segment:
        for col in row:
            if col == "P":
                PlatBasic((x, y), platforms, entities)
            if col == "E":
                PlatExitFree((x, y), platforms, entities)
            if col == "F":
                PlatSpeedF((x, y), platforms, entities)
            if col == "H":
                PlatSpeedH((x, y), platforms, entities)
            if col == "M":
                PlatSpeedM((x, y), platforms, entities)
            if col == "L":
                PlatSpeedL((x, y), platforms, entities)
            if col == "N":
                PlatNorm((x, y), platforms, entities)
            if col == "J":
                PlatJumpH((x, y), platforms, entities)
            if col == "G":
                PlatJumpM((x, y), platforms, entities)
            if col == "S":
                PlatNext((x, y), platforms, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0

    while 1:

        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        entities.update()

        screen.fill((hex1,hex2,hex3))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)



def main(Map):
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE.size)
    pygame.display.set_caption("Level Mode")
    timer = pygame.time.Clock()

    platforms = pygame.sprite.Group()
    player = Player(platforms, (TILE_SIZE, TILE_SIZE))
    level_width = MAP_BORDER[0] * TILE_SIZE
    level_height = MAP_BORDER[1] * TILE_SIZE
    entities = CameraAwareLayeredUpdates(player, pygame.Rect(0, 0, level_width, level_height))

    # build the map_border
    x = y = 0
    for row in Map:
        for col in row:
            if col == "P":
                PlatBasic((x, y), platforms, entities)
            if col == "E":
                PlatExit((x, y), platforms, entities)
            if col == "F":
                PlatSpeedF((x, y), platforms, entities)
            if col == "H":
                PlatSpeedH((x, y), platforms, entities)
            if col == "M":
                PlatSpeedM((x, y), platforms, entities)
            if col == "L":
                PlatSpeedL((x, y), platforms, entities)
            if col == "N":
                PlatNorm((x, y), platforms, entities)
            if col == "J":
                PlatJumpH((x, y), platforms, entities)
            if col == "G":
                PlatJumpM((x, y), platforms, entities)
            if col == "2":
                PlatLevel2((x, y), platforms, entities)
            if col == "3":
                PlatLevel3((x, y), platforms, entities)
            if col == "4":
                PlatLevel4((x, y), platforms, entities)
            if col == "5":
                PlatLevel5((x, y), platforms, entities)
            if col == "6":
                PlatLevel6((x, y), platforms, entities)
            if col == "7":
                PlatLevel3((x, y), platforms, entities)
            if col == "0":
                PlatMoving((x, y), platforms, entities)
            x += TILE_SIZE
        y += TILE_SIZE
        x = 0

    while 1:

        for e in pygame.event.get():
            if e.type == QUIT:
                return
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                return

        entities.update()

        screen.fill((0, 0, 0))
        entities.draw(screen)
        pygame.display.update()
        timer.tick(60)






class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, *groups):
        super().__init__(*groups)
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


class Player(Entity,):
    def __init__(self, platforms, pos, *groups):
        super().__init__(Color("#5aa2e0"), pos)
        self.image = pygame.image.load(CHARACTER_SKINS).convert()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.vel = pygame.Vector2((0, 0))
        self.onGround = False
        self.platforms = platforms
        self.speed = 8
        self.jump_strength = 10

    def update(self):
        pressed = pygame.key.get_pressed()
        up = pressed[K_SPACE]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]
        running = pressed[K_UP]
        quit = pressed[K_ESCAPE]

        if quit:
            pygame.quit()
            sys.exit()
        if up:
            # only jump if on the ground
            if self.onGround: self.vel.y = -self.jump_strength
        if left:
            self.vel.x = -self.speed
        if right:
            self.vel.x = self.speed
        if running:
            self.vel.x *= 1.5
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.vel += GRAVITY
            # max falling speed
            if self.vel.y > 100: self.vel.y = 100
        if not (left or right):
            self.vel.x = 0
        # increment in x direction
        self.rect.left += self.vel.x
        # do x-axis collisions
        self.collide(self.vel.x, 0, self.platforms)
        # increment in y direction
        self.rect.top += self.vel.y
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.vel.y, self.platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, PlatExit):
                    music_effect(1)
                    time.sleep(0.3)
                    SCREEN.fill((255, 0, 0))
                    my_font = pygame.font.SysFont('Comic Sans MS', 250)
                    font_render = my_font.render('WASTED', False, (0, 0, 0))
                    SCREEN.blit(font_render,(100,150))
                    pygame.display.update()
                    time.sleep(1.95)
                    levels_window()

                if isinstance(p, PlatExitFree):
                    music_effect(1)
                    time.sleep(0.3)
                    SCREEN.fill((255, 0, 0))
                    my_font = pygame.font.SysFont('Comic Sans MS', 250)
                    font_render = my_font.render('WASTED', False, (0, 0, 0))
                    SCREEN.blit(font_render,(100,150))
                    pygame.display.update()
                    time.sleep(1.95)
                    play_window()

                if isinstance(p, PlatNext):
                    cash(money=10)
                    random_number()



                if isinstance(p, PlatLevel2):
                    allowed_maps(completed_maps=1, level=2)
                    cash(money=10)
                    map_choice(level=2)


                if isinstance(p, PlatLevel3):
                    allowed_maps(completed_maps=2, level=3)
                    cash(money=20)
                    map_choice(level=3)


                if isinstance(p, PlatLevel4):
                    allowed_maps(completed_maps=3, level=4)
                    cash(money=30)
                    map_choice(level=4)


                if isinstance(p, PlatLevel5):
                    allowed_maps(completed_maps=4, level=5)
                    map_choice(level=5)
                    cash(money=40)


                if isinstance(p, PlatLevel6):
                    allowed_maps(completed_maps=5, level=6)
                    cash(money=50)
                    map_choice(level=6)


                if isinstance(p, PlatLevel7):
                    allowed_maps(completed_maps=8, level=9)
                    cash(money=60)
                    map_choice(level=7)

                if isinstance(p, PlatSpeedF):
                    self.speed = 300

                if isinstance(p, PlatSpeedH):
                    self.speed = 50
                if isinstance(p, PlatSpeedM):
                    self.speed = 16
                if isinstance(p, PlatSpeedL):
                    self.speed = 5



                if isinstance(p, PlatNorm):
                    self.speed = 8
                    self.jump_strength = 10

                if isinstance(p, PlatJumpH):
                    self.jump_strength = 30

                if isinstance(p, PlatJumpM):
                    self.jump_strength = 15



                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.vel.y = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom






class PlatLevel2(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)
class PlatLevel3(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)
class PlatLevel4(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)
class PlatLevel5(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)
class PlatLevel6(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)
class PlatLevel7(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)



class PlatBasic(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)

class PlatMoving(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#10eb93"), pos, *groups)

    def update(self):
        self.x += 10 * self.dx

class PlatExit(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)

class PlatExitFree(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#c40c0c"), pos, *groups)

class PlatSpeedF(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatSpeedH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatSpeedM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatSpeedL(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatNorm(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)


class PlatJumpH(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatJumpM(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatImmune(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#0033FF"), pos, *groups)

class PlatNext(Entity):
    def __init__(self, pos, *groups):
        super().__init__(Color("#b154eb"), pos, *groups)

def level_music(level):
    music = ["Music/madirfan-hidden-place-extended-version-13891.mp3",
             "Music/this-minimal-technology-pure-12327.mp3",
             "Music/slow-trap-18565.mp3",
             "Music/bensound-summer_ogg_music.ogg",
             "Music/tropical-house-112360.mp3",
             "Music/sport-fashion-rock-95426.mp3",
             "Music/sport-fashion-rock-95426.mp3",
             "Music/sport-fashion-rock-95426.mp3 "]
    mixer.init()
    mixer.music.load(music[level])
    mixer.music.play()

def free_play_music():
    music = ["Music/madirfan-hidden-place-extended-version-13891.mp3",
             "Music/this-minimal-technology-pure-12327.mp3",
             "Music/slow-trap-18565.mp3",
             "Music/bensound-summer_ogg_music.ogg",
             "Music/tropical-house-112360.mp3",
             "Music/sport-fashion-rock-95426.mp3",
             "Music/sport-fashion-rock-95426.mp3",
             "Music/sport-fashion-rock-95426.mp3 "]
    random_number = randint(1,7)
    mixer.init()
    for i in range(7):
        mixer.music.load(music[random_number])
        mixer.music.play()

def music_effect(sound_effect):
    music = ["Music/gta-v-death-sound-effect-102.mp3"]
    mixer.init()
    mixer.music.load(music[sound_effect-1])
    mixer.music.play()





while True:
    inventory_choice(item=0)
    main_menu_window()

