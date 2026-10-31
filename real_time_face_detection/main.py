import cv2
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
classifier = cv2.CascadeClassifier(cascade_path)
camera = cv2.VideoCapture(0)
status = camera.isOpened()    
while status == True:    
    success, frame = camera.read()
    if success == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(gray)
        faces_count = len(faces)
        for x,y,w,h in faces:
            color = (0,255,0)
            thickness = 2
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,thickness)
        cv2.putText(frame,f"Faces Detected: {faces_count}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.imshow("My Webcam",frame)
        stop = cv2.waitKey(1)   
        if stop == ord('q'):
            break
    else:
        print("An error occured while opening camera.")
camera.release()
cv2.destroyAllWindows()

