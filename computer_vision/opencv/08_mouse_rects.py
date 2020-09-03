import cv2
import numpy as np

# vars
drawing = False
ix, iy = -1, -1

# func
def draw_rect(event, x, y, flags, params):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, ix = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)


# img
img = np.zeros((800, 800, 3))

cv2.namedWindow(winname="my_art")
cv2.setMouseCallback("my_art", draw_rect)

while True:
    cv2.imshow("my_art", img)
    # await esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
