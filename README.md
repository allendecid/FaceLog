# FaceLog
Face Detection, Recognition and Logging with OpenCV and Python.
FaceLog lets you build a database of faces from videos, train classifiers based on those datasets, recognize faces from new videos and then log those faces and detections with image files and record entries.

# Requirements
Tu run the program you will need to have Python 2.7 or higher installed, and OpenCV with [OpenCV's extra modules](https://github.com/opencv/opencv_contrib). The easiest way is to [install them through homebrew](http://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/), but there is also other alternatives for [Windows](https://putuyuwono.wordpress.com/2015/04/23/building-and-installing-opencv-3-0-on-windows-7-64-bit/) and [Linux](http://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html).


```

Easy OpenCV with extra mudoles install
brew install opencv3 --with-contrib

Numpy
pip install numpy

Pillow
pip install Pillow


```

To run the command you will have to go to the location of the FaceLog folder that has the python code or reference the location. You can also execute the zip file by running "python FaceLog.zip" instead of "python FaceLog".

# Building a face Dataset
For this step it detects faces from a sample video (used for training and to get face templates) using the Haar Cascade provided by OpenCV ("haarcascade_frontalface_default.xml"). After it detects the faces it extracts the image from the video and saves it in a folder. You can set some parameters to select the location of the folder and to set the window (in seconds) from one individual face from another in the video. To create a face database you can run the following commands.

```
python FaceLog -c facesample.mp4 #Creates the database from facesample.mp4

You can also change the default parameters

python FaceLog -c facesample.mp4 0 subjects

-c: indicates you are creating a dataset
videosample.mp4 is the video used for the database
0 is the window (seconds) from one subject to another
testsubjects is the folder where the faces will be saved

```


# Creating a LBPH Face Recognizer 

After the faces have been extracted from the videos, manual filtering and ordering is required on the images, in order to check that all the images are indeed faces and to tag each series of pictures with a subject. The images will be names face-1.154.jpg face-2.21 etc. The first part of the name indicates the subject (face-1, face-2)(subject one and two) and the second part indicates the framenumber (154,21). After the faces from the video have been taken you wil need to tag all the pictures with the subject id (face-1, face-2, face-3...).

After the faces have been tagged and order you can create a LBPH Face Recognizer with the following command:

```
python FaceLog -t

You can also change the default parameters

python FaceLog -t subjects Data.xml

subjects: is the folder where the tagged faces are
Data.xml: is the name of the recognizer

```

# Recognizing and keeping record of the faces 

After the face dataset has been created and the recognizer trained you can start creating records of faces from video files.
To recognize faces and to log them run the following command:


```
python FaceLog -r facesample.mp4

You can also change the default parameters

python FaceLog -r facesample.mp4 Data.xml logvid 100

Data.xml: is the name of the recognizer
logvid: is the folder where the log and the pictures will be saved
100: is the confidence threshold (to filter unknown faces)

```
The results will be placed in a folder with a Logfaces.txt file indicating the faces that where recognized, the time they where recognized and the confidence. Images will also be taken in the following format: 3.34sec-id1.jpg meaning it was taken on the second 3.34, with th subject id 1.



