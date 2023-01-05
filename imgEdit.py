import numpy as np

import cv2

# 入力画像のパス
input_img = './images/img_edit_input.png'

# カットする位置を計算
img_org = cv2.imread(input_img)
height, width, channels = img_org.shape
cut_y = height // 3

# 入力画像を読み込み
img_src = cv2.imread(input_img)

# 1/3の部分を切り取る
h = img_src.shape[0]
img_dst = img_src[0:h-cut_y, :]

# 結果を出力
cv2.imwrite('./images/img_edit_output.png', img_dst)