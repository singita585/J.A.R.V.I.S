#Import that is needed
import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video FrameWidth

detector = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
#Haar Cascade classifier is an effective object detection approach

face_id = input("Enter a Numeric user ID  here:  ")
#Use integer ID for every new face (0,1,2,3,4,5,6,7,8,9........)

print("Taking samples, look at the camera ......")
count = 0 # Initializing sampling face count

while True:
    # This section of code is to read the frames 
    # using the above created object and convert an input image from one color space to another
    ret, img = cam.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGRGRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        #this section of code is used to draw 
        #a rectangle on any image
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        #This section is to capture and save images into the datasets folder
        cv2.imwrite("samples/face." + str(face_id) + "." + str(count) + ".jpg", converted_image[y:y+h, x:x+w])

        #Used to display an image in a window
        cv2.imshow("image", img)
    #Waits for a pressed key
    k = cv2.waitKey(100) & 0xff

    #Press "ESC" to stop
    if k == 27:
        break
        #Take 50 sample (More sample --> More accuracy)
    elif count >= 10:
        break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()