import os
import cv2

#read image
img = cv2.imread(os.path.join('.', 'data', 'bird.jpg'))

resized_img = cv2.resize(img, (540,720))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img',img)
cv2.imshow('resized_img', resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()