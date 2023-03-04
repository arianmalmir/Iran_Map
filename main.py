import pyray as pr 
from Transform import *

pr.init_window(1080, 720, "Ali")


Alborz = State(58, 324, "assets/Alborz.png")
Ardebil = State(18, 224, "assets/Ardebil.png")
Azebayjan_sharghi = State(167, 239, "assets/Azebayjan_sharghi.png")
Azerbayjan_gharbi = State(143, 222, "assets/Azerbayjan_gharbi.png")
Bushehr = State(163, 492, "assets/Bushehr.png")
Chahar_mahal_bakhtiari = State(133, 427, "assets/Chahar_mahal_bakhtiari.png")
Elam = State(44, 388, "assets/Elam.png")
Esfehan = State(158, 375, "assets/Esfehan.png")
Fars = State(205, 453, "assets/Fars.png")
Ghazvin = State(95, 310, "assets/Ghazvin.png")
Ghom = State(211, 355, "assets/Ghom.png")
Gilan = State(82, 263, "assets/Gilan.png")
Golestan = State(125, 273, "assets/Golestan.png")
Hamedan = State(52, 339, "assets/Hamedan.png")
Hormozgan = State(261, 527, "assets/Hormozgan.png")
Kerman = State(318, 445, "assets/Kerman.png")
Kermanshah = State(89, 353, "assets/Kermanshah.png")
Khorasan_junubi = State(374, 383, "assets/Khorasan_junubi.png")
Khorasan_razavi = State(355, 279, "assets/Khorasan_razavi.png")
Khorasan_shomali = State(293, 268, "assets/Khorasan_shomali.png")
Khuzestan = State(92, 416, "assets/Khuzestan.png")
KohGiloye_Boyer_ahmad = State(139, 459, "assets/KohGiloye_Boyer_ahmad.png")
Kordestan = State(111, 318, "assets/Kordestan.png")
Lorestan = State(80, 380, "assets/Lorestan.png")
Markazi = State(13, 342, "assets/Markazi.png")
Mazandaran = State(105, 306, "assets/Mazandaran.png")
Semnan = State(213, 295, "assets/Semnan.png")
Sistan_Baluchestan = State(394, 461, "assets/Sistan_Baluchestan.png")
Tehran = State(50, 331, "assets/Tehran.png")
Yazd = State(231, 357, "assets/Yazd.png")
Zanjan = State(89, 297, "assets/Zanjan.png")

States = [Alborz, Ardebil, Azebayjan_sharghi, Azerbayjan_gharbi, Bushehr, Chahar_mahal_bakhtiari, Elam, Esfehan, Fars, Ghazvin, Ghom, Gilan, Golestan, Hamedan, Hormozgan, Kerman, Kermanshah, Khorasan_junubi, Khorasan_razavi, Khorasan_shomali, Khuzestan, KohGiloye_Boyer_ahmad, Kordestan, Lorestan, Markazi, Mazandaran, Semnan, Sistan_Baluchestan, Tehran, Yazd, Zanjan]

press = False
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.WHITE)
 
    mousePoint = pr.get_mouse_position()

    for s in States:
        s.draw()

    exit = pr.Rectangle(15,21,35,35)
    Button(pr.Vector2(15,21),35,35,pr.RED) # Exit button

    alborz = pr.Rectangle(295,334,7,7)
    Button(pr.Vector2(295,334),7,7,pr.RED)

    ardebil = pr.Rectangle(236,262,10,10)
    Button(pr.Vector2(236,262),10,10,pr.RED) 
    
    azarbayjan_sharghi = pr.Rectangle(198,277,15,15)
    Button(pr.Vector2(198,277),15,15,pr.RED)

    azerbayjan_gharbi = pr.Rectangle(177,310,15,15)
    Button(pr.Vector2(172,304),15,15,pr.RED)

    boshehr = pr.Rectangle(307, 522, 10, 10)
    Button(pr.Vector2(307,522),10,10,pr.RED)

    chahar_mahal = pr.Rectangle(289, 439, 10, 10)
    Button(pr.Vector2(289, 439), 10, 10, pr.RED)

    elam = pr.Rectangle(196, 405, 10, 10)
    Button(pr.Vector2(196, 405), 10, 10, pr.RED)

    esfehan = pr.Rectangle(303, 398, 80, 25)
    Button(pr.Vector2(303, 398),80, 25, pr.RED)

    fars = pr.Rectangle(329, 463, 25, 80)
    Button(pr.Vector2(329, 463),25, 80, pr.RED)

    ghasvin = pr.Rectangle(271, 323, 15, 15)
    Button(pr.Vector2(271, 323),15, 15, pr.RED)

    ghom = pr.Rectangle(295, 369, 10, 10)
    Button(pr.Vector2(295, 369),10, 10, pr.RED)

    gilan = pr.Rectangle(262, 292, 10, 10)
    Button(pr.Vector2(262, 292),10, 10, pr.RED)

    golestan = pr.Rectangle(386, 297, 18, 10)
    Button(pr.Vector2(386, 297),18, 10, pr.RED)

    hamedan = pr.Rectangle(239, 352, 12, 15)
    Button(pr.Vector2(239, 352), 12, 15, pr.RED)

    if (pr.check_collision_point_rec(mousePoint , exit)):
        
        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , alborz)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , ardebil)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")
    elif(pr.check_collision_point_rec(mousePoint , azarbayjan_sharghi)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , azerbayjan_gharbi)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , boshehr)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , chahar_mahal)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , elam)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , esfehan)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , fars)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , ghasvin)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , ghom)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , gilan)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , golestan)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , hamedan)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")


    else:
        press = False   

    
    # print(mousePoint.x,mousePoint.y)


    pr.end_drawing()
