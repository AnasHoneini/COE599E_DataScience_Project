from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    name = ["anas","honeini"]

    if request.method == "POST":
        # get the uploaded image file
        file = request.files['image']
        print(file)
        return "File uploaded successfully"
        #proccess it in google collab
        # put the details in a list called name
        
    return render_template("main.html",name=name)


if __name__ == '__main__':
    app.run(debug=True)
