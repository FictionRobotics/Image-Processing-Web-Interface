#from gpiozero import Servo, Motor
from time import sleep
#import serial
import socket
import time
import cv2
import numpy as np


#port = serial.Serial("/dev/rfcomm2", baudrate=9600)
'''
motor1 = Motor(20,21,16)

motor2 = Motor(26,19,13)

servo1 = Servo(17)

servo2 = Servo(27)
'''

msg_user=[]
msg_pack=[]
msg_num=[]

kernelopen = np.ones((5,5))
kerneclose = np.ones((20,20))







##############################################################################
def redcolor():

    while True:
        
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

        
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
            if area>30000:
                #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
                x,y, w, h = cv2.boundingRect(cnt_red)
                cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
                cv2.imshow("feed", frame)

                return 'r'
                
        key = cv2.waitKey(1)
        if key== 27:
            break


############################################################################## 
def greencolor():

    while True:  
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
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
            if area>30000 and area<70000:
                #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
                x,y, w, h = cv2.boundingRect(cnt_green)
                cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
                cv2.imshow("feed", frame)

                return 'g'
                break
        key = cv2.waitKey(1)
        if key== 27:
            break


###############################################################################

def bluecolor():

    while True:  
        _,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
##
    ##    low_blue = np.array([l_h, l_s, l_v])
    ##    high_blue = np.array([u_h, u_s, u_v])

        low_blue = np.array([104, 69, 0])
        high_blue = np.array([147, 255, 255])

        blue_mask=cv2.inRange(hsv,low_blue,high_blue)
        
        maskopen_blue=cv2.morphologyEx(blue_mask,cv2.MORPH_OPEN,kernelopen)
        maskclose_blue=cv2.morphologyEx(maskopen_blue,cv2.MORPH_CLOSE,kerneclose)
        maskfinal_blue=maskclose_blue
        
        contours_blue,h= cv2.findContours(maskfinal_blue.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        
        for cnt_blue in contours_blue:
            area = cv2.contourArea(cnt_blue)
           # print(area)
            if area>10000:
                #cv2.drawContours(frame,cnt, -1, (255, 0, 0), 5)
                x,y, w, h = cv2.boundingRect(cnt_blue)
                cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),3)
                cv2.imshow("feed", frame)

                
                return 'b'
                
        key = cv2.waitKey(1)
        if key== 27:
            break


def armaction():

    servo2.value = -0.7

    sleep(2)

    servo1.value = -0.8

    sleep(2)

    servo2.value = 0.7

    sleep(2)

    servo1.mid()

    sleep(2)

    motor1.forward(0.2)

    sleep(0.86)

    motor1.stop()

    sleep(2)

    servo1.value = -0.6

    sleep(2)

    servo2.mid()

    sleep(2)

    servo1.mid()

    sleep(2)

    motor1.backward(0.2)
    
    sleep(0.84)

    motor1.stop()
    
    sleep(3)

    arm=1


def conveyer_start():
    
    motor2.forward(0.5)

def conveyer_stop():
    
    motor2.stop(0.5)

def main():
    
    y=0
  
    print("DIGITAL LOGIC -- > SENDING...")
    x=str('i')
    port.write(bytes(x,'utf-8'))

    rec = port.readline()

    if (rec == bytes("start\n","utf-8")):
        
        
        

        while(y<3):
        
            
            conveyer()
    
            sleep(1)
    
            armaction()

            print("CARGO PLACED ON DELIVERY BOT...")
          
            y = y +1

            x=0
            
def server():

    global msg_user
    global msg_pack
    global msg_num

    host=""
    port=5000

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("127.0.0.1",port))

    print("server started ready for input")
    s.listen(5)

    c,addr=s.accept()

    for x in range(0,3):
        y=c.recv(1024)
        msg_user.append(y.decode('UTF-8'))
        if msg_user[x]==b'x':
            break
        #print("USER:",str(msg_user[x]))
        time.sleep(1)
        y=c.recv(1024)
        msg_pack.append((y.decode('UTF-8')))
       # print("PACKAGE:",msg_pack)
        time.sleep(1)
        y=c.recv(1024)
        msg_num.append((y.decode('UTF-8')))
      #  print("NUMBER OF PACKAGE REQUIRED:",msg_num)
        time.sleep(1)
    print("FINAL ORDER IS:")
    print("USER                      :",msg_user)
    print("PACKAGE                   :",msg_pack)
    print("NUMBER OF PACKAGE REQUIRED:",msg_num)
    c.close()
    
    return

def main():
    global msg_user
    global msg_pack
    global msg_num
    server()
##    conveyer_start()
##    msg_pack=msg_pack.reverse()
##    for x in range(3):
##        if msg_pack[x]=="red":
##            if not (msg_num ==''):
##                for z in range(int(msg_num[x])):
##                    value1=redcolor()
##                    if value1=='r':
##                        conveyer_stop()
##                        armaction()
##        if msg_pack[x]=="blue":
##            if not (msg_num ==''):
##                for z in range(int(msg_num[x])):
##                    value1=bluecolor()
##                    if value1=='b':
##                        conveyer_stop()
##                        armaction()
##        if msg_pack[x]=="green":
##            if not (msg_num ==''):
##                for z in range(int(msg_num[x])):
##                    value1=greencolor()
##                    if value1=='g':
##                        conveyer_stop()
##                        armaction()
##        if msg_pack[x]=="":
##            conveyer_stop()
##
##    for y in range(3):
##            print("DIGITAL LOGIC -- > SENDING...")
##            x=msg_user[y]
##            port.write(bytes(x,'utf-8'))
        

    
    

if __name__ == "__main__":
    main()
    
