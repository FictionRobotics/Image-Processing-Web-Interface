import cv2
import numpy as np


def nothing(x):
    pass

cap = cv2.VideoCapture(1)

##cv2.namedWindow("Trackbars")
##cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
##cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
##cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
##cv2.createTrackbar("U-H","Trackbars",180,180,nothing)
##cv2.createTrackbar("U-S","Trackbars",255,255,nothing)
##cv2.createTrackbar("U-V","Trackbars",255,255,nothing)
##
##
kernelopen = np.ones((5,5))
kerneclose = np.ones((20,20))







##############################################################################
def redcolor():

    

    
##    low_red = np.array([l_h, l_s, l_v])
##    high_red = np.array([u_h, u_s, u_v])

    low_red = np.array([162, 52, 0])
    high_red = np.array([180, 255, 255])

    red_mask=cv2.inRange(hsv,low_red,high_red)
    
    maskopen_red=cv2.morphologyEx(red_mask,cv2.MORPH_OPEN,kernelopen)
    maskclose_red=cv2.morphologyEx(maskopen_red,cv2.MORPH_CLOSE,kerneclose)
    maskfinal_red=maskclose_red
    
    contours_red,h= cv2.findContours(maskfinal_red.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    for cnt_red in contours_red:
        area = cv2.contourArea(cnt_red)
       # print(area)
        if area>2000:
            #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
            x,y, w, h = cv2.boundingRect(cnt_red)
            cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
            cv2.putText(frame, "Red package", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),2)
            return 'r'


############################################################################## 
def greencolor():

    
##    low_green = np.array([l_h, l_s, l_v])
##    high_green = np.array([u_h, u_s, u_v])

    low_green = np.array([24, 61, 35])
    high_green = np.array([92, 255, 255])

    green_mask=cv2.inRange(hsv,low_green,high_green)
    
    maskopen_green=cv2.morphologyEx(green_mask,cv2.MORPH_OPEN,kernelopen)
    maskclose_green=cv2.morphologyEx(maskopen_green,cv2.MORPH_CLOSE,kerneclose)
    maskfinal_green=maskclose_green
    
    contours_green,h= cv2.findContours(maskfinal_green.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    for cnt_green in contours_green:
        area = cv2.contourArea(cnt_green)
        #print(area)
        if area>2000:
            #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
            x,y, w, h = cv2.boundingRect(cnt_green)
            cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
            cv2.putText(frame, "green package", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),2)
            return 'g'

###############################################################################

def bluecolor():

    
##
##    low_blue = np.array([l_h, l_s, l_v])
##    high_blue = np.array([u_h, u_s, u_v])

    low_blue = np.array([120, 61, 0])
    high_blue = np.array([148, 255, 255])

    blue_mask=cv2.inRange(hsv,low_blue,high_blue)
    
    maskopen_blue=cv2.morphologyEx(blue_mask,cv2.MORPH_OPEN,kernelopen)
    maskclose_blue=cv2.morphologyEx(maskopen_blue,cv2.MORPH_CLOSE,kerneclose)
    maskfinal_blue=maskclose_blue
    
    contours_blue,h= cv2.findContours(maskfinal_blue.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    for cnt_blue in contours_blue:
        area = cv2.contourArea(cnt_blue)
       # print(area)
        if area>3000 :
            #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
            x,y, w, h = cv2.boundingRect(cnt_blue)
            cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
            cv2.putText(frame, "blue package", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255),2)
            return 'b'

#############################################################################


while True:  
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


##    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
##    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
##    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
##    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
##    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
##    u_v = cv2.getTrackbarPos("U-V", "Trackbars")



            

    
    redcolor()
    if redcolor() == 'r':
        print('red detected')
        
        
    


    greencolor()
    if greencolor() == 'g':
        print('green detected')
            



    bluecolor()
    if bluecolor() == 'b':
        print('blue detected')
            
        

    
    cv2.imshow("feed", frame)
##    cv2.imshow("mask", blue_mask)
##    cv2.imshow("mask111", maskclose_blue)
  

    key = cv2.waitKey(1)
    if key== 27:
        break
cap.release()
cv2.destroyAllWindows()
