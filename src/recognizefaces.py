#!/usr/bin/env python

import cv2, os
import numpy as np
from PIL import Image
import sys

length=len(sys.argv)
if length < 2:
    sys.exit('\nAt least one argument required')
#print (' '.join(sys.argv[2:]));
if length < 3:
    vidPath = sys.argv[1]
    classPath = "Data.xml"
    logPath = "logvid"
    limit = 100
else:
    #cascPath = sys.argv[1]
    vidPath = sys.argv[1]
    classPath = sys.argv[2]
    logPath = sys.argv[3]
    limit = sys.argv[4]

if not os.path.exists(logPath):
    os.makedirs(logPath)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image_faces = []
count=0
idface=0
recognizer = cv2.face.createLBPHFaceRecognizer()
video_capture = cv2.VideoCapture(vidPath)
frameRate = video_capture.get(5)
recognizer.load(classPath)
while(video_capture.isOpened()):
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    numberframe = video_capture.get(1)
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=2,
            minNeighbors=5,
            flags=cv2.CASCADE_SCALE_IMAGE,
            minSize=(30, 30)
        )
    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	    #image_faces.append(image[y:(y+h), x:(x+w)])
            #cv2.imwrite("face-" + str(count) + ".jpg", frame[y:(y+h), x:(x+w)])
	    image_faces.append(frame[y:(y+h), x:(x+w)])
            gray = cv2.cvtColor( frame[y:(y+h), x:(x+w)], cv2.COLOR_BGR2GRAY )
	    nbr_predicted, conf = recognizer.predict(gray)
	    #nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
	    #print "{} is recognized with {}".format(nbr_predicted, conf)
	    #cv2.imshow("Recognising Face", gray)
	    if idface != nbr_predicted and idface != 0 and conf<limit:
                string="At "+str(round((numberframe/frameRate),2))+" seconds"+" Subject: "+str(nbr_predicted)+" Confidence:"+str(conf)+"\n"
                with open(logPath+"/"+"Logfaces.txt", "a") as myfile:
                    myfile.write(string)
                cv2.imwrite(logPath+"/"+str(round((numberframe/frameRate),2)) +"sec-id"+ str(nbr_predicted) + ".jpg", frame[y:(y+h), x:(x+w)])
	    if conf<limit and idface==0:
                string="At "+str(round((numberframe/frameRate),2))+" seconds"+" Subject: "+str(nbr_predicted)+" Confidence:"+str(conf)+"\n"
                with open(logPath+"/"+"Logfaces.txt", "a") as myfile:
                    myfile.write(string)
                cv2.imwrite(logPath+"/"+str(round((numberframe/frameRate),2)) +"sec-id"+ str(nbr_predicted) + ".jpg", frame[y:(y+h), x:(x+w)])

	    if conf<limit:
	        idface=nbr_predicted
    else:  
        video_capture.release()
        cv2.destroyAllWindows()
    # Display the resulting frame

#python recognizefaces.py facesample.mp4 Data.xml logvid 100

