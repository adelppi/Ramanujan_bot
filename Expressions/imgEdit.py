import numpy as np

import cv2
import numpy as np

# input image file path
in_img_path = './Expressions/images/img_edit_input.png'
# output image file path
out_img_path = './Expressions/images/img_edit_output.png'

# load image
img = cv2.imread(in_img_path)

# Load the cascade
cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')

# Detect faces
faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)

# Draw edges around the face
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display
cv2.imshow('img', img)

# Save output image
cv2.imwrite(out_img_path, img)

cv2.waitKey(0)
cv2.destroyAllWindows()