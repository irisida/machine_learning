# %%
import cv2

# %%
face_cascade = cv2.CascadeClassifier(
    "DATA/haarcascades/haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier("DATA/haarcascades/haarcascade_eye.xml")


# %%
def detect_eyes(img):
    face_img = img.copy()
    eye_rects = eye_cascade.detectMultiScale(face_img)

    for (x, y, w, h) in eye_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)

    return face_img


# %%
def detect_face(img):
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(
        face_img, scaleFactor=1.18, minNeighbors=4
    )

    for (x, y, w, h) in face_rects:
        cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 5)

    return face_img


cap = cv2.VideoCapture(0)

# %%
while True:
    ret, frame = cap.read(0)
    # frame = detect_face(frame)
    frame = detect_eyes(frame)

    cv2.imshow("", frame)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# %%
