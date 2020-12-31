import cv2
import os
char = ' .,-~:;=!*#$@░▒▓█' #20
nw = 100

cap = cv2.VideoCapture('video/video.mp4')

os.system("cls")

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape
    nh = int(h / w * nw)

    img = cv2.resize(img, (nw * 3, nh))

    for row in img:
        for pixel in row:
            index = int(pixel / 256 * len(char))
            print(char[index], end='')
        print()

    print('\x1b[H', end='')