#importing Necessary Libray !!

import cv2


#Creating local Cascade classifiers !
faceCascade = cv2.CascadeClassifier('haarcascade_profileface.xml')

eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Assigning the HARDWARE(WEBCAMERA) to the program !!
video_capture=cv2.VideoCapture(0)

#Creating a Name Format for saving the TEST RESULTS !!
img_counter=0


while True:
#Capture Frame-by-Frame Live Stream !!

    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k=cv2.waitKey(1)


#Detecting Face !!
 
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(20,20),
    )
    for (x, y, w, h) in faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(20,20),
    ):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)


#Detecting Eyes !!

##    eyes = eyeCascade.detectMultiScale(
##        gray,
##        scaleFactor=1.2,
##        minNeighbors=7,
##        minSize=(30, 30),
##    )
##    for (x, y, w, h) in eyes:
##        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 230, 255), 2)

#Live Result Displaying !!

    cv2.imshow('FaceDetection', frame)



#Capture The Detected Image !!
    if k%256 == 32:
        img_name = "Facedetect_webcam_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} SAVED!".format(img_name))
        img_counter += 1


#Terminate the Program !!
    elif k%256 == 13: 
        break

#Destroy all intermediate Windows during Excecutionv!!
cv2.destroyAllWindows()


#SYSTEM Release of the HARDWARE !!
video_capture.release()

