import cv2
import urllib.request
import joblib 
from bound import find_bounding_box
import sklearn
import os

# Load the saved model
svc = joblib.load('./models/best_model_knn.pkl')
knn = joblib.load('./models/best_model_svc.pkl')
mlp = joblib.load('./models/best_model_mlp.pkl')


#FACE DETECTION 
#AUTOMATIC

def extractImage(id_image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(id_image, cv2.COLOR_BGR2GRAY)
    profile_img=[]
    # Download the face detection model
    url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/lbpcascades/lbpcascade_frontalface.xml'
    filename = './models/lbpcascade_frontalface.xml'
    urllib.request.urlretrieve(url, filename)

    # Load the face detection model
    face_cascade = cv2.CascadeClassifier(filename)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image)

    # Get the coordinates of the face bounding box
    for (x, y, w, h) in faces:
        profile_img = id_image[y:y+h, x:x+w]

    image_path = './static/profile.jpg'

    # Display the profile picture
    if os.path.exists(image_path):
    # Remove the existing file
        os.remove(image_path)

    # Save the image using cv2.imwrite()
    cv2.imwrite(image_path, profile_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop_nb(img,Thresh):

  # Upscale the image to double its size using bicubic interpolation
  img = cv2.resize(img,(img.shape[1]*4, img.shape[0]*4))
  
  # Get the dimensions of the image
  height, width, channels = img.shape

  # Set the crop box dimensions
  left = int(width * 0.5)
  top = int(height * 0.8)
  right = int(width*0.93)
  bottom = int(height*0.9)  # 25% of the bottom


  #  Crop the image
  cropped_img = img[top:bottom, left:right]
  img = cv2.threshold(cropped_img, Thresh, 255, cv2.THRESH_BINARY)[1] #change here
  return img



def extractIDNumber(img):
    img2=[]

    ThreshSet = False
    Thresh = 60
    id = []
    while ThreshSet== False and Thresh<255 :
        try:
            print(Thresh)
            img2 = crop_nb(img,Thresh)
            #cv2_imshow(img)
            char,padd = find_bounding_box(img2)
            if len(padd) == 12:
                ThreshSet= True
                for i in padd:
                    resized =  cv2.resize(i, (28, 28))
                    x = [resized.flatten(),]
                    print(knn.predict(x),
                        svc.predict(x),mlp.predict(x))
                    id.append(svc.predict(x))
            else:
                Thresh+=5
        except: 
            Thresh+= 5
    return id

