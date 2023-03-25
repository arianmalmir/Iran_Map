import pyray as pr 
from Transform import *
from Map import Map

pr.init_window(1080, 720, "Iran Map")

ir_map = Map(0, -10)
ir_map.create_states()

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
 
    mousePoint = pr.get_mouse_position()

    for s in ir_map.States:
        s.draw()

    pr.end_drawing()
