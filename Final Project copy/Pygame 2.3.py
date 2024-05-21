import pgzrun

WIDTH = 1236
HEIGHT = 725

score = 0
#sprites 
Player1 = Actor('frump1')
Player1.pos = (618, 70)
Player2 = Actor('putin2')
Player2.pos = (618, 600)

#background
Towers = Actor('towers')
Towers.pos = (618, 362.5)
Backcolor = Rect((0,0), (10000,10000))

#bricks
Brick1 = Actor('brick')
Brick1.pos = (-100, 70)
Brick2 = Actor('brick')
Brick2.pos = (-100, 70)
Brick3 = Actor('brick')
Brick3.pos = (-100, 70)
Brick4 = Actor('brick')
Brick4.pos = (-100, 70)
Brick5 = Actor('brick')
Brick5.pos = (-100, 70)
Brick6 = Actor('brick')
Brick6.pos = (-100, 70)
Brick7 = Actor('brick')
Brick7.pos = (-100, 70)

#pixel under putin
box = Rect((618,700), (10,1))

#gravity
gravity = 5
jump_height = -150

def draw():
    screen.clear()
    Towers.draw()
    Player2.draw()
    Player1.draw()
    Brick1.draw()
    Brick2.draw()
    Brick3.draw()
    Brick4.draw()
    Brick5.draw()
    Brick6.draw()
    Brick7.draw()
    screen.draw.filled_rect(box,"black")

def update():

    #player 2
    if keyboard.K_RIGHT:
        Player2.x += 6
        box.x += 6
    if keyboard.K_LEFT:
        Player2.x = Player2.x - 6
        box.x -= 6
    if Player2.x < 0:
        Player2.x = WIDTH
    if Player2.x > WIDTH:
        Player2.x = 0
        

    #player 1
    if keyboard.d:
        Player1.x += 7
    if keyboard.a:
        Player1.x = Player1.x - 7
    if Player1.x < 0:
        Player1.x = WIDTH
    if Player1.x > WIDTH:
        Player1.x = 0

    #jumping & bricks
    if keyboard.K_SPACE and Player2.colliderect(box):
        Player2.y += jump_height


    if keyboard.K_1:
        Brick1.pos = Player1.pos
    if keyboard.K_2:
        Brick2.pos = Player1.pos
    if keyboard.K_3:
        Brick3.pos = Player1.pos
    if keyboard.K_4:
        Brick4.pos = Player1.pos
    if keyboard.K_5:
        Brick5.pos = Player1.pos
    if keyboard.K_6:
        Brick6.pos = Player1.pos
    if keyboard.K_7:
        Brick7.pos = Player1.pos

    
    if Player2.colliderect(box):
        Player2.y = box.y - 50

    if box.x < 0:
        box.x = WIDTH
    if box.x > WIDTH:
        box.x = 0
        
    #gravity 2
    Brick1.y += gravity + 10
    Brick2.y += gravity + 10
    Brick3.y += gravity + 10
    Brick4.y += gravity + 10
    Brick5.y += gravity + 10
    Brick6.y += gravity + 10
    Brick7.y += gravity + 10
    Player2.y += gravity

    #score
    global score
    if Player2.colliderect(Brick1):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick2):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick3):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick4):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick5):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick6):
        score = score + 1
        print("Hit",
              score)
    if Player2.colliderect(Brick7):
        score = score + 1
        print("Hit",
              score)

    if score > 200:
        print('''





HOW COULD YOU DIE YOU ACTUAL EGG!!!!!!''')
        exit()

        


        

pgzrun.go()
