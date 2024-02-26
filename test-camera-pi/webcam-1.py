import cv2
import time

num = 1
cap = cv2.VideoCaptura(0)

while True:
    ret, img = cap.read()
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite('home/oscpi/Pictures/'+str(num)+'.jpg', img)
        print('Captures', str(num))
        num += 1
    if num == 4:
        break
cap.release()
cv2.destroyAllWindows()