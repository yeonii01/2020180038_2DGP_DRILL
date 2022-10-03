from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirx, diry
    global lastdirx
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirx += 1
                lastdirx = 1
            elif event.key == SDLK_LEFT:
                lastdirx = 2
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                lastdirx = 2
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1
    pass

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dirx = 0
diry = 0
lastdirx = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dirx == 0 and diry == 0 and lastdirx == 1:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    elif dirx == 0 and diry == 0 and lastdirx == 2:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
    elif dirx == 1 or lastdirx == 1:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif dirx == -1 or lastdirx == 2:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    update_canvas()

    handle_events()

    if x < 1280 and dirx == 1:
        x += dirx * 5
    elif x > 0 and dirx == -1:
        x += dirx * 5
    if y < 1024 and diry == 1:
        y += diry * 5
    elif y > 0 and diry == -1:
        y += diry * 5
    frame = (frame + 1) % 8
    delay(0.01)

close_canvas()