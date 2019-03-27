import numpy as np
import cv2

imagemOriginal = cv2.imread('biel.png', cv2.IMREAD_GRAYSCALE)

#kernel = np.ones((5, 5), np.float32)/25;
#imagemFiltrada = cv2.filter2D(imagemOriginal, -1, kernel)
imagemGaussiana = cv2.GaussianBlur(imagemOriginal, (5, 5),0)
imagemMediaBlur = cv2.blur(imagemOriginal, (5, 5))
kernel = np.array([[-1, -1, -1],
                  [-1, 9, -1],
                  [-1, -1, -1]])

sharpened =cv2.filter2D(imagemOriginal, -1, kernel)

cv2.imshow('Imagem Original', imagemOriginal)
cv2.imshow('Imagem Gaussiana', imagemGaussiana)
cv2.imshow('Imagem Blur', imagemMediaBlur)
cv2.imshow('Imagem kernel definido', sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()