import cv2
import numpy as np

video = cv2.VideoCapture("vid.mp4") 
image = cv2.imread("earth.jpg")

while True:
    ret, frame = video.read() # any error in retreiving video ret becomes false and while loop exit,else store in frame
    frame = cv2.resize(frame, (640, 480)) # resizing frame,vid
    image = cv2.resize(image, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # converting rgb to hue saturtn val(hsv) the frame to the hsv val
    l_g = np.array([32, 94, 132]) # lower green value of in frame
    u_g = np.array([179, 255, 255]) # create a mask so that obj detectn in border will identigy obj
    mask = cv2.inRange(hsv, l_g, u_g) #mask is created to cover green values i.e range of hsv vals
    res = cv2.bitwise_and(frame, frame, mask=mask) # do AND between frame,mask to get res,identified screen and rempoved obj
    f = frame-res # to delete green screen and only obj shuld be there
    green_screen = np.where(f == 0, image, f) # now wherever obj is black , replace by img where f=0,replace by img
    cv2.imshow("final-out", green_screen)# display finally 
    #cv2.imshow("Frame",frame) # display the frame(video stored)
    k=cv2.waitKey(1) # wait time for us to enter a particular key , that will be stored in k in unicode format
     #cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("RES", res)
    if k==ord('q'):  # q in unicode format if user presses q , then quit
        break

video.release()  # release all used resources
cv2.destroyAllWindows() # destroy video frame