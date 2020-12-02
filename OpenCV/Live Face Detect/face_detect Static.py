import cv2

# Function for detection of face
def detect():
    img_path=('nasa.png')


# Create the haar cascade
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Read the image
    image = cv2.imread(img_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
# faces = faceCascade.detectMultiScale(gray,1.5,4)

# Draw a rectangle around the faces
    for (x, y, w, h) in faceCascade.detectMultiScale(gray,1.3,4):
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)

    print("Found {0} faces!".format(len(faceCascade.detectMultiScale(gray,1.2,5))))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

detect()
