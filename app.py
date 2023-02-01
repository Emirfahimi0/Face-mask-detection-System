#IMPORT LIBRARIES
import os
import subprocess
from datetime import datetime
import torch
from Detection import ObjectDetection
from matplotlib import pyplot as plt
import sys
import io
from io import BytesIO
import base64
from PIL import Image
sys.path.insert( 0 ,'./yolov5-master')
import torch.backends.cudnn as cudnn

from flask import Flask, render_template, request, abort, \
    send_from_directory



templates_folder = 'templates'
static_ = 'static'
app = Flask(__name__, template_folder=templates_folder, static_folder=static_)
upload_dir = os.path.join(app.instance_path, 'uploads')
result_dir = os.path.join(app.root_path, 'output')



ALLOWED_EXTENSIONS = {'mov', 'mp4', 'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(upload_dir, exist_ok=True)  # upload directory

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"




@app.route('/')
def index():
    title = "face mask detection System"
    return render_template("index.html")


def loadTorchHub(url_link, model, source):

    custom_model = url_link+'best_'+model+'.PT'
    print('best_'+model+'.pt')
    # Create a new object and execute.
    
    detection =ObjectDetection (capture_index=source, model_name=custom_model)
    detection()
 


@app.route("/opencam", methods=['POST'])  # function to run live camera
def opencam():
    if request.method == 'POST':
        model = request.form['model']
        source = request.form['source']
        load = request.form['load']
        path = 'static/custom/'
        if load == 'Torch':
            loadTorchHub(path, model, source)
            return "Evoke camera with OpenCV"
        
        elif load =='local':
        # subprocess.run("ls")
            print(path, 'best_' + model + '.pt')
            subprocess.run(['python', 'detect.py', '--weights', path + 'best_' + model + '.pt', '--source', source],shell=True)
           
            return "Evoked Cam"
    


def allowed_file(filename):  # function to allow types of files that zcan be uploaded
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





@app.route("/detect", methods=['POST'])  # function uploading files images
def detect():

    DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"
    now = datetime.now().strftime(DATETIME_FORMAT)
    file = request.files['file']
    model = request.form['model']
     
    print("Using " + model + ".PT")
    custom_model = 'static/custom/best_'+model+'.pt'
    if file.filename == '':
        return "No file selected"

    if file and allowed_file(file.filename):

         #get_file = os.path.join(upload_dir, secure_filename(file.filename))
         #file.save(get_file)
        #Load model from torch hub
         model = torch.hub.load('ultralytics/yolov5', 'custom', path=custom_model, force_reload=True)
         img_bytes = file.read()   
         img = Image.open(io.BytesIO(img_bytes))
         results = model([img])
         im =  results.ims
         results.render()
         results.show()
         img_savename = f"static/output/{now}.JPEG"
         #img_base64.save(save_dir=img_savename)    
         img_base64 = Image.fromarray(im[0]).save(img_savename)
        
    
         for img_results in results.ims:
          buffered = BytesIO()
        

          with open(img_savename,"rb") as result_file:

            BinaryData = result_file.read()

    
         # print(base64.b64encode(buffered.getvalue()).decode('utf-8')) # base64 encoded image with results

            

        #subprocess.run(['python', 'detect.py', '--weights', path + 'best_' + model + '.pt', '--source',
         #               get_file], shell=True)
         
        # return as an object of file name to data ajax
    object = img_savename
    return object








if__name__ = '__main__'
app.config['SECRET_KEY'] = 'athris'
#os.environ['FLASK_DEBUG'] = 'development'
app.run()
