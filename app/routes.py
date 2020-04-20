from app import app
from flask import Flask, request, jsonify, redirect
import io
from pydub import AudioSegment
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from config import config

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
    

@app.route('/check_connexion')
def connexion_test():
    return jsonify({'status': "OK"})
    

@app.route('/find_sound', methods=['POST', 'GET'])
def recognize_song():
    print("=" * 50)
    print("List uploaded files: {}".format(request.files.getlist('uploaded_file')))
    print("=" * 50)
    files = request.files.getlist('uploaded_file')

    artist = ""
    title = ""

    if files and len(files) > 0:
        print("\t Reading song uploaded ...")        
        # Read song from parameters -> download it as mp3 file    
        b = io.BytesIO(files[0].read())
        song = AudioSegment.from_file(b, format="3gp")
        song.export("temp/test.mp3", format="mp3")

        print("\t File song read\n\t Song recognition started...")        
        # create a Dejavu instance
        djv = Dejavu(config)

        # Recognize audio from a file
        song_found = djv.recognize(FileRecognizer, "temp/test.mp3")

        print("\tSong recognition finished")        

        if song_found: 
            song_name = song_found.get('song_name').split("--")
            artist = song_name[0]
            title = song_name[1]

    print("\tReturnin response")        
    return jsonify({
        'artist': artist,
        'title': title
        })