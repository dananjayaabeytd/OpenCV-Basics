import os
import cv2

#read image
img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

print(img.shape)

cropped_img = img[70:640, 120:640]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)