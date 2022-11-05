import cv2 as cv

#detecting pistol and guns

image = cv.imread('arma.jpg')
cascade = cv.CascadeClassifier("treinamento/cascade.xml")
objects = cascade.detectMultiScale(image, 1.3, 5)

for (x, y, w, h) in objects:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv.imshow('imagem de arma', image)


cv.waitKey(0) 
cv.destroyAllWindows()
