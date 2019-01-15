import cv2
import numpy as np

cap = cv2.VideoCapture('101.mp4')

l = 1
arr = [0]
q = []

while(True):
    try:
        ret, frame = cap.read()
        arr[0] = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hist1 = cv2.calcHist([gray],[0],None,[256],[0,256])
        if l > 1:
            if (int(cv2.compareHist(hist1,hist2,cv2.HISTCMP_BHATTACHARYYA)*100) != 0.0):
                q.append(buffer)
        l += 1
        buffer = cv2.cvtColor(arr[0], cv2.COLOR_BGR2GRAY)
        hist2 = cv2.calcHist([buffer],[0],None,[256],[0,256])
    except:
        q.append(gray)
        break


imagePull = []
for i in range(len(q)):
    new = True
    for j in imagePull:
        if np.allclose(q[i], j, 1.6, 2):
            new = False
    if new:
        imagePull.append(q[i])
print(len(imagePull))
