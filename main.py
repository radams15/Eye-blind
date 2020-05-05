import numpy as np
import serial
import time
import sys
import cv2

arduino = serial.Serial('/dev/ttyUSB0', 9600)
CAM = 0

light = 1

def goto(x, y):
	data = "X{}Y{}Z".format(int(x), int(y))
	print ("output = '" +data+ "'")
	arduino.write((data+"\n").encode())
	
def led_toggle():
	global light
	goto(-2, 0);
	light = not light
	
goto(-1, -1);


cascade = cv2.CascadeClassifier('face.xml')

cap = cv2.VideoCapture(CAM)

ret, img = cap.read()
cv2.imshow('img',img)
	

while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500,500)
    img = cv2.flip(img, 1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.3)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
        print (arr)
        
        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))

        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2

        print (xx)
        print (yy)
        
        xx = img.shape[1] - xx
        yy = img.shape[0] - yy

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        goto(xx, yy)
        break
#    else:
#        goto(-1, -1)
    

    cv2.imshow('img',img)
   
    k = cv2.waitKey(30) & 0xff
    if k == ord("q"):
        break
    if k == ord("l"):
        led_toggle()

        
goto(-1, -1);
if light:
	led_toggle()
