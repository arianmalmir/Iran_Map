from Transform import State

class Map:
    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y

        self.States = []

    def create_states(self):
        self.Alborz = State(-59 + self.offset_x, 251 + self.offset_y, "assets/Alborz.png")
        self.Ardebil = State(-119 + self.offset_x, 104 + self.offset_y, "assets/Ardebil.png")
        self.Azebayjan_sharghi = State(106 + self.offset_x, 126 + self.offset_y, "assets/Azerbayjan_sharghi.png")
        self.Azerbayjan_gharbi = State(70 + self.offset_x, 101 + self.offset_y, "assets/Azerbayjan_gharbi.png")
        self.Bushehr = State(96 + self.offset_x, 500 + self.offset_y, "assets/Bushehr.png")
        self.Chahar_mahal_bakhtiari = State(52 + self.offset_x, 406 + self.offset_y, "assets/Chahar_mahal_bakhtiari.png")
        self.Elam = State(-81 + self.offset_x, 348 + self.offset_y, "assets/Elam.png")
        self.Esfehan = State(90 + self.offset_x, 327 + self.offset_y, "assets/Esfehan.png")
        self.Fars = State(161 + self.offset_x, 443 + self.offset_y, "assets/Fars.png")
        self.Ghazvin = State(-3 + self.offset_x, 231 + self.offset_y, "assets/Ghazvin.png")
        self.Ghom = State(171 + self.offset_x, 299 + self.offset_y, "assets/Ghom.png")
        self.Gilan = State(-24 + self.offset_x, 162 + self.offset_y, "assets/Gilan.png")
        self.Golestan = State(41 + self.offset_x, 174 + self.offset_y, "assets/Golestan.png")
        self.Hamedan = State(-68 + self.offset_x, 275 + self.offset_y, "assets/Hamedan.png")
        self.Hormozgan = State(245 + self.offset_x, 553 + self.offset_y, "assets/Hormozgan.png")
        self.Kerman = State(330 + self.offset_x, 430 + self.offset_y, "assets/Kerman.png")
        self.Kermanshah = State(-12 + self.offset_x, 296 + self.offset_y, "assets/Kermanshah.png")
        self.Khorasan_junubi = State(415 + self.offset_x, 339 + self.offset_y, "assets/Khorasan_junubi.png")
        self.Khorasan_razavi = State(388 + self.offset_x, 184 + self.offset_y, "assets/Khorasan_razavi.png")
        self.Khorasan_shomali = State(294 + self.offset_x, 167 + self.offset_y, "assets/Khorasan_shomali.png")
        self.Khuzestan = State(-8 + self.offset_x, 390 + self.offset_y, "assets/Khuzestan.png")
        self.KohGiloye_Boyer_ahmad = State(61 + self.offset_x, 453 + self.offset_y, "assets/KohGiloye_Boyer_ahmad.png")
        self.Kordestan = State(22 + self.offset_x, 244 + self.offset_y, "assets/Kordestan.png")
        self.Lorestan = State(-28 + self.offset_x, 335 + self.offset_y, "assets/Lorestan.png")
        self.Markazi = State(-126 + self.offset_x, 279 + self.offset_y, "assets/Markazi.png")
        self.Mazandaran = State(11 + self.offset_x, 225 + self.offset_y, "assets/Mazandaran.png")
        self.Semnan = State(174 + self.offset_x, 207 + self.offset_y, "assets/Semnan.png")
        self.Sistan_Baluchestan = State(444 + self.offset_x, 451 + self.offset_y, "assets/Sistan_Baluchestan.png")
        self.Tehran = State(-69 + self.offset_x, 261 + self.offset_y, "assets/Tehran.png")
        self.Yazd = State(201 + self.offset_x, 300 + self.offset_y, "assets/Yazd.png")
        self.Zanjan = State(-12 + self.offset_x, 214 + self.offset_y, "assets/Zanjan.png")

        self.States = [self.Alborz, self.Ardebil, self.Azebayjan_sharghi, self.Azerbayjan_gharbi, self.Bushehr, self.Chahar_mahal_bakhtiari, self.Elam, self.Esfehan, self.Fars, self.Ghazvin, self.Ghom, self.Gilan, self.Golestan, self.Hamedan, self.Hormozgan, self.Kerman, self.Kermanshah, self.Khorasan_junubi, self.Khorasan_razavi, self.Khorasan_shomali, self.Khuzestan, self.KohGiloye_Boyer_ahmad, self.Kordestan, self.Lorestan, self.Markazi, self.Mazandaran, self.Semnan, self.Sistan_Baluchestan, self.Tehran, self.Yazd, self.Zanjan]
