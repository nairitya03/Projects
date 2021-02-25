## Import Libraries
import os
from PIL import Image

#Fancy ASCII text...
import pyfiglet

print(pyfiglet.figlet_format("Image Croper", font = "bulbhead" ).center(30))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ).ljust(30))
print("-"*70,"\n")

#define a funtion To accept image and resize it
def Resize(item):
    
    #oepn and safe image in a variable
    image=Image.open(item)
    
    #split the name of the image into name and extention
    img_name, img_ext = os.path.splitext(item)
    
    #user input width and height for resizing
    w,h = map(int, input("Enter the new size Width * Height >>>").strip().split('*'))
    
    #calling the resize funtion
    img_resized = image.resize((w,h), Image.ANTIALIAS)
    
    ##saving new resized image 
    img_resized.save(img_name + '_newsize_' + img_ext, 'JPEG',quality=95)
    
    
    print("\nImage has been Resized Successfully")
    
    
## self invoking constructor        
if __name__ == '__main__':
    
    #take image path from user
    path = input("Enter the path of image >>")
    
    #resize funtion call
    Resize(path)
        
        
