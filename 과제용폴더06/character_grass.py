from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

startx = 400
starty = 90
rad = 0
r = 50


while rad<720:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(startx+math.cos(rad/360)*r*math.pi, (starty+r+100)+math.sin(rad/360)*r*math.pi)
    rad= rad+2
    delay(0.01)

close_canvas()
