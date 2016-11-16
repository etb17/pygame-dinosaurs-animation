
# Computer Programming 1
# Evan Budelmann
# 11/11/
# Dinosaurs running from extinction.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Dinosaurs"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (39, 109, 25)
WHITE = (216, 153, 130)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
DINO = (6, 53, 7)
TAN = (178, 140, 80)
DARKTAN = (209, 197, 163)
DIRT = (81, 81, 35)
BLACK = (0, 0, 0)
GRAY = (119, 115, 104)
BROWN = (66, 48, 7)
RED = (153, 46, 16)

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    
def draw_dinosaurs(x, y):
    pygame.draw.polygon(screen, DINO, [[x + 45, y],[x + 40, y + 25], [x + 15, y + 25], [x , y + 20], [x + 5, y + 10]])
    pygame.draw.ellipse(screen, DINO, [x + 25, y + 10, 65, 30])
    if frame == 0:
        pygame.draw.rect(screen, DINO, [x + 25, y + 25, 10, 25])
        pygame.draw.rect(screen, DINO , [x + 75, y + 25, 10, 25])
    elif frame == 1:
        pygame.draw.rect(screen, DINO, [x + 25, y + 20, 10, 25])
        pygame.draw.rect(screen, DINO , [x + 75, y + 25, 10, 25])

    elif frame == 2:
        pygame.draw.rect(screen, DINO, [x + 25, y + 25, 10, 25])
        pygame.draw.rect(screen, DINO , [x + 75, y + 20, 10, 25])

    pygame.draw.rect(screen, GRAY, [x +5, y + 5, 3, 5])
    pygame.draw.rect(screen, GRAY, [x + 15, y + 5, 20, 3])
    pygame.draw.ellipse(screen, GRAY, [x - 1, y + 16, 7, 6])
    pygame.draw.ellipse(screen, BLACK, [x + 25, y + 10, 2, 2])
    
def draw_dust(x, y, r):
    pygame.draw.ellipse(screen, TAN, [x, y, r, r])
    pygame.draw.ellipse(screen, DARKTAN, [x + 1, y + 2, r - 1, r - 1])
    
def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [x + 35, y + 50, 20, 100])
    pygame.draw.ellipse(screen, GREEN, [x, y, 100, 100])
    
def draw_background(x, y):
    pygame.draw.polygon(screen, BLACK, [[x + 20, y], [x - 90, y + 200], [x + 110, y + 200]])
    pygame.draw.polygon(screen, DINO, [[x + 10, y], [x - 90, y + 200], [x + 110, y + 200]])
    pygame.draw.polygon(screen, GREEN, [[x, y], [x - 100, y + 200], [x + 100, y + 200]])
    pygame.draw.rect(screen, DINO, [0, 300, 800, 110])
    
def draw_trex(x, y):
    if frame == 0:
        pygame.draw.polygon(screen, BLACK, [[x, y], [x - 10, y], [x - 15, y + 5], [x - 30, y + 5], [x - 60, y + 25], [x - 85, y + 25], [x - 100, y + 30], [x - 105, y + 35], [x - 110, y + 45], [x - 105, y + 55], [x - 100, y + 65], [x - 95, y + 75], [x - 90, y + 80], [x - 80, y + 85], [x - 15, y + 95], [x + 20, y + 95], [x + 20, y + 90], [x + 70, y + 110], [x + 70, y + 55] , [x + 55, y + 45], [x + 20, y + 25] , [x + 10 , y + 10], [x + 5, y + 5]])
        pygame.draw.ellipse(screen, BLACK, [x + 55, y + 30, 200, 100])
    elif frame == 1:
        pygame.draw.polygon(screen, BLACK, [[x, y + 1], [x - 10, y + 1], [x - 15, y + 6], [x - 30, y + 6], [x - 60, y + 26], [x - 85, y + 26], [x - 100, y + 31], [x - 105, y + 36], [x - 110, y + 46], [x - 105, y + 56], [x - 100, y + 66], [x - 95, y + 76], [x - 90, y + 81], [x - 80, y + 86], [x - 15, y + 96], [x + 20, y + 96], [x + 20, y + 91], [x + 70, y + 111], [x + 70, y + 56] , [x + 55, y + 46], [x + 20, y + 26] , [x + 10 , y + 11], [x + 5, y + 6]])
        pygame.draw.ellipse(screen, BLACK, [x + 55, y + 31, 200, 100])        
    elif frame == 2:
        pygame.draw.polygon(screen, BLACK, [[x, y], [x - 10, y], [x - 15, y + 5], [x - 30, y + 5], [x - 60, y + 25], [x - 85, y + 25], [x - 100, y + 30], [x - 105, y + 35], [x - 110, y + 45], [x - 105, y + 55], [x - 100, y + 65], [x - 95, y + 75], [x - 90, y + 80], [x - 80, y + 85], [x - 15, y + 95], [x + 20, y + 95], [x + 20, y + 90], [x + 70, y + 110], [x + 70, y + 55] , [x + 55, y + 45], [x + 20, y + 25] , [x + 10 , y + 10], [x + 5, y + 5]]) 
        pygame.draw.ellipse(screen, BLACK, [x + 55, y + 30, 200, 100])

    ''' make clouds '''
clouds = []
for i in range(150):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    clouds.append([x, y])
    
'''make dinosaurs'''
dinosaurs = []
for i in range(100):
    x = random. randrange (-100, 1600)
    y = random.randrange (400, 800)
    speed = random.randrange(5, 10)
    dinosaurs.append([x, y, speed])
    
'''make trex'''
trex = []
for i in range(1):
    x = 910
    y = 150
    trex.append([x, y])
    
'''make dust'''
dust = []
for i in range (400):
    x = random.randrange (-100, 1600)
    y = random.randrange (400, 800)
    r = random.randrange (5, 15)
    dust.append([x, y, r])


t_rex_move = False
pygame.mixer.music.load('jpark.mp3')
pygame.mixer.music.play(-1)
# Game loop
done = False
ticks = 0
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                t_rex_move = True

    # Game logic
    frame = ticks // 10
    ticks += 1

    if ticks >= 30:
        ticks = 0
    ''' move clouds '''
    for c in clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)
    '''move dinosuars'''
    for s in dinosaurs:
        s[0] -= s[2]
        if s[0] < -100:
            s[0] = random.randrange(800, 1600)
            s[1] = random.randrange(400, 800)
    '''move rex'''
    for t in trex:
        if t_rex_move == True:
            
            t[0] -= 3
            if t[0] < -250:
                t[0] = 910
                t[1] = 150
                t_rex_move = False
    '''move dust'''
    for d in dust:
        d[0] += 3
        d[1] -= 1
        
        if d[0] > 815:
            d[0] = random.randrange(-800, 800)
            d[1] = random.randrange (400, 800)
        if d[1] < 300:
            d[0] = random.randrange(-800, 800 )
            d[1] = random.randrange (400, 800)
    # Drawing code
    ''' sky '''
    screen.fill(RED)
    pygame.draw.rect(screen, DINO, [0, 300, 800, 200])
    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' grass '''
    pygame.draw.rect(screen, DIRT, [0, 400, 800, 200])
    y = 200
    '''trex'''
    for t in trex:
        draw_trex(t[0], t[1])
    '''background'''
    for x in range(-100, 800, 50):
        draw_background(x, y)
    ''' tree '''
    y = 280
    for x in range(-100, 800, 50):
        draw_tree(x, y)

    '''dinosaurs'''
    for s in dinosaurs:
        draw_dinosaurs(s[0], s[1])

    '''dust'''
    for d in dust:
        draw_dust(d[0], d[1], d[2])
        
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
