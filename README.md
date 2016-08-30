# robotics-camera

Step 1: Connect the camera to the pi

Step 2: Enable the camera via raspi-config:

$ sudo raspi-config 
Select Camera -> Enable 
Reboot

Step 3: Install the pycamera libraries for python
sudo apt-get install python-picamera

Step 4: Test that the camera is working via command line

$ sudo raspistill -o "myimage.jpg"

The above command should capture an image and place it in your working directory

Step 5: install opencv for python (this will help with doing any image processing with pictures or video streams)
$ sudo apt-get install libopencv-dev python-opencv


