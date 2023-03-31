from pyray import (
    load_image, unload_image, 
    load_texture_from_image, 
    draw_texture,
    WHITE , BLACK, GREEN, RED, ORANGE, YELLOW, PINK,
    draw_rectangle,
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
