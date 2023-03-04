from pyray import (
    load_image, unload_image, 
    load_texture_from_image, 
    draw_texture, Vector2,
    WHITE , BLACK, draw_rectangle,
    )

class State:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y

        img = load_image(img)

        self.tx = load_texture_from_image(img)

        unload_image(img)

    def draw(self):
        draw_texture(self.tx, self.x, self.y, WHITE)

class Button:
    def __init__(self , pos : Vector2 , width : int , height : int, color = BLACK):

        self.pos = pos
        self.width = width
        self.height = height
        self.color = color

        draw_rectangle(int(self.pos.x), int(self.pos.y), width, height, color)
    
    def exit(self):
        pass
    
    def next(self):
        pass
