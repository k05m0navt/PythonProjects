import numpy as np

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

def SrednArif(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            P = image[i][j][0] + image[i][j][1] + image[i][j][2]
            P /= 3
            image[i][j] = P
    return image

def SrednVzv(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            Y = (image[i][j][0] * 0.299) + (image[i][j][1] * 0.587) + (image[i][j][2] * 0.114)
            image[i][j] = Y
    return image

def NeuterAc(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            pixel = image[i][j]
            L = max(pixel[0], pixel[1], pixel[2]) + min(pixel[0], pixel[1], pixel[2])
            L /= 2
            image[i][j] = L
    return image

def Brightness(image):
    for i in range(len(image)):
        for j in range(len(image[i])):
            pixel = image[i][j]
            V = max(pixel[0], pixel[1], pixel[2])
            image[i][j] = V
    return image

def SrednGeoFilt(image):
    NewImage = image.copy()
    for i in range(1,len(image) - 1):
        for j in range(1,len(image[i]) - 1):
            for k in range(3):
                P = (image[i][j][k] * image[i][j - 1][k] * image[i][j + 1][k] * image[i - 1][j][k] * image[i - 1][j - 1][k] * image[i - 1][j + 1][k] * image[i + 1][j][k] * image[i + 1][j - 1][k] * image[i + 1][j + 1][k])
                P = P ** (1. / 9)
                NewImage[i][j][k] = P
    return NewImage

def MedianFilt(image):
    NewImage = image.copy()
    for i in range(1,len(image) - 1):
        for j in range(1,len(image[i]) - 1):
            for k in range(3):
                P = sort(list((image[i][j][k], image[i][j - 1][k], image[i][j + 1][k], image[i - 1][j][k], image[i - 1][j - 1][k], image[i - 1][j + 1][k], image[i + 1][j][k], image[i + 1][j - 1][k], image[i + 1][j + 1][k])))
                P = P[4]
                NewImage[i][j][k] = P
    return NewImage

W, H = input().split(' ')
W = int(W)
H = int(H)

OriginalImage = np.zeros((H, W, 3))

pixels = input().split(' ')
"""
while('' in pixels):
    pixels.remove('')
"""

for i in range(H):
    for j in range(W):
        for k in range(3):
            OriginalImage[i][j][k] = hexToFloat(pixels[i*W + j][k * 2: k * 2 + 2])



F = input()
D = input()
F = int(F)
D = int(D)


if(F == 1):
    OriginalImage = SrednGeoFilt(OriginalImage)
elif(F == 2):
    OriginalImage = MedianFilt(OriginalImage)

#print(OriginalImage[7][5])

if(D == 1):
    OriginalImage = SrednArif(OriginalImage)
elif(D == 2):
    OriginalImage = SrednVzv(OriginalImage)
elif(D == 3):
    OriginalImage = NeuterAc(OriginalImage)
elif(D == 4):
    OriginalImage = Brightness(OriginalImage)


#print(OriginalImage[7][5])

minV = OriginalImage.min()
maxV = OriginalImage.max()
print(minV.astype(np.int64), maxV.astype(np.int64))
