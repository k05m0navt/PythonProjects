import numpy, json
eyeLeftOuter = [252.0, 331.0]
noseTip = [520.0, 634.0]
eyeRightOuter = [782.0, 321.0]
ex2x = []
ex2y = []
ex = json.loads(input())
copy = ex.copy()

ex2x.append(ex[0]["faceLandmarks"]["eyeLeftOuter"]["x"])
ex2y.append(ex[0]["faceLandmarks"]["eyeLeftOuter"]["y"])
ex2x.append(ex[0]["faceLandmarks"]["noseTip"]["x"])
ex2y.append(ex[0]["faceLandmarks"]["noseTip"]["y"])
ex2x.append(ex[0]["faceLandmarks"]["eyeRightOuter"]["x"])
ex2y.append(ex[0]["faceLandmarks"]["eyeRightOuter"]["y"])
del copy[0]['faceLandmarks']['eyeLeftOuter'], copy[0]['faceLandmarks']['noseTip'], copy[0]['faceLandmarks']['eyeRightOuter']
ex2x.append(list(copy[0]["faceLandmarks"].values())[0]["x"])
ex2y.append(list(copy[0]["faceLandmarks"].values())[0]["y"])

arr1 = [1.0, eyeLeftOuter[0], eyeLeftOuter[1]], [1.0, noseTip[0], noseTip[1]], [1.0, eyeRightOuter[0], eyeRightOuter[1]]
arr2 = [ex2x[0], ex2x[1], ex2x[2]]
arr4 = [ex2y[0], ex2y[1], ex2y[2]]
M1 = numpy.array(arr1)
V1 = numpy.array(arr2)
V2 = numpy.array(arr4)
a0, a1, a2 = numpy.linalg.solve(M1, V1)[0], numpy.linalg.solve(M1, V1)[1], numpy.linalg.solve(M1, V1)[2]
b0, b1, b2 = numpy.linalg.solve(M1, V2)[0], numpy.linalg.solve(M1, V2)[1], numpy.linalg.solve(M1, V2)[2]
arr5 = [a1, a2], [b1, b2]
arr6 = [ex2x[3] - a0, ex2y[3] - b0]
M2 = numpy.array(arr5)
V3 = numpy.array(arr6)

x, y = int(numpy.linalg.solve(M2, V3)[0]), int(numpy.linalg.solve(M2, V3)[1])
print(x, y)
