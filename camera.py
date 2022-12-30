import cv2
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    roi=frame[100:300, 100:300]
        
        
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    #take image from the rectangle 
    cv2.imshow('roi', roi)
    i=0
    while(1):
    #wait 2 seconds
        cv2.waitKey(2000)
        cv2.imwrite("Hand"+str(i)+".png", roi)
        #convert int to string
        #i=str(i)
        i=i+1

    
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()