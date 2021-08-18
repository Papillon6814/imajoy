import cv2
import numpy as np

class ValoGenerator:
    def __init__(self):
        self.base_height = 900
        self.base_width = 1650

    def gen_base(self):
        blank = np.zeros((self.base_height, self.base_width, 3))
        blank += [236, 240, 243][::-1]

        cv2.imwrite("blank.png", blank)


if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()