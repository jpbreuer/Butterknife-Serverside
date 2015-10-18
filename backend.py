from flask import Flask, request
import lyrics
import translator
import imgur
import wikipedia

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTTENSIONS = ['png', 'jpeg', 'gif', 'jpg']

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

@app.route("/api/lyrics/<songname>")
def get_lyrics_song_name(songname):
    return lyrics.get_lyrics(songname)

@app.route("/api/lyrics/<artist>/<songname>")
def get_lyrics_song_name_artist(artist, songname):
    return lyrics.get_lyrics_artist(artist, songname)

@app.route("/api/translator/<to_language>/<text>")
def get_translated_text(to_language, text):
    return translator.translate(text, to_language)

@app.route("/api/imgur/")
def get_imgur_link(image):
    pass

@app.route("/api/wikipedia/<text>")
def get_wikipedia_page(text):
    return wikipedia.wikipediasearch(text)

if __name__ == "__main__":
    app.run(host='0.0.0.0')


