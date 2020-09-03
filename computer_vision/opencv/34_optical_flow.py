#!/usr/bin/env python
# coding: utf-8

# # Optical Flow

# Optical flow is the pattern of apparent motion of image objects betwen two consecutive frames caused by the movement of the object or of the camera.
#
# #### Assumptions are:
# - pixel intesities of an object do not change between consecutive frames.
# - neighbouring pixels have a similar motion.
#
# #### Usage caveats:
# - The Lucas-Kanade operates on a sparse feature set.
# - This meansit *only* takes care and tracks the points it was told to track.
# - optical flow methods in openCV take in a given set of points and a frame.
# - it will look for those points in the next frame.
# - The user supplies the points to be tracked.
# - we pass the points and the previous frame to the Lucas-Kanade function.
#
#
# If you want to track all the points in a video the `Gunner Farneback` algorithm may be amore appropriate choice to calculate dense optical flow. This calculates all the points in a video, colouring them black where no flow is detected.

# In[2]:


import cv2
import numpy as np


# ## Lucas Kanade method

# In[3]:


# 'maxCorners' number of best quality point to detect
# 'qualityLevel'
# 'minDistance'
# 'blockSize'
# all used for corner detection
corner_track_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)


# In[4]:


# params for the Lucas Kanade function to be called.
# 'winSize' is a trade off between small (more sensitive to
# noise, less to fast motion) and large (less sensitivity,
# but better for fast motion)
# 'maxLevel' is related to the image pyramid, multi-layer,
# multi-resolution imaging.
# EPS vs COUNT is about speed vs accuracy
lk_params = dict(
    winSize=(200, 200),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)


# ## Load the video data

# In[7]:


cap = cv2.VideoCapture(0)

ret, prev_frame = cap.read()

prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# declare the points
prevPts = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_params)

# use mask for visualising / drawing on
mask = np.zeros_like(prev_frame)

while True:
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calc the optical flow
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(
        prev_gray, frame_gray, prevPts, None, **lk_params
    )

    good_new = nextPts[status == 1]
    good_prev = prevPts[status == 1]

    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = new.ravel()
        x_prev, y_prev = prev.ravel()

        mask = cv2.line(
            mask, (x_new, y_new), (x_prev, y_prev), (0, 255, 0), thickness=3
        )

        frame = cv2.circle(frame, (x_new, y_new), 8, (0, 0, 255), thickness=2)

    img = cv2.add(frame, mask)
    cv2.imshow("Tracking", img)

    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1, 1, 2)


cv2.destroyAllWindows()
cap.release()


# In[ ]:


# In[ ]:


# In[ ]:

