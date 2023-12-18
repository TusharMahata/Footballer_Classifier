from flask import Flask, request, send_from_directory, render_template, url_for, jsonify
import util
import cv2 as cv
#from werkzeug import secure_filename, FileStorage
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from flask_wtf import FlaskForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'tushar'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

class UploadFrom(FlaskForm):
    photo = FileField(
        validators = [
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')

        ]

    )
    submit = SubmitField('Classify')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods = ['GET', 'POST'])
def classify_image():

    form = UploadFrom()
    if form.validate_on_submit():
        #file_url = r'C:\Users\DCL\Footballer Recognizer\Server\uploads\me.jpg'
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        #cv.imshow('img', filename)
    else:
        file_url = None
    #image_data = request.form['image_data']
    result = None

    if file_url != None:
        path = r'C:\Users\DCL\Footballer Recognizer\Server'
        img_path = path + file_url
        util.load_saved_artifacts()



        result = util.classify_image(None, img_path)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    #print(response)

    return render_template('app.html',form=form, file_url=file_url, result=result)
    #return "Tushar :-) "


if __name__=='__main__':
    #print('Starting Python Flask Server For Footballer Classification')
    util.load_saved_artifacts()
    #classify_image()
    #path = r'C:\Users\DCL\Footballer Recognizer\Server\test_imgs\mussial.jpg'
    #print(util.classify_image(None, path))

    app.run(port:5000)