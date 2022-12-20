import os
import subprocess
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, send_file, redirect, url_for, jsonify, abort, \
    send_from_directory
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL

templates_folder = 'theme_folder'
static_ = 'theme_static'
app = Flask(__name__, template_folder=templates_folder, static_folder=static_)
upload_dir = os.path.join(app.instance_path, 'uploads')
result_dir = os.path.join(app.root_path, 'output')
# set up mysql Database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'athris123'
app.config['MYSQL_DB'] = 'new_db'

mysql = MySQL(app)
ALLOWED_EXTENSIONS = {'mov', 'mp4', 'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(upload_dir, exist_ok=True)  # upload directory

weights = ['yolov5n', 'yolov5s', 'yolov5m', 'yolov5l']


@app.route('/')
def index():
    title = "face mask detection System"
    return render_template("index.html")


@app.route("/opencam", methods=['POST'])  # function to run live camera
def opencam():
    if request.method == 'POST':
        model = request.form['model']
        source = request.form['source']

        path = 'runs/custom/'
        # subprocess.run("ls")
        subprocess.run(['python', 'detect.py', '--weights', path + 'best_' + model + '.pt', '--source', source],
                       shell=True)
        print(path, 'best_' + model + '.pt')

        return render_template("index.html")


def allowed_file(filename):  # function to allow types of files that zcan be uploaded
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_DB', methods=['POST'])  # UPLOAD RESULTS TO DATABASE
def upload_file():
    now = datetime.now()

    file = request.files['image_db']
    data = file.read()
    directory = os.path.join(result_dir, secure_filename(file.filename))
    if os.path.exists(directory):
        if file and allowed_file(file.filename):
            file.save(directory)
            filename = secure_filename(file.filename)

            # Creating a connection cursor
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO upload VALUES(NULL,%s,%s,%s)''', (filename, now, data))
            mysql.connection.commit()
            cursor.close()
            return f"Succesfully uploaded to database"
    else:
        return f"Results returns with error"

        # show directory contents


@app.route("/detect", methods=['POST'])  # function uploading files images
def detect():
    now = datetime.now()
    file = request.files['file']
    model = request.form['model']
    path = 'runs/custom/'
    print("Using " + model)

    if file.filename == '':
        return "No file selected"

    if file and allowed_file(file.filename):
        file.save(os.path.join(upload_dir, secure_filename(file.filename)))

        subprocess.run(['python', 'detect.py', '--weights', path + 'best_' + model + '.pt', '--source',
                        os.path.join(upload_dir, secure_filename(file.filename))], shell=True)
        # return as an object of file name to data ajax

        return 'Results saved in OUTPUT '
    else:
        return 'Invalid format of file'


if__name__ = '__main__'
app.config['SECRET_KEY'] = 'athris'
os.environ['FLASK_DEBUG'] = 'development'
app.run(debug=True)
