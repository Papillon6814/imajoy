import cv2
import numpy as np

class ValoGenerator:
    def __init__(self):
        self.base_height = 900
        self.base_width = 1650
        self.card_height = 0
        self.card_width = 0

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")
        # blank = np.zeros((self.base_height, self.base_width, 4))
        # blank += [236, 240, 243, 255][::-1]
        print(blank.shape)

        for i in range(5):
            blank = self.paste_red(blank, i*(self.card_width+20))
        
        cv2.imwrite("blank.png", blank)

    def paste_red(self, base, x):
        red = cv2.imread("assets/redCard.png", -1)

        h, w = red.shape[:2]
        self.card_height = h
        self.card_width = w

        print(h, w)

        base[20:h+20, x+20:x+w+20] = base[20:h+20, x+20:x+w+20] * (1 - red[:, :, 3:] / 255) + \
            red[:, :, :3] * (red[:, :, 3:] / 255)

        return base

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()