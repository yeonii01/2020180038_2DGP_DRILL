from pico2d import *
open_canvas()

sprite = load_image('sprite_sheet.png')

frame = 0
y = 100
while True:
    for x in range(100, 150, 10):
        clear_canvas()
        sprite.clip_draw(frame*44,70,50,30,x,50)
        update_canvas()
        frame = (frame+1) % 5
        delay(0.1)
        get_events()
    for x in range(100, 180, 10):
        clear_canvas()
        sprite.clip_draw(frame*40,100,40,40,400,x)
        update_canvas()
        frame = (frame+1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame*40,140,40,40,x,400)
        update_canvas()
        frame = (frame+1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame * 40, 180, 40, 40, x, 400)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 260, 10):
        clear_canvas()
        sprite.clip_draw(frame*40,220,40,40,x,400)
        update_canvas()
        frame = (frame+1) % 8
        delay(0.1)
        get_events()
    for x in range(140, 100-1, -5):
        clear_canvas()
        sprite.clip_draw(frame*40,260,40,40,400,x)
        update_canvas()
        frame = (frame+1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame*40,300,40,40,x,y)
        update_canvas()
        frame = (frame+1) % 8
        y -= 5
        delay(0.1)
        get_events()
    y = 100
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame * 40, 340, 40, 40, 100, 400)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame * 40, 380, 40, 40, x, 400)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 140, 5):
        clear_canvas()
        sprite.clip_draw(frame * 40, 420, 40, 40, 100, 400)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()
    for x in range(100, 180, 10):
        clear_canvas()
        sprite.clip_draw(frame * 40, 460, 40, 40, x, 400)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.1)
        get_events()
close_canvas()