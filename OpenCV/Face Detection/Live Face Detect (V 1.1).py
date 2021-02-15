# importing Necessary Libray !!
import cv2
import pyfiglet 

# ASCII Text Art
print(pyfiglet.figlet_format("Live Face Detect", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

# Declaring global Variables
global faceCascade
global eyeCascade

# Creating local Cascade classifiers !
faceCascade = cv2.CascadeClassifier('Haarcascade\haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('Haarcascade\haarcascade_eye.xml')


def live():

    # Assigning the HARDWARE(WEBCAMERA) to the program !!
    video_capture=cv2.VideoCapture(0)

    # Creating a Name Format for saving the TEST RESULTS !!
    img_counter=0

    print("Press \"SpaceBar\" to Save Image")
    print("Press \"Enter\" to Exit Image")

    while True:

        # Capture Frame-by-Frame Live Stream !!
        ret, frame = video_capture.read()

        # Gray Scale Conversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        k=cv2.waitKey(1)

        # loop For Continuos Detection !!
        for (x, y, w, h) in faceCascade.detectMultiScale(gray,1.3,4):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            for (x, y, w, h) in eyeCascade.detectMultiScale(gray,1.3,6):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 230, 255), 2)

        # Live Result Displaying !!
        cv2.imshow('FaceDetection', frame)
        print("The number of faces found = ", len(faceCascade.detectMultiScale(gray,1.2,6)))
        
        # Capture The Detected Image !!
        if k%256 == 32:
            img_name = "Facedetect_webcam_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} SAVED!".format(img_name))
            img_counter += 1


        # Terminate the Program !!
        elif k%256 == 13: 
            break

    # SYSTEM Release of the HARDWARE !!
    video_capture.release()

    
# Function to detect Face from an image !!
def static():

    # Declaring global Variables
    global faceCascade
    
    # Input Image path
    path=input("Enter Image path \n>>> ")
    image = cv2.imread(path)

    #get Image Size
    #dimensions = image.shape
    #print(dimensions)
    #height = image.shape[0]
    #width = image.shape[1]
    #if (width >= 640 and height >= 480):
    img_scale = cv2.resize(image,(1024,768),interpolation=cv2.INTER_AREA)
    #else:
       # img_scale = image

    # Gray Scale Conversion
    gray = cv2.cvtColor(img_scale, cv2.COLOR_BGR2GRAY)

    # loop For Multiple Detection !!
    for (x,y,w,h) in faceCascade.detectMultiScale(gray,1.3,4):
        cv2.rectangle(img_scale, (x,y), (x+h, y+h), (0, 255, 0), 2)

    # Result Displaying !!
    cv2.imshow("Faces found", img_scale)    
    print("The number of faces found = ", len(faceCascade.detectMultiScale(gray,1.2,6)))

    cv2.waitKey(0)
    
#switch Function to toggle between feeds
def switch(case):

    if case == 1:
        live()
        
    elif case == 2:
        static()
   
# Constructor call    
if __name__=='__main__':

    choice = 0
    
    while choice != 1 or choice != 2:
        choice = int(input ("Enter your Choice !"
                  "\n 1: Live Feed Face Detection"
                  "\n 2: Image Input Face Detection"
                  "\n >>>"
                  ))
        

        if choice == 1 or choice == 2:
            break
        else:
            print("\nInvalid Choice... Try Again !! \n")

    switch(choice)
    
    # Destroy all intermediate Windows during Excecutionv!!
    cv2.destroyAllWindows()

    
