import pyray as pr 
from Transform import *

pr.init_window(1080, 720, "Iran Map")


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
Sistan_Baluchestan = State(444, 451, "assets/Sistan_Baluchestan.png")
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

    pr.end_drawing()
