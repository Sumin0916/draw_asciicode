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

    f = open("input_file_path\\temp.txt", 'w', -1, "utf-8")
    for row in img:
        for pixel in row:
            index = int(pixel / 256 * len(char))
            index = -(index + 1) #(흑백 반전)
            data = char[index]
            f.write(data)
        f.write('\n')
    f.close()
    src = os.path.join(file_path, 'temp.txt')
    dst = img_path + '.txt'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)