import cv2
import numpy as np


result = 'change_video.avi'

threshold = 100.

cap = cv2.VideoCapture('videos/video_1.mp4')

ret, frame = cap.read()
height, width, nchannels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter(result, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20, (width, height))
count = 0

while True:

    # previous frame
    frame0 = frame

    # new frame
    ret, frame = cap.read()
    if not ret:
        break

    # how different is it?
    if np.sum(np.absolute(frame-frame0))/np.size(frame) > threshold:
        out.write(frame)
        count += 1

if count > 0:
    print('The video changed')
else:
    print('The video no changed')


# When everything done, release the capture
cap.release()
out.release()

print('The process is over')