from flask import Flask,render_template,jsonify,request,make_response,send_from_directory,abort
import os
import re
import datetime
import random
from main import plant_id

def create_uuid():
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    randomNum = random.randint(0,100)

    uniqueNum = str(nowTime) + str(randomNum)
    return uniqueNum

app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
ALLOWD_EXTENSIONS = set(['png','jpg','JPG','PNG','gif','GIF','jpeg','JEPG'])


def allowd_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWD_EXTENSIONS

@app.route('/')
def upload_test():
    return render_template('index.html')

@app.route('/up_photo',methods=['POST'],strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir,app.config['UPLOAD_FOLDER'])
    print(file_dir)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']

    if f and allowd_file(f.filename):
        new_filename = create_uuid()
        f.save(os.path.join(file_dir,new_filename+'.png'))

    image_path_1 =  os.path.join(file_dir,new_filename+'.png')
    return plant_id(image_path_1)
if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)
