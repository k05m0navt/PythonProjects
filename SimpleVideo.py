import cv2
cap = cv2.VideoCapture('36.mp4')
i = 0
p = 1
arr = [0]
while(True):
    try:
        ret, frame = cap.read()
        arr[0] = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hist1 = cv2.calcHist([gray],[0],None,[256],[0,256])
        if p > 1:
            if (int(cv2.compareHist(hist1,hist2,cv2.HISTCMP_BHATTACHARYYA)*100) != 0.0):
                i += 1
                p += 1
                buffer = cv2.cvtColor(arr[0], cv2.COLOR_BGR2GRAY)
                hist2 = cv2.calcHist([buffer],[0],None,[256],[0,256])
    except:
    break
print(i)
