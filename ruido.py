import cv2
import numpy as np
import argparse

def noise(img, gray_lvl=0, pixels=100):
    p = 0
    while p != pixels // 2:
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        if img[x, y] != 0:
            img[x, y] = 0
            p += 1

    p = 0
    while p != pixels // 2:
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        if img[x, y] != 255:
            img[x, y] = 255
            p += 1

    return img



def main():
    parser = argparse.ArgumentParser(prog="ruido.py")
    parser.add_argument('file', nargs='+', help="File(s) path(s)")
    parser.add_argument("-n", "--num-pixels", type=int, default=4, help="Number of pixels to be altered.")

    args = parser.parse_args()

    for f in args.file:
        img = cv2.imread(f, 0)
        img_noise = noise(img, pixels=args.num_pixels)
        cv2.imshow(f, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

main()
