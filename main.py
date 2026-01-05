import pygame, random, tkinter

# ARROW - PLAYER 1
# WASD - PLAYER 2

# CREATE SKINS FOR BOTH P1 AND P2
# TAG GAME

x = pygame.init()
root = tkinter.Tk()
pcspecs = (root.winfo_screenwidth(),root.winfo_screenheight())
           
pygame.mixer.init()
character_index_1 = 0
character_index_2 = 1

pygame.font.get_fonts()
font = pygame.font.SysFont('arialblue', 60)

def tex(text, greenor, x, y) : 
    screen_text = font.render(str(text), True, greenor)
    win.blit(screen_text, [x,y])


# BASIC SETTING 
win = pygame.display.set_mode(pcspecs, pygame.FULLSCREEN)
pygame.display.set_caption("Something, I don't know")
pygame.display.update()
clock = pygame.time.Clock()

# IMAGE SETUP
menu_bg = pygame.transform.scale(pygame.image.load("images/background.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()
blimg = pygame.transform.scale(pygame.image.load("images/blur.png"), (pcspecs[0], pcspecs[1])).convert_alpha()
start = pygame.transform.scale(pygame.image.load("images/title.png"), (pcspecs[0]/1.7, pcspecs[1]/9)).convert_alpha()
volumeimg = pygame.transform.scale(pygame.image.load("images/vol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
no_volumeimg = pygame.transform.scale(pygame.image.load("images/novol.png"), (pcspecs[0]/34, pcspecs[1]/18)).convert_alpha()
gameoverimg = pygame.transform.scale(pygame.image.load("images/over.png"), (650,90)).convert_alpha() 
resetimg = pygame.transform.scale(pygame.image.load("images/reset.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()
menuimg = pygame.transform.scale(pygame.image.load("images/menu.png") , (pcspecs[0]/2,pcspecs[1]/30)).convert_alpha()
arrowimg = pygame.transform.scale(pygame.image.load("images/arrow.png"), (35, 35)).convert_alpha()

# PLATFORMS (drawn as rectangles instead of image sprites)
# Color for platform fill and optional border
platform_color = (120, 72, 18)  # brown-ish
platform_border = (30, 20, 10)

# CHARACTERS
char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (40, 40)).convert_alpha()
char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (40, 40)).convert_alpha()

default_volume = True                   # Volume button boolean

def loadscreen() : 
    global character_index_1, character_index_2
    exit_game = False 
    char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (60, 60)).convert_alpha()
    char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (60, 60)).convert_alpha()
    playbutton_img = pygame.transform.scale(pygame.image.load("images/playbutton1.png"), (pcspecs[0]/6.8,pcspecs[1]/25)).convert_alpha()
    playbutton_dimension = (pcspecs[0]//3+10, pcspecs[1]//2+200)
    volumebutton_dimension = (pcspecs[0]-100, 50)
    leftarrow1_dimension = (pcspecs[0]//2+100, pcspecs[1]//2-90)
    rightarrow1_dimension = (pcspecs[0]//2+225, leftarrow1_dimension[1])
    leftarrow2_dimension = (pcspecs[0]//2-200, leftarrow1_dimension[1])
    rightarrow2_dimension = (pcspecs[0]//2-75, leftarrow1_dimension[1])
    playbutton_rect = pygame.Rect(playbutton_dimension[0], playbutton_dimension[1], pcspecs[0]/3, pcspecs[1]/15)
    volumebutton_rect = pygame.Rect(volumebutton_dimension[0], volumebutton_dimension[1], pcspecs[0]/27, pcspecs[1]/14.5)
    leftbutton1_rect = pygame.Rect(leftarrow1_dimension[0], leftarrow1_dimension[1], 35, 35)
    rightbutton1_rect = pygame.Rect(rightarrow1_dimension[0], rightarrow1_dimension[1], 35, 35)
    leftbutton2_rect = pygame.Rect(leftarrow2_dimension[0], leftarrow2_dimension[1], 35, 35)
    rightbutton2_rect = pygame.Rect(rightarrow2_dimension[0], rightarrow2_dimension[1], 35, 35)
    leftarrow1 = pygame.transform.scale(pygame.image.load("images/left1.png"), (35,35)).convert_alpha() 
    leftarrow2 = pygame.transform.scale(pygame.image.load("images/left2.png"), (35,35)).convert_alpha() 
    rightarrow1 = pygame.transform.scale(pygame.image.load("images/right1.png"), (35,35)).convert_alpha() 
    rightarrow2 = pygame.transform.scale(pygame.image.load("images/right2.png"), (35,35)).convert_alpha() 
    pygame.mixer.music.load("music/game sound3.mp3")
    global default_volume
    pygame.mixer.music.play(loops=10)
    while not exit_game : 
        win.blit(menu_bg, (0,0))
        win.blit(char2_img, (pcspecs[0]//2-150, pcspecs[1]//2-100))
        win.blit(char1_img, (pcspecs[0]//2+150, pcspecs[1]//2-100))
        win.blit(start, (pcspecs[0]//5, pcspecs[1]/7.2))
        pygame.draw.rect(win, (63, 0, 93), playbutton_rect)
        pygame.draw.rect(win, (255,255,255), volumebutton_rect)
        pygame.draw.rect(win, (0, 0, 0), leftbutton1_rect)
        pygame.draw.rect(win, (0, 0, 0), rightbutton1_rect)
        pygame.draw.rect(win, (0, 0, 0), leftbutton2_rect)
        pygame.draw.rect(win, (0, 0, 0), rightbutton2_rect)
        win.blit(leftarrow1, leftarrow1_dimension)
        win.blit(rightarrow1, rightarrow1_dimension)
        win.blit(leftarrow2, leftarrow2_dimension)
        win.blit(rightarrow2, rightarrow2_dimension)
        win.blit(playbutton_img, (playbutton_dimension[0]+(playbutton_dimension[0]/3-10), playbutton_dimension[1]+10))

        if default_volume:
            win.blit(volumeimg, (volumebutton_dimension[0]+5, volumebutton_dimension[1]+5))
            pygame.mixer.music.unpause()
        else:
            win.blit(no_volumeimg, (volumebutton_dimension[0]+5, volumebutton_dimension[1]+5))
            pygame.mixer.music.pause()

        # BUTTON FUNCTIONALITY
        pygame.time.delay(100)
        for event in pygame.event.get():
            mloc = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if volumebutton_rect.collidepoint(mloc):
                    default_volume = not default_volume
                elif playbutton_rect.collidepoint(mloc): 
                    if default_volume :
                        pygame.mixer.music.load("music/ingame music3.mp3")
                        pygame.mixer.music.play(loops=10)
                    gameloop()
                if leftbutton1_rect.collidepoint(mloc) :
                    character_index_1 -= 1
                    if character_index_1 == character_index_2 : 
                        character_index_1 -= 1
                    if character_index_1 < 0 :
                        character_index_1 = 9
                if leftbutton2_rect.collidepoint(mloc) :
                    character_index_2 -= 1
                    if character_index_1 == character_index_2 : 
                        character_index_2 -= 1
                    if character_index_2 < 0 :
                        character_index_2 = 9
                if rightbutton1_rect.collidepoint(mloc) :
                    character_index_1 += 1
                    if character_index_1 == character_index_2 : 
                        character_index_1 += 1
                    if character_index_1 > 9 :
                        character_index_1 = 0
                if rightbutton2_rect.collidepoint(mloc) :
                    character_index_2 += 1
                    if character_index_1 == character_index_2 : 
                        character_index_2 += 1
                    if character_index_2 > 9 :
                        character_index_2 = 0
                char1_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_1}.png"), (60, 60)).convert_alpha()
                char2_img = pygame.transform.scale(pygame.image.load(f"images/skins/{character_index_2}.png"), (60, 60)).convert_alpha()
                

            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_ESCAPE : 
                    quit()

        pygame.display.update()
        clock.tick(60)



def gameloop() : 
    # Improved physics implementation
    global char1_img, char2_img
    turn = random.randint(0, 1)
    clock = pygame.time.Clock()
    counter = 30
    countdown = str(counter)
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # Physics constants (tweak these to taste)
    GRAVITY = 1.2
    JUMP_VELOCITY = -20
    MOVE_SPEED = 7

    platformlist = [
        (pcspecs[0] // 4, 75, 700, 30),
        (pcspecs[0] // 2, 175, 350, 30),
        (pcspecs[0] // 5, 300, 350, 30),
        (pcspecs[0] // 2 + 100, 300, 350, 30),
        (pcspecs[0] // 7, 450, 175, 30),
        (pcspecs[0] // 2, 450, 175, 30),
        (pcspecs[0] // 4, 620, 350, 30),
        (pcspecs[0] // 2 + 200, 600, 175, 30)
    ]

    ingame_bg = pygame.transform.scale(pygame.image.load("images/image.jpg"), (pcspecs[0], pcspecs[1])).convert_alpha()

    # Positions and velocities
    char1_x, char1_y = 10.0, 700.0
    char2_x, char2_y = 500.0, 700.0
    char1_vx, char1_vy = 0.0, 0.0
    char2_vx, char2_vy = 0.0, 0.0
    in_air1, in_air2 = False, False

    exit_game = False
    game_over = False
    last = pygame.time.get_ticks()

    # helper to get rects
    def player_rect(x, y, img):
        return pygame.Rect(int(x), int(y), img.get_width(), img.get_height())

    # main loop
    while not exit_game:
        if game_over:
            if turn == 0:
                winimg = pygame.image.load("images/winner1.png")
            else:
                winimg = pygame.image.load("images/winner2.png")

            winimg = pygame.transform.scale(winimg, (400, 50))

            win.blit(gameoverimg, (360, 120))
            win.blit(blimg, (0, 0))
            win.blit(winimg, (pcspecs[0] / 4, pcspecs[1] / 3))
            win.blit(resetimg, (pcspecs[0] / 4, 1.5 * pcspecs[1] / 3))
            win.blit(menuimg, ((pcspecs[0] / 4, 1.8 * pcspecs[1] / 3)))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                    if event.key == pygame.K_ESCAPE:
                        loadscreen()

        else:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    counter -= 1
                    countdown = str(counter) if counter > 0 else '0'
                    if counter <= 0:
                        game_over = True

                if event.type == pygame.QUIT:
                    exit_game = True

                # KEYDOWN -> start movement or jump
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        loadscreen()

                    # Player 2 (WASD)
                    if event.key == pygame.K_d:
                        speed = 3 if turn == 1 else 0
                        char2_vx = MOVE_SPEED + speed
                    elif event.key == pygame.K_a:
                        speed = 3 if turn == 1 else 0
                        char2_vx = - (MOVE_SPEED + speed)
                    elif event.key == pygame.K_w:
                        if not in_air2:
                            char2_vy = JUMP_VELOCITY
                            in_air2 = True

                    # Player 1 (arrow keys)
                    if event.key == pygame.K_RIGHT:
                        speed = 3 if turn == 0 else 0
                        char1_vx = MOVE_SPEED + speed
                    elif event.key == pygame.K_LEFT:
                        speed = 3 if turn == 0 else 0
                        char1_vx = - (MOVE_SPEED + speed)
                    elif event.key == pygame.K_UP:
                        if not in_air1:
                            char1_vy = JUMP_VELOCITY
                            in_air1 = True

                # KEYUP -> stop horizontal movement when keys released
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_d, pygame.K_a):
                        char2_vx = 0
                    if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                        char1_vx = 0

            # Apply horizontal velocities
            char1_x += char1_vx
            char2_x += char2_vx

            # Apply gravity and vertical movement
            char1_vy += GRAVITY
            char1_y += char1_vy

            char2_vy += GRAVITY
            char2_y += char2_vy

            # Ground collision
            GROUND_Y = 700
            if char1_y >= GROUND_Y:
                char1_y = GROUND_Y
                char1_vy = 0
                in_air1 = False
            if char2_y >= GROUND_Y:
                char2_y = GROUND_Y
                char2_vy = 0
                in_air2 = False

            # Platform collisions (only when falling)
            def resolve_platform_collision(x, y, vy, img):
                rect = player_rect(x, y, img)
                # previous bottom to avoid tunnelling check could be improved; this is a simple check
                for px, py, pw, ph in platformlist:
                    plat_rect = pygame.Rect(px, py, pw, ph)
                    # check if player is overlapping horizontally
                    if rect.right > plat_rect.left + 5 and rect.left < plat_rect.right - 5:
                        # only handle collision when coming from above (falling)
                        if vy >= 0 and rect.bottom >= plat_rect.top and rect.bottom <= plat_rect.top + ph:
                            # snap to platform top
                            new_y = plat_rect.top - img.get_height()
                            return new_y, 0.0, False
                return y, vy, True if vy != 0 else False

            char1_y, char1_vy, in_air1 = resolve_platform_collision(char1_x, char1_y, char1_vy, char1_img)
            char2_y, char2_vy, in_air2 = resolve_platform_collision(char2_x, char2_y, char2_vy, char2_img)

            # Wrap-around horizontally
            if char1_x < 0:
                char1_x = pcspecs[0]
            elif char1_x > pcspecs[0]:
                char1_x = 0
            if char2_x < 0:
                char2_x = pcspecs[0]
            elif char2_x > pcspecs[0]:
                char2_x = 0

            # Tagging: when close, and enough time has passed, swap turn and reset timer
            dist_x = abs(char1_x - char2_x)
            dist_y = abs(char1_y - char2_y)
            if dist_x < 40 and dist_y < 50:
                now = pygame.time.get_ticks()
                if now - last >= 2000:
                    # swap who is "it"
                    turn = 1 - turn
                    last = now

            # Draw everything
            win.blit(ingame_bg, (0, 0))
            tex(countdown, (0, 0, 0), pcspecs[0] // 2 - 50, 10)

            for platform in platformlist:
                px, py, pw, ph = platform
                # Draw filled rectangle for each platform and a subtle border
                pygame.draw.rect(win, platform_color, (px, py, pw, ph))
                pygame.draw.rect(win, platform_border, (px, py, pw, ph), 2)

            win.blit(char1_img, (int(char1_x), int(char1_y)))
            win.blit(char2_img, (int(char2_x), int(char2_y)))

            if turn == 0:
                win.blit(arrowimg, (int(char1_x), int(char1_y) - 50))
            else:
                win.blit(arrowimg, (int(char2_x), int(char2_y) - 50))

        pygame.display.update()
        clock.tick(60)
      
    
loadscreen()
    
    
    