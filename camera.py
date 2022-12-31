import cv2
  
# define a video capture object
vid = cv2.VideoCapture(0)
i=20
c=0
while(True):
    c+=1
    
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    roi=frame[100:500, 100:500]
    cv2.rectangle(frame,(90,90),(500,500),(0,255,0),0)    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    #take image from the rectangle 
    cv2.imshow('roi', roi)
    #take a photo every 2 seconds and save it
    print(c)
    if c%100==0:
        i=i+1
        #save the image
        cv2.imwrite("hand"+str(i)+".jpg", roi)
        #convert int to string
        #i=str(i)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()