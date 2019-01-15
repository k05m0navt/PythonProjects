import numpy as np
from PIL import Image, ImageDraw
import math
import sys

def hexToFloat(bits):
    numb = float(0)
    alf = {'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}
    if bits[0] in alf:
        numb += alf[bits[0]]
    else:
        numb += float(bits[0])
    numb *= 16
    if bits[1] in alf:
        numb += alf[bits[1]]
    else:
        numb += float(bits[1])
    return numb

def sort(listo):
    n = len(listo)
    bridge = 0
    while(bridge < n - 1):
        minI = bridge
        for i in range(bridge, n):
            if(listo[i] < listo[minI]):
                minI = i
        holder = listo[bridge]
        listo[bridge] = listo[minI]
        listo[minI] = holder
        bridge += 1
    return listo

def IngvarrsInput():
    g = input().split(' ')
    H, W = g[:2]
    W = int(W)
    H = int(H)
    OriginalImage = np.zeros((H, W, 3))

    for i in range(H):
        pixels = sys.stdin.readline().split(' ')
        for j in range(W):
            for k in range(3):
                OriginalImage[i][j][k] = int(pixels[j][k * 2: k * 2 + 2], 16)
    return W, H, OriginalImage

def InputFromConsole():
    W, H = input().split(' ')

    W = int(W)
    H = int(H)

    OriginalImage = np.zeros((H, W, 3))

    pixels = sys.stdin.readline().split(' ')
    for i in range(H):
        for j in range(W):
            for k in range(3):
                OriginalImage[i][j][k] = int(pixels[i*W + j][k * 2: k * 2 + 2], 16)
    return W, H, OriginalImage


def InputFromFile(fileName):
    file = open(fileName)
    W, H = file.readline().split(' ')
    W = int(W)
    H = int(H[:-1])
    data = file.read().split(' ')[:-1]
    while(data[-1] == '\n'):
        data = data[:-1]
    for i in range(len(data)):
        if data[i][0] == '\n':
            data [i] = data[i][1:]

    OriginalImage = np.zeros((H, W, 3))

    for i in range(H):
        for j in range(W):
            for k in range(3):
                OriginalImage[i][j][k] = int(data[i*W + j][k * 2: k * 2 + 2], 16)
    return W, H, OriginalImage

def showImage(data, fileName):
    h = len(data)
    w = len(data[0])
    pict = Image.new("RGB", (h,w))
    draw = ImageDraw.Draw(pict)
    for i in range(h):
        for j in range(w):
            r = int(math.fabs(data[i][j][0]))
            g = int(math.fabs(data[i][j][1]))
            b = int(math.fabs(data[i][j][2]))
            draw.point((j,i), (r,g,b))
    pict.save(fileName, "JPEG")
    del draw


def SrednArif(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            P = image[i][j][0] + image[i][j][1] + image[i][j][2]
            P /= 3
            image[i][j] = P
    return image

def myReshape(image, num):
    new = np.ones((len(image), len(image[0])))
    for i in range(len(image)):
        for j in range(len(image[i])):
            new[i][j] = image[i][j][num]
    return new

def myReReshape(image):
    new = np.ones((len(image), len(image[0]), 3))
    for i in range(len(image)):
        for j in range(len(image[i])):
            new[i][j][0] = image[i][j]
            new[i][j][1] = image[i][j]
            new[i][j][2] = image[i][j]
    return new

def calculateGradients(OriginalImage):
    H, W = OriginalImage.shape
    NewImage = np.zeros((H+2,W+2))
    Gradients = np.zeros((H,W,2))
    for j in range(W):
        NewImage[0][j + 1] = OriginalImage[0][j]
        NewImage[H + 1][j + 1] = OriginalImage[H - 1][j]

    for i in range(H):
        NewImage[i + 1][0] = OriginalImage[i][0]
        NewImage[i + 1][W + 1] = OriginalImage[i][W - 1]
        for j in range(W):
            NewImage[i+1][j+1] = OriginalImage[i][j]

    for i in range(H):
        for j in range(W):
            Gradients[i][j][0] = NewImage[i+1][j+2] - NewImage[i+1][j]
            Gradients[i][j][1] = NewImage[i+2][j+1] - NewImage[i][j+1]
    return Gradients


def SrednVzv(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            Y = (image[i][j][0] * 0.299) + (image[i][j][1] * 0.587) + (image[i][j][2] * 0.114)
            image[i][j] = Y
    return image

def IngvarrsReshape(image):
    NewImage = np.zeros(image.shape)
    for i in range(len(image)):
        for j in range(len(image[i])):
            V = image[i][j][0]
            NewImage[i][j] = V
    return NewImage

def removeEdges(image):
    H,W = image.shape
    Hnew = H - (H % 8)
    Wnew = W - (W % 8)
    newI = np.zeros((Hnew, Wnew))
    for i in range(Hnew):
        for j in range(Wnew):
            newI[i][j] = image[i][j]

    return newI

def magnitudeAndDirection(Gradients):
    H, W, trashCan = Gradients.shape
    MD = np.zeros((H, W, 2))
    for i in range(H):
        for j in range(W):
            MD[i][j][0] = math.sqrt(Gradients[i][j][0]**2 + Gradients[i][j][1]**2)
            #if(i == H - 1):
            #    print(Gradients[i][j][0], Gradients[i][j][1])
            if(Gradients[i][j][0] == 0):
                MD[i][j][1] = ((np.arctan(Gradients[i][j][1] /  0.0001) / np.pi) * 180)
            else:
                MD[i][j][1] = ((np.arctan(Gradients[i][j][1] /  Gradients[i][j][0]) / np.pi) * 180)
            if MD[i][j][1] < 0:
                MD[i][j][1] += 180
    return MD

def calculateHOG(Gradients, cells):
    H, W, trashCan = Gradients.shape
    H8 = H / cells
    W8 = W / cells
    H8 = int(H8)
    W8 = int(W8)
    HOGs = np.zeros((H8, W8, 9))
    for i in range(H):
        for j in range(W):
            D = Gradients[i][j][1]
            M = Gradients[i][j][0]
            #print(D)
            box = int(D / 20)
            ratio1 = D - box * 20
            ratio2 = 20 - ratio1
            box2 = box + 1
            if(box == 8):
                box2 = 0
            HOGs[int(i / cells)][int(j / cells)][box] += ratio1 * M
            HOGs[int(i / cells)][int(j / cells)][box2] += ratio2 * M
    return HOGs

def sin(a):
    return np.sin(a)

def cos(a):
    return np.cos(a)

def countHOGboxesForGr(Gr):
    lezh = 0
    stoj = 0
    for i in Gr:
        for j in i:
            lezh += sin(j[1] * (np.pi / 180)) * j[0]
            stoj += math.fabs(cos(j[1] * (np.pi / 180))) * j[0]
            #print(i, j, sin(k * (np.pi / 6)) * j[k], math.fabs(cos(k * (np.pi / 6))) * j[k])
    return list([lezh, stoj])

def countHOGboxes(HOG):
    lezh = 0
    stoj = 0
    for i in HOG:
        for j in i:
            for k in range(len(j)):
                lezh += sin(k * (np.pi / 9)) * j[k]
                stoj += math.fabs(cos(k * (np.pi / 9))) * j[k]
                #print(i, j, sin(k * (np.pi / 6)) * j[k], math.fabs(cos(k * (np.pi / 6))) * j[k])
    return list([lezh, stoj])


W, H, OriginalImage = IngvarrsInput()

#(W, H, OriginalImage) = InputFromConsole()

#(W, H, OriginalImage) = InputFromFile("stdin-000")

#showImage(OriginalImage, "ans0.jpg")

OriginalImage = SrednVzv(OriginalImage)
OriginalImage = myReshape(OriginalImage, 1)
#print(OriginalImage)

#OriginalImage = resize(OriginalImage, 124,)

OriginalImage = removeEdges(OriginalImage)

Gradients = calculateGradients(OriginalImage)

#showImage(myReReshape(myReshape(Gradients, 0)), "ansx.jpg")
#showImage(myReReshape(myReshape(Gradients, 1)), "ansy.jpg")

Gradients = magnitudeAndDirection(Gradients)

#showImage(myReReshape(myReshape(Gradients, 0)), "ansMa.jpg")
#showImage(myReReshape(myReshape(Gradients, 1)), "ansDe.jpg")


#HOG = calculateHOG(Gradients, 8)
#showImage(myReReshape(myReshape(HOG, 4)), "ansHOG90.jpg")
#showImage(myReReshape(myReshape(HOG, 0)), "ansHOG0.jpg")

#lezh, stoj = countHOGboxes(HOG)
lezh, stoj = countHOGboxesForGr(Gradients)
#print(countHOGboxes(HOG))

if(lezh == 0 and stoj == 0):
    print("0")
elif(lezh == 0):
    print("1")
elif(stoj == 0):
    print("2")
elif(stoj > lezh):
    if(stoj / lezh < 1.25):
        print("0")
    else:
        print("1") # stoji
else:
    if(lezh / stoj < 1.25):
        print("0")
    else:
        print("2") # lezhi
