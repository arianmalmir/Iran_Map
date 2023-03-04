import pyray as pr
pr.init_window(1080,720,"oft")

press = False

img = pr.load_texture("assets/Kerman.png")
button = pr.Rectangle(10,5,20,50)
pr.draw_texture_rec(img,button,pr.Vector2(10,5),pr.WHITE)

while not pr.window_should_close():

    pr.begin_drawing()
    pr.clear_background(pr.WHITE)


    
    mouse = pr.get_mouse_position()
    pr.draw_rectangle(10,5,20,50,pr.GREEN)
    pr.draw_text("miumen",15,2,10,pr.BLACK)

    if (pr.check_collision_point_rec(mouse , button)):
        
        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")
        
    else:
        press = False



    
    pr.end_drawing()