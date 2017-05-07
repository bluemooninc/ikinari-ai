# coding: utf-8
from flask import Flask, render_template
import glob, os

app = Flask(__name__)

@app.route('/')

def index():
    data = []
    pathname = '/home/pi/ikinari-ai/static/img/*.jpg'
    images = sorted(glob.glob(pathname), key=os.path.getmtime)
    for i in range(len(images)):
        if i>10:
            break
        f = open(images[i]+'.txt')
        text = f.read()
        f.close()
        fname = 'img/'+os.path.basename(images[i])
        data.append({'text':text, 'fname':fname}) 
    return render_template('index.html', images=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

