from pico2d import *

open_canvas(1280, 1024)

ground = load_image('TUK_GROUND.png')
character = load_image('wolfSprite.png')

def handle_events():
    global running, dirx, diry, lastdir

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
                lastdir = 1
            elif event.key == SDLK_LEFT:
                dirx += 1
                lastdir = 2
            elif event.key == SDLK_UP:
                diry -= 1
                lastdir = 3
            elif event.key == SDLK_DOWN:
                diry += 1
                lastdir = 4

def move_character():
    global x, y

    if dirx == 1 and diry == 0 and x < 1214:
        x += 5
    elif dirx == -1 and diry == 0 and x > 0:
        x -= 5
    elif dirx == 0 and diry == 1 and y < 962:
        y += 5
    elif dirx == 0 and diry == -1 and y > 0:
        y -= 5

def character_draw():
    if dirx == 0 and diry == 0: # Idle 애니메이션
        if lastdir == 1:
            character.clip_draw(frame * 65 + 318, 289, 64, 40, x, y, 150, 150)
        elif lastdir == 2:
            character.clip_draw(frame * 65 + 318, 97, 65, 40, x, y, 150, 150)
        elif lastdir == 3:
            character.clip_draw(frame * 32 + 160, 257, 32, 62, x, y, 150, 150)
        elif lastdir == 4:
            character.clip_draw(frame * 32, 257, 32, 62, x, y, 150, 150)
    elif dirx == 1 and diry == 0: # 오른쪽 진행 애니메이션
        character.clip_draw(frame * 65 + 318, 257, 64, 31, x, y, 150, 150)
    elif dirx == -1 and diry == 0: # 왼쪽 진행 애니메이션
        character.clip_draw(frame * 65 + 318, 64, 63, 32, x, y, 150, 150)
    elif dirx == 0 and diry == 1: # 위쪽 진행 애니메이션
        character.clip_draw(frame * 32 + 160, 195, 32, 62, x, y, 150, 150)
    elif dirx == 0 and diry == -1: # 아래쪽 진행 애니메이션
        character.clip_draw(frame * 32, 193, 32, 62, x, y, 150, 150)
    else:
        character.clip_draw(frame * 65 + 318, 289, 64, 40, x, y, 150, 150)

running = True
x = 1280 // 2
y = 1024 // 2
frame = 0
dirx = 0
diry = 0
lastdir = 1

while running:
    clear_canvas()
    ground.draw(640, 512)
    handle_events()
    move_character()
    character_draw()
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.15)

close_canvas()