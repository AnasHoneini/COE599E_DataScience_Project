from flask import Flask
from flask import render_template, request
import boundaryDetection
import extractInfo
import cv2
import numpy as np



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == "POST":
        # get the uploaded image file
        file = request.files['image']
        file.save('static/profile.jpeg')
        img= cv2.imread('static/profile.jpeg')
      
        ID = boundaryDetection.boundImage(img)
        #cv2.imshow("sa",ID)
        #cv2.waitKey()
        extractInfo.extractImage(ID)
        IDNumber= extractInfo.extractIDNumber(ID)
        if len(IDNumber) == 0:
            print("The IDNumber list is empty.")
        else:
            IDNumber_array = np.array(IDNumber)

            # Convert the array to a string representation
            IDNumber_str = np.array2string(IDNumber_array, separator=', ')
        #proccess it in google collab
        # put the details in a list called name
        
    return render_template("main.html",IDNumber_str=IDNumber_str)


if __name__ == '__main__':
    app.run(debug=True)
