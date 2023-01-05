# import cv2
# import cv2u

# def URLSave(URL):
#     img = cv2u.urlread(URL)
#     cv2.imwrite("./images/img_edit_input.png", img)

import requests

def URLSave(URL, filename):
    r = requests.get(URL, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)

if __name__ == "__main__":
    URLSave("https://cdn.discordapp.com/attachments/1047422842276425789/1057312092513910915/nelnel.jpg", "./images/img_edit_input.png")