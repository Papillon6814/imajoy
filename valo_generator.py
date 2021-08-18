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

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")
        # blank = np.zeros((self.base_height, self.base_width, 4))
        # blank += [236, 240, 243, 255][::-1]
        print(blank.shape)

        for i in range(5):
            blank = self.paste_red(blank, i*(self.card_width+20))

        for i in range(5):
            blank = self.paste_blue(blank, i*(self.card_width+20))
        
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

        print(self.card_height)

        base[self.margin_by:self.card_height+self.margin_by, x+self.margin:x+self.card_width+self.margin] = \
            base[self.margin_by:self.card_height+self.margin_by, x+self.margin:x+self.card_width+self.margin] * \
            (1 - blue[:, :, 3:] / 255) + \
            blue[:, :, :3] * (blue[:, :, 3:] / 255)

        return base

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()