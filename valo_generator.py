import cv2
import numpy as np

class ValoGenerator:
    def __init__(self):
        self.base_height = 900
        self.base_width = 1650

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")
        # blank = np.zeros((self.base_height, self.base_width, 4))
        # blank += [236, 240, 243, 255][::-1]
        print(blank.shape)
        blank = self.paste_red(blank)

        cv2.imwrite("blank.png", blank)

    def paste_red(self, base):
        red = cv2.imread("assets/redCard.png", -1)

        h, w = red.shape[:2]

        # mask = red[:, :, 3]
        # mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        # mask = mask / 255

        #red = red[:, :, 3]
        #base[0:w, 0:h, :] = red

        base[0:h, 0:w] = base[0:h, 0:w] * (1 - red[:, :, 3:] / 255) + \
            red[:, :, :3] * (red[:, :, 3:] / 255)

        return base

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()