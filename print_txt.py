import cv2
import os
from glob import glob

file_path = 'input_file_path'
file_names = os.listdir(file_path)
char = ' .,-◂~:;=!*ᧉө#$@░▒▓█' #20
nw = 100

for img_path in glob('img/*.jpg'):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = img.shape
    nh = int(h / w * nw)

    img = cv2.resize(img, (nw * 3, nh))

    for row in img:
        for pixel in row:
            index = int(pixel / 256 * len(char))
            print(char[index])

        print()
os.system('pause')