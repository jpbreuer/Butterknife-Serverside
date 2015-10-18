from flask import Flask
import requests
import urllib

__author__ = 'Laura'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTTENSIONS = set(['png', 'jpeg', 'gif', 'jpg'])

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))