import cv2

cap = cv2.VideoCapture(0)

# callback
def draw_rect(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, bottomRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:

        # reset
        if topLeft_clicked and bottomRight_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            bottomRight_clicked = False

        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True

        elif not bottomRight_clicked:
            pt2 = (x, y)
            bottomRight_clicked = True


# globals
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
bottomRight_clicked = False

cap = cv2.VideoCapture(0)

cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_rect)

while True:
    ret, frame = cap.read()

    # draw baed on globals
    if topLeft_clicked:
        cv2.circle(frame, pt1, 5, (0, 0, 255), -1)

    if topLeft_clicked and bottomRight_clicked:

        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), thickness=2)

    cv2.imshow("Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
