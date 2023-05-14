from flask import Flask
from flask import render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

@app.route('/home')
def home():
    if request.method == "POST":
        # get the uploaded image file

        return "Image uploaded successfully!"
        
    return render_template("main.html")






