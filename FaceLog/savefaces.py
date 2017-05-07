#!/usr/bin/env python
import cv2
import sys
import os

length=len(sys.argv)
if length < 2:
    sys.exit('\nAt least one argument required')
#print (' '.join(sys.argv[2:]));
if length < 3:
    videoPath = sys.argv[1]
    rate = 0
    dir = "subjects"
else:
    videoPath = sys.argv[1]
    rate = int(sys.argv[2])
    dir = sys.argv[3]

if not os.path.exists(dir):
    os.makedirs(dir)

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image_faces = []
count=0
startframe=0
subject=1
control=0
#dir="subjects"

video_capture = cv2.VideoCapture(videoPath)
frameRate = video_capture.get(5)
window = frameRate*rate

while(video_capture.isOpened()):
    frameId = video_capture.get(1)
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=2,
        minNeighbors=5,
        flags=cv2.CASCADE_SCALE_IMAGE,
        minSize=(30, 30)
        #maxSize
        #flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	#image_faces.append(image[y:(y+h), x:(x+w)])
        cv2.imwrite(dir +"/face-" + str(subject) +"." + str(count) + ".jpg", frame[y:(y+h), x:(x+w)])
	count +=1
	startframe = video_capture.get(1)
    if frameId >= (startframe+window) and control==0:
        subject +=1
        control =1
        count =0
        print "subject" + str(subject)
       

    if frameId < (startframe+window):
        control =0

    # Display the resulting frame
    #cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

#python savefaces.py haarcascade_frontalface_default.xml
#python savefaces.py video.mp4 3 testsubjects
