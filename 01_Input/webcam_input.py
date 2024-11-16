import cv2

#Read webcam
webcam = cv2.VideoCapture(0)

#visualize webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('Webcam Video', frame)

    #Terminate the loop by pressing letter 'q'
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
