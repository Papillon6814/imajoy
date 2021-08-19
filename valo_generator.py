import cv2
import numpy as np

class ValoGenerator:
    def __init__(self):
        self.base_height = 900
        self.base_width = 1650
        self.card_height = 0
        self.card_width = 0
        self.margin = 20
        self.margin_ry = 20
        self.margin_by = 550
        self.margin_rcy = 50
        self.margin_bcy = 580
        self.characters = [
            "jet",
            "sage",
            "sova",
            "brim",
            "cypher",
            "omen",
            "yoru",
            "viper",
            "skye",
            "reyna"
        ]
        self.margin_rlay = 250
        self.margin_blay = 780
        self.rnames = [
            "Tarou",
            "Jirou",
            "Saburou",
            "Shirou",
            "Gorou"
        ]
        self.bnames = [
            "ASDF",
            "ASDFG",
            "ASDFGH",
            "ASDFGHJ",
            "ASDFGHJK"
        ]

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")
        # blank = np.zeros((self.base_height, self.base_width, 4))
        # blank += [236, 240, 243, 255][::-1]

        for i in range(5):
            blank = self.paste_red(blank, i*(self.card_width+20))
            blank = self.paste_red_character(blank, self.characters[i], i*(self.card_width+20)+60)
            blank = self.paste_dark_overlay(blank, i*(self.card_width+20), self.margin_rlay)
            self.paste_name(blank, self.rnames[i], i*(self.card_width+20), self.margin_rlay)

        for i in range(5):
            blank = self.paste_blue(blank, i*(self.card_width+20))
            blank = self.paste_blue_character(blank, self.characters[i+5], i*(self.card_width+20)+60)
            blank = self.paste_dark_overlay(blank, i*(self.card_width+20), self.margin_blay)
            self.paste_name(blank, self.bnames[i], i*(self.card_width+20), self.margin_blay)
        
        cv2.imwrite("blank.png", blank)

    def paste_red(self, base, x):
        red = cv2.imread("assets/redCard.png", -1)

        h, w = red.shape[:2]
        self.card_width = w
        self.card_height = h
        print("x: {}".format(x))

        base[self.margin_ry:h+self.margin_ry, x+self.margin:x+w+self.margin] = base[self.margin_ry:h+self.margin_ry, x+self.margin:x+w+self.margin] * (1 - red[:, :, 3:] / 255) + \
            red[:, :, :3] * (red[:, :, 3:] / 255)

        return base

    def paste_blue(self, base, x):
        blue = cv2.imread("assets/blueCard.png", -1)

        base[self.margin_by:self.card_height+self.margin_by, x+self.margin:x+self.card_width+self.margin] = \
            base[self.margin_by:self.card_height+self.margin_by, x+self.margin:x+self.card_width+self.margin] * \
            (1 - blue[:, :, 3:] / 255) + \
            blue[:, :, :3] * (blue[:, :, 3:] / 255)

        return base

    def paste_red_character(self, base, name, x):
        character = cv2.imread("assets/valo/{}.png".format(name), -1)
        h, w = character.shape[:2]

        base[self.margin_rcy:h+self.margin_rcy, x+self.margin:x+w+self.margin] = base[self.margin_rcy:h+self.margin_rcy, x+self.margin:x+w+self.margin] * (1 - character[:, :, 3:] / 255) + \
            character[:, :, :3] * (character[:, :, 3:] / 255)

        return base

    def paste_blue_character(self, base, name, x):
        character = cv2.imread("assets/valo/{}.png".format(name), -1)
        h, w = character.shape[:2]

        base[self.margin_bcy:h+self.margin_bcy, x+self.margin:x+w+self.margin] = base[self.margin_bcy:h+self.margin_bcy, x+self.margin:x+w+self.margin] * (1 - character[:, :, 3:] / 255) + \
            character[:, :, :3] * (character[:, :, 3:] / 255)

        return base

    def paste_dark_overlay(self, base, x, y):
        overlay = cv2.imread("assets/darkOverlay.png", -1)
        h, w = overlay.shape[:2]
        print(overlay.shape)
        print("{} {}".format(x, base.shape))

        base[y:h+y, x+self.margin:x+w+self.margin] = \
            base[y:h+y, x+self.margin:x+w+self.margin] * (1 - overlay[:, :, 3:] / 255) + \
            overlay[:, :, :3] * (overlay[:, :, 3:] / 255)

        return base

    def paste_name(self, base, text, x, y):
        cv2.putText(
            base, 
            text=text, 
            org=(x+120, y+40), 
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1.0,
            color=(255, 255, 255),
            thickness=3,
            lineType=16
        )

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()