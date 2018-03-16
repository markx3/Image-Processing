import cv2
import numpy as np
import argparse

img = cv2.imread('imagens/lena.jpg', 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)

def entropy(img):
    ni = np.zeros(2 ** 10)
    x = img.shape[0]
    y = img.shape[1]
    for i in range(x):
        for j in range(y):
            ni[img[i,j]] += 1
    pi = ni / (x * y)

    res = 0
    for n in pi:
        if n > 0:
            res += n * np.log2(n)
    res = -res
    return res

def main(args):

    entropies = []
    for f in args.file:
        en = entropy(cv2.imread(f, 0))
        entropies.append((en, f))
    max_entropy, f = max(entropies)
    entropies = sorted(entropies, reverse=True)

    print("Entropy\t\tPercentage\t\tFile")
    for en, f in entropies:
        perc = (en/max_entropy)*100
        print("%.5f" % en + "\t\t" + "%.2f" % perc + "%\t\t" + str(f) + " " )

def parse_args():
    parser = argparse.ArgumentParser(prog="entropia.py")
    parser.add_argument('file', nargs='+', help="File(s) path(s)")

    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args())
