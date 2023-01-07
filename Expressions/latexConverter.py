import io
import cv2
import cv2u
import numpy as np

def latex2png(latexURL):
    print("OK1", latexURL)
    inputImg = cv2u.urlread(latexURL)
    height, width = inputImg.shape[:2]
    inputImg = inputImg[:, :, 3]
    inputImg = cv2.copyMakeBorder(inputImg, 10, 10, 10, 10, cv2.BORDER_CONSTANT, (0,0,0))
    inputImg = cv2.resize(inputImg, dsize = (width, height))

    blurred = cv2.GaussianBlur(inputImg, (7, 7), 0)
    _, threshed = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)

    inner = cv2.cvtColor(inputImg, cv2.COLOR_BGR2BGRA)
    inner[:, :, 3] = np.where(inner[:, :, 1] == 0, 0, 255)

    outer = cv2.cvtColor(threshed, cv2.COLOR_BGR2BGRA)
    outer[:, :, 0] = 63
    outer[:, :, 1] = 57
    outer[:, :, 2] = 54
    outer[:, :, 3] = np.where(outer[:, :, 1] == 0, 0, 255)

    result = cv2.add(inner, outer)
    print("OK2")
    cv2.imwrite("/home/pi/Saves/bot/Expressions/images/formula.png", result)

if __name__ == "__main__":
    text = r"y = \sin t"
    URL = "https://latex.codecogs.com/png.image?\dpi{1250}" + text.replace(" ", "{}").replace("=", "{=}")
    latex2png(URL)
    # latex2png("https://latex.codecogs.com/png.image?\dpi{1250}y=\sin{}x")