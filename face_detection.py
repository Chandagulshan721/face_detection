
import cv2

# Load Haar Cascade
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + alg)

# Read the Image
image_path = "human_face.jpg"
img = cv2.imread(image_path)

if img is None:
    print("Error: Unable to load image.")
else:
    # Convert to Grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    faces = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

    # Draw Rectangles Around Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the Image
    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()












    


"""import sys
print("Python Version:", sys.version)
print("Python Executable:", sys.executable)

import cv2
print("OpenCV Version:", cv2.__version__)"""



"""import cv2
alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)

video_path="human face.jpg"
img= cv2.imread(video_path)

while True:
    _, img = cam.read()
    grayImg = cv2.Cascade(img,cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayImg,1.3,4)

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("FaceDetection",img)

    key = cv2.waitkey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()"""




