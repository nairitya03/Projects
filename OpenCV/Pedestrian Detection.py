import cv2 
import numpy as np



body_classifier = cv2.CascadeClassifier('F:\Learning\OpenCV\Haarcascade\haarcascade_fullbody.xml')


video_cap = cv2.VideoCapture('run.mp4')


while True:
  ret,frame = video_cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
  if ret == True:
    for (x,y,w,h) in body_classifier.detectMultiScale(gray,1.18,2):
      cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),4)

      cv2.imshow("Pedestrian Detection",frame)
    
    if cv2.waitKey(1) == 27:
      break
  
  else:
    break

video_cap.release()
cv2.destroyAllWindows()
