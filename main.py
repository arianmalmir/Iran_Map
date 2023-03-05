import pyray as pr 
from Transform import *

pr.init_window(1080, 720, "Ali")


Alborz = State(-59, 251, "assets/Alborz.png")
Ardebil = State(-119, 104, "assets/Ardebil.png")
Azebayjan_sharghi = State(106, 126, "assets/Azerbayjan_sharghi.png")
Azerbayjan_gharbi = State(70, 101, "assets/Azerbayjan_gharbi.png")
Bushehr = State(96, 500, "assets/Bushehr.png")
Chahar_mahal_bakhtiari = State(52, 406, "assets/Chahar_mahal_bakhtiari.png")
Elam = State(-81, 348, "assets/Elam.png")
Esfehan = State(90, 327, "assets/Esfehan.png")
Fars = State(161, 443, "assets/Fars.png")
Ghazvin = State(-3, 231, "assets/Ghazvin.png")
Ghom = State(171, 299, "assets/Ghom.png")
Gilan = State(-24, 162, "assets/Gilan.png")
Golestan = State(41, 174, "assets/Golestan.png")
Hamedan = State(-68, 275, "assets/Hamedan.png")
Hormozgan = State(245, 553, "assets/Hormozgan.png")
Kerman = State(330, 430, "assets/Kerman.png")
Kermanshah = State(-12, 296, "assets/Kermanshah.png")
Khorasan_junubi = State(415, 339, "assets/Khorasan_junubi.png")
Khorasan_razavi = State(388, 184, "assets/Khorasan_razavi.png")
Khorasan_shomali = State(294, 167, "assets/Khorasan_shomali.png")
Khuzestan = State(-8, 390, "assets/Khuzestan.png")
KohGiloye_Boyer_ahmad = State(61, 453, "assets/KohGiloye_Boyer_ahmad.png")
Kordestan = State(22, 244, "assets/Kordestan.png")
Lorestan = State(-28, 335, "assets/Lorestan.png")
Markazi = State(-126, 279, "assets/Markazi.png")
Mazandaran = State(11, 225, "assets/Mazandaran.png")
Semnan = State(174, 207, "assets/Semnan.png")
Sistan_Baluchestan = State(394, 461, "assets/Sistan_Baluchestan.png")
Tehran = State(-69, 261, "assets/Tehran.png")
Yazd = State(201, 300, "assets/Yazd.png")
Zanjan = State(-12, 214, "assets/Zanjan.png")

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

    hormoz = pr.Rectangle(413, 554, 20, 17)
    Button(pr.Vector2(413, 554), 20, 17, pr.RED)

    kerman = pr.Rectangle(397, 481, 80, 42) 
    Button(pr.Vector2(397, 481),80, 42,pr.RED )

    kermanshah = pr.Rectangle(186, 369, 10, 10)
    Button(pr.Vector2(186, 369), 23, 13, pr.RED)

    khorasan_junubi = pr.Rectangle(474, 421, 54, 42)
    Button(pr.Vector2(474, 421), 54, 42, pr.RED)

    khorasan_razavi = pr.Rectangle( 460, 323, 57,50)
    Button(pr.Vector2(460, 323), 57, 50, pr.RED)

    khorasan_shomali = pr.Rectangle(430, 281, 20, 20)
    Button(pr.Vector2(430, 281), 20, 20, pr.RED)

    khuzestan = pr.Rectangle(237,437,42,40)
    Button(pr.Vector2(237,437),42,40,pr.RED)


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

    elif (pr.check_collision_point_rec(mousePoint , hormoz)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , kerman)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , kermanshah)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , khorasan_junubi)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , khorasan_razavi)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")
    
    elif (pr.check_collision_point_rec(mousePoint , khorasan_shomali)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")

    elif (pr.check_collision_point_rec(mousePoint , khuzestan)):

        if ( pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT) and press == False):
            press = True
            print("Pressed")
            
    else:
        press = False   

    
    # print(mousePoint.x,mousePoint.y)


    pr.end_drawing()
