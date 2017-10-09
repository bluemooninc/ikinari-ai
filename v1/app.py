# coding: utf-8
from flask import Flask, render_template
import glob, os
import datetime

app = Flask(__name__)

@app.route('/')

def index():
    data = []
    pathname = '/home/pi/ikinari-ai/static/img/*.jpg'
    images = sorted(glob.glob(pathname), key=os.path.getmtime, reverse=True)
    for i in range(len(images)):
        if i>10:
            break
        stat = os.stat(images[i])
        last_modified = stat.st_mtime
        print(last_modified)
        dt = datetime.datetime.fromtimestamp(last_modified)
        dtstr = dt.strftime("%Y-%m-%d %H:%M:%S") 
        if os.path.exists(images[i]+'.txt'):
            f = open(images[i]+'.txt')
            text = f.read()
            f.close()
        else:
            text = 'No Title'
        text = dtstr + ' ' + text
        fname = 'img/'+os.path.basename(images[i])
        data.append({'text':text, 'fname':fname}) 
    return render_template('index.html', images=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

