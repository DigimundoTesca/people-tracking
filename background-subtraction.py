import numpy as np 
import cv2

cap=cv2.VideoCapture('vtest.avi')
fgbg=cv2.createBackgroundSubtractorMOG2()
fgbg2=cv2.createBackgroundSubtractorMOG2(500, 16, False)

# fgbg=cv2.BackgroundSubtractorMOG()
while(1):
  ret, frame=cap.read()
  fgmask=fgbg.apply(frame)
  fgmask2=fgbg2.apply(frame)
  # cv2.imshow('Video',frame)
  cv2.imshow('fgmask', fgmask)
  cv2.imshow('fgmask2', fgmask2)
  k=cv2.waitKey(30) & 0xFF
  if k==27:
    break

cap.release()
cv2.destroyAllWindows()