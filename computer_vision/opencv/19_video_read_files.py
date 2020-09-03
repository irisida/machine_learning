import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("VideoED.mp4")

if cap.isOpened() is False:
    print("ERROR -> file not found")

while cap.isOpened():
    ret, frame = cap.read()

    if ret is True:
        cv2.imshow("frame", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
