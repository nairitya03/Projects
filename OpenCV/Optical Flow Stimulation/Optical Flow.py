import cv2 
import numpy as np
import pyfiglet 

# ASCII Text Art
print(pyfiglet.figlet_format("Optical Flow", font = "bulbhead" ))
print(pyfiglet.figlet_format("Created By @FaLLenGuY", font = "digital" ))
print("-"*70,"\n")

#Parameters For Shi-Tomasi Corner detections

st_param = dict (maxCorners=30,
                qualityLevel=0.2,
                minDistance=2,
                blockSize=7)

#Parameters For Lucas-Kande optical flow

lk_param = dict(winSize=(15,15),
               maxLevel=2,
               criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1))

#Video Capture

video_cap = cv2.VideoCapture('Optical Video.mp4')

#color for optical flow

color = (0,243,0)

#Read the capture and get the first frame
ret,first_frame = video_cap.read()

#convert frame to gray sccale
prev_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)

#find the strongest corners in the first frame
prev = cv2.goodFeaturesToTrack(prev_gray,mask= None,**st_param)

#create an  image with the same distance as the frame 
mask = np.zeros_like(first_frame)
cap=True
#while Loop
while(cap):
    
    ret,frame = video_cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    next,status,error = cv2.calcOpticalFlowPyrLK(prev_gray,gray,prev,None,**lk_param)
    
    good_old = prev[status==1]
    
    good_new = next[status==1]
    
    for i ,(new,old) in enumerate(zip(good_new,good_old)):
        a,b =new.ravel()
        
        c,d = old.ravel()
        
        
        mask = cv2.line(mask,(round(a),round(b)),(round(c),round(d)),color,3)
        
        frame = cv2.circle(frame,(round(a),round(b)),2,color,-1)
        
        output = cv2.add(frame,mask)
        
        prev_gray= gray.copy()
        
        prev = good_new.reshape(-1,1,2)
        
        cv2.imshow("Optical Flow",output)
        
    if cv2.waitKey(100) & 0xFF== ord("q"):
        cap=False
            
video_cap.release()
cv2.destroyAllWindows()
