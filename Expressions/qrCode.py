import pyqrcode
from pyqrcode import QRCode
import cv2
import numpy as np

def qrGen(cmdInput, emoji):

    if emoji:
        qr = pyqrcode.create(cmdInput)
        qr.png("./images/qr.png", scale = 1, quiet_zone = 0)
        img = cv2.imread("./images/qr.png")
        emoji1 = cv2.imread("./images/1.png", -1)
        emoji2 = cv2.imread("./images/2.png", -1)
        blank = emoji1 - 255
        blank[:, :, 0] = 0
        blank[:, :, 1] = 0
        blank[:, :, 2] = 0
        blank[:, :, 3] = 255
        size = img.shape[0]
        pattern = [[0] * size for i in range(size)]
        row = []
        rows = []
        for i in range(size):
            for j in range(size):
                pattern[i][j] = img[i][j][0]
                if (i < 7 and j < 7 and img[i][j][0] == 0) or (i < 7 and j > size - 8 and img[i][j][0] == 0) or (i > size - 8 and j < 7 and img[i][j][0] == 0):
                    row.append(blank)
                else:
                    if img[i][j][0] == 0:
                        row.append(emoji1)
                    elif img[i][j][0] == 255:
                        row.append(emoji2)

            rows.append(cv2.hconcat(row))
            row.clear()

        result = cv2.vconcat(rows)
        cv2.imwrite("./images/qr.png", result)
    else:
        qr = pyqrcode.create(cmdInput)
        qr.png("./images/qr.png", scale = 10, quiet_zone = 1)
        img = cv2.bitwise_not(cv2.imread("./images/qr.png"))
        img = np.where(img == (0, 0, 0), (63, 57, 54), (255, 255, 255))
        cv2.imwrite("./images/qr.png", img)

if __name__ == "__main__":
    qrGen("https://youtube.com", emoji = True)