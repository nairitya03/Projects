import cv2
import pyfiglet 

print(pyfiglet.figlet_format("Face Detect", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")


path=input("Enter Image path \n>>> ")

image = cv2.imread(path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('F:\GitHub Repositories\Projects\OpenCV\Haarcascade\haarcascade_frontalface_default.xml')

print("The number of faces found = ", len(face_cascade.detectMultiScale(gray,1.2,6)))

for (x,y,w,h) in face_cascade.detectMultiScale(gray,1.2,6):
    cv2.rectangle(image, (x,y), (x+h, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)    

cv2.waitKey(0)
cv2.destroyAllWindows()
  
