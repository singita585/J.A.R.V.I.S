#The import that is needed for face recognition
import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) # this code initialize the haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

#number of persons you want to Recognize
id = 2 

names = ['','avi']  #For the names first we leave them empty, reason for this is beacause the counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

#These codes is used to define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
   #This block of code is used to read the frames using the above created object
   # And  convert an input image from one color space to another
    ret, img =cam.read() 

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #code here is used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) # this code here is used to predict on every single image

        # This block of code checks if accuracy is less than 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

# Press 'ESC' for exiting video
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()