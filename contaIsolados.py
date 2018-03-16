import cv2
import numpy as np
import argparse
#cv2.imshow('ruido', img)
#cv2.waitKey(0)

def _neighbors(arr,x,y,n):
    arr=np.roll(np.roll(arr,shift=-x+1,axis=0),shift=-y+1,axis=1)
    return arr[:n,:n]

def contaIsolados(img, nivelCinza, viz=False):
    brancos = 0
    pretos  = 0

    if not viz: # vizinhanca-4
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if (i == 0 or i == img.shape[0]-1 or j == 0 or j == img.shape[1]-1):
                    neighbors = _neighbors(img, i, j, 3)
                else:
                    neighbors = img[i-1:i+2,j-1:j+2]

                if img[i, j] == 0:
                    if (neighbors[0, 1] == 255 and neighbors[2, 1] == 255 and
                        neighbors[1, 0] == 255 and neighbors[1, 2] == 255):
                        pretos += 1
                elif img[i, j] == 255:
                    if (neighbors[0, 1] == 0 and neighbors[2, 1] == 0 and
                        neighbors[1, 0] == 0 and neighbors[1, 2] == 0):
                        brancos += 1
    if viz: # vizinhanca-8
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if (i == 0 or i == img.shape[0]-1 or j == 0 or j == img.shape[1]-1):
                    neighbors = _neighbors(img, i, j, 3)
                else:
                    neighbors = img[i-1:i+2,j-1:j+2]
                if img[i, j] == 0:
                    if len(neighbors[neighbors == 255]) == 8:
                        pretos += 1
                if img[i, j] == 255:
                    if len(neighbors[neighbors == 0]) == 8:
                        brancos +=1
            #print("B: " + str(pretos) + "\tW: " + str(brancos))
    return pretos, brancos

def main():
    parser = argparse.ArgumentParser(prog="contaIsolados.py")
    parser.add_argument('file', nargs='+', help="File(s) path(s)")
    parser.add_argument("-n", "--neighborhood", type=int, default=4, help="Neighborhood 4 or 8.")

    args = parser.parse_args()

    if args.neighborhood != 4 and args.neighborhood != 8:
        raise Exception("Invalid neighborhood size.")
    flag = (args.neighborhood == 8)
    for f in args.file:
        print(f)
        img = cv2.imread(f, 0)
        print(contaIsolados(img, 0, viz=flag))


if __name__ == '__main__':
    main()
