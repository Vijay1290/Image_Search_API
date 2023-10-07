from flask import Flask, render_template, redirect, request, flash, session
from email import message
from urllib import request
from flask import Flask, render_template
from flask import Flask, redirect, url_for, render_template, request
import requests

app = Flask(__name__)

app.config["SESSION_TYPE"] = "memcached"
app.config["SECRET_KEY"] = "super secret key"

PIXABAY_API_KEY = '37689083-25cb317453531dcfb805d697d'
PIXABAY_API_URL = 'https://pixabay.com/api/'

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        image = request.form.get('image')

        params = {
            'key': PIXABAY_API_KEY,
            'q': image,
            'image_type': 'photo',
            'per_page': 100
        }

        response = requests.get(PIXABAY_API_URL, params=params)
        data = response.json()

        if data.get('hits'):
            images = data['hits']
            num_images = len(images)
            return render_template('index.html', num_images=num_images, images=images)
        else:
            return render_template('index.html', error='No images found')
    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
