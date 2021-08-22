import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def pil2cv(imgPIL):
    imgCV_RGB = np.array(imgPIL, dtype = np.uint8)
    imgCV_BGR = np.array(imgPIL)[:, :, ::-1]
    return imgCV_BGR

def cv2pil(imgCV):
    imgCV_RGB = imgCV[:, :, ::-1]
    imgPIL = Image.fromarray(imgCV_RGB)
    return imgPIL

def cv2_putText(img, text, org, fontFace, fontScale, color):
    x, y = org
    b, g, r = color
    colorRGB = (r, g, b)
    imgPIL = cv2pil(img)
    draw = ImageDraw.Draw(imgPIL)
    fontPIL = ImageFont.truetype(font = fontFace, size = fontScale)
    w, h = draw.textsize(text, font = fontPIL)
    draw.text(xy = (x-(w/2),y-h), text = text, fill = colorRGB, font = fontPIL)
    imgCV = pil2cv(imgPIL)
    return imgCV

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
        self.rcharacters = [
            "jet",
            "reyna",
            "astra",
            "killjoy",
            "sova"
        ]
        self.bcharacters = [
            "jet",
            "phoenix",
            "astra",
            "killjoy",
            "sova"
        ]
        self.margin_rlay = 250
        self.margin_blay = 780
        self.rnames = [
            "moca",
            "MkxlElf",
            "Mashiro",
            "AxiA",
            "sRqzx"
        ]
        self.bnames = [
            "SnowYukiWhite",
            "tapazo",
            "NJack",
            "Orca",
            "zonge"
        ]
        self.rteam_name = "LN"
        self.bteam_name = "AG"
        self.rscore = 13
        self.bscore = 7

    def gen_base(self):
        blank = cv2.imread("assets/blank.png")

        for i in range(5):
            blank = self.paste_red(blank, i*(self.card_width+20))
            blank = self.paste_red_character(blank, self.rcharacters[i], i*(self.card_width+20)+60)
            blank = self.paste_dark_overlay(blank, i*(self.card_width+20), self.margin_rlay)
            blank = self.paste_name(blank, self.rnames[i], i*(self.card_width+20), self.margin_rlay)

        for i in range(5):
            blank = self.paste_blue(blank, i*(self.card_width+20))
            blank = self.paste_blue_character(blank, self.bcharacters[i], i*(self.card_width+20)+60)
            blank = self.paste_dark_overlay(blank, i*(self.card_width+20), self.margin_blay)
            blank = self.paste_name(blank, self.bnames[i], i*(self.card_width+20), self.margin_blay)
        
        blank = self.paste_rscore(blank, self.rscore, 700, 485)
        blank = self.paste_bscore(blank, self.bscore, 930, 485)

        blank = self.paste_rteam_name(blank, self.rteam_name, 320, 470)
        blank = self.paste_bteam_name(blank, self.bteam_name, 1320, 470)
        
        cv2.imwrite("blank.png", blank)

    def paste_red(self, base, x):
        red = cv2.imread("assets/redCard.png", -1)

        h, w = red.shape[:2]
        self.card_width = w
        self.card_height = h

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

        base[y:h+y, x+self.margin:x+w+self.margin] = \
            base[y:h+y, x+self.margin:x+w+self.margin] * (1 - overlay[:, :, 3:] / 255) + \
            overlay[:, :, :3] * (overlay[:, :, 3:] / 255)

        return base

    def paste_name(self, base, text, x, y):
        fontPIL = "Noto_Sans_JP/NotoSansJP-Bold.otf"

        base = cv2_putText(
            img = base,
            text=text,
            org=(x+170, y+45),
            fontFace=fontPIL,
            fontScale=36,
            color=(255,255,255)
        )

        return base

    def paste_rscore(self, base, score, x, y):
        fontPIL = "Noto_Sans_JP/NotoSansJP-Black.otf"

        base = cv2_putText(
            img = base,
            text=str(score),
            org=(x, y),
            fontFace=fontPIL,
            fontScale=112,
            color=(99,99,255)
        )

        return base

    def paste_bscore(self, base, score, x, y):
        fontPIL = "Noto_Sans_JP/NotoSansJP-Black.otf"

        base = cv2_putText(
            img = base,
            text=str(score),
            org=(x, y),
            fontFace=fontPIL,
            fontScale=112,
            color=(251,153,26)
        )

        return base

    def paste_rteam_name(self, base, name, x, y):
        fontPIL = "Noto_Sans_JP/NotoSansJP-Bold.otf"

        base = cv2_putText(
            img = base,
            text=name,
            org=(x, y),
            fontFace=fontPIL,
            fontScale=64,
            color=(99,99,255)
        )

        return base

    def paste_bteam_name(self, base, name, x, y):
        fontPIL = "Noto_Sans_JP/NotoSansJP-Bold.otf"

        base = cv2_putText(
            img = base,
            text=name,
            org=(x, y),
            fontFace=fontPIL,
            fontScale=64,
            color=(251,153,26)
        )

        return base

if __name__ == "__main__":
    valo_generator = ValoGenerator()
    valo_generator.gen_base()