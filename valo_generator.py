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
        self.margin_bcy = 600

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")
        # blank = np.zeros((self.base_height, self.base_width, 4))
        # blank += [236, 240, 243, 255][::-1]
        print(blank.shape)

        for i in range(5):
            blank = self.paste_red(blank, i*(self.card_width+20))
            blank = self.paste_red_character(blank, "jet", i*(self.card_width+20)+60)

        for i in range(5):
            blank = self.paste_blue(blank, i*(self.card_width+20))
            blank = self.paste_blue_character(blank, "omen", i*(self.card_width+20)+60)
        
        cv2.imwrite("blank.png", blank)

    def paste_red(self, base, x):
        red = cv2.imread("assets/redCard.png", -1)

        h, w = red.shape[:2]
        self.card_height = h
        self.card_width = w

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

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()