import cv2
import time

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    "VideoED.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height)
)

while True:
    ret, frame = cap.read()

    writer.write(frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(1 / 30)
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
