<<<<<<< HEAD
# Capturing images with Picamera, trasnforming images to HSV color space
# and dislaying them with opencv
=======
# Capturing images with Picamera and dislaying them with opencv
>>>>>>> 9a30c61099447548eacb8741b33638d71159cf01
import cv2
import picamera
import picamera.array
import time
<<<<<<< HEAD

myfile = open('my_image.jpg','wb')

with picamera.PiCamera() as camera:
    camera.resolution=(640,480)
    camera.framerate = 32
    #camera.start_preview()
    time.sleep(2)
    #capture to file with resizing
    camera.capture(myfile, resize= (320,240))
    myfile.close()
    #camera.stop_preview()

    with picamera.array.PiRGBArray(camera, size=(640,480)) as stream:
        
        #capture to stream for use with opencv
        camera.capture(stream, format='bgr')
        image = stream.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        print "display hsv image"
        #display the image on screen and wait for a key press
        cv2.imshow('Image', hsv)
        # save the transformed image to file
        cv2.imwrite('hsvimage.jpg', hsv)
        cv2.waitKey(0)

    

   
=======

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        while True:
            camera.capture(stream, format='bgr')
            image = stream.array
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # reset the stream before the next capture
            stream.seek(0)
            stream.truncate()
        cv2.destroyAllWindows()
>>>>>>> 9a30c61099447548eacb8741b33638d71159cf01
