import os
import cv2


img = cv2.imread(os.path.join('.', 'whiteboard.png'))

print(img.shape)

# line (parameters -> 2.starting point 3.End point 4.Line Color 5.Thickness of the Line)
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

# rectangle (parameters -> 2.top left point 3.bottom right point 4.rectangle Color 5.Thickness of the rectangle border)
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), -1)

# circle (parameters -> 2.center point 3.radius 3.color 4.thickness)
cv2.circle(img, (800, 200), 75, (255, 0, 0), 10)

# text (parameters) -> 2.text we want 3.position of text 4.font 5.size of text 6.color of text 7.thickness)
cv2.putText(img, 'Hellooo', (600, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)

cv2.imshow('img', img)
cv2.waitKey(0)