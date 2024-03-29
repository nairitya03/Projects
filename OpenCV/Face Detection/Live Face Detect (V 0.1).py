#importing Necessary Libray !!
import cv2
import pyfiglet 

# ASCII Text Art
print(pyfiglet.figlet_format("Live Face Detect", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

#Creating local Cascade classifiers !
faceCascade = cv2.CascadeClassifier('F:\GitHub Repositories\Projects\OpenCV\haarcascade\haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('F:\GitHub Repositories\Projects\OpenCV\haarcascade\haarcascade_eye.xml')

#Assigning the HARDWARE(WEBCAMERA) to the program !!
try:
    video_capture=cv2.VideoCapture(0)

    
    #Creating a Name Format for saving the TEST RESULTS !!
    img_counter=0

    print("Press \"SpaceBar\" to Save Image")
    print("Press \"Enter\" to Exit Image")


    while True:
    #Capture Frame-by-Frame Live Stream !!

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k=cv2.waitKey(1)


    #Detecting Face !!
    ##faces = faceCascade.detectMultiScale(gray,1.3,4)
    ##Detecting Eyes !!
    #eyes = eyeCascade.detectMultiScale(gray,1.3,6)

    #loop For Continuos Detection !!

        for (x, y, w, h) in faceCascade.detectMultiScale(gray,1.3,4):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            for (x, y, w, h) in eyeCascade.detectMultiScale(gray,1.3,6):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 230, 255), 2)

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

except:
    print("Error 101: Could not read input from webcam")
