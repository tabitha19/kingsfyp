import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
from werkzeug.utils import secure_filename
from dataProcessing import *
from Threading import *
from flask import send_file
import time
script = ''
UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['txt']) #only .txt files allowed

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER #files uploaded will be stored in the UPLOAD_FOLDER

def resultE():
    return render_template('KeyResult.html') #rendering html files

def resultD():
    return render_template('DecryptResult.html')

@app.route('/encrypt/')
def EncryptInput(): #function to encrypt
  st = time.time()
  Segment() #dividing file into N parts
  getInfo() #get info of the N parts
  HybridCrypt() #encrypt with threads
  et = time.time()
  print("encryption time is ")
  print(et-st)
  return resultE()

@app.route('/decrypt/')
def DecryptMessage(): #function to decrypt
  st=time.time()
  HybridDeCrypt()# decrypt threading
  trim() #trim the N decrypted files
  Merge() #merge the N decrypted files
  et=time.time()
  print("decryption time is ")
  print(et - st)
  return resultD()

def start():
  content = open('SecureKey.txt', 'r')
  content.seek(0)
  first_char = content.read(1) 
  if not first_char:
    return render_template('Empty.html')
  else:
    return render_template('Process.html')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/process')
def process():
  return render_template('index.html')



def allowed_file(filename): #only .txt files allowed
  return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/return-files-key/')
def return_files_key():#return secure key
  try:
    return send_file('SecureKey.txt', attachment_filename='SecureKey.txt', as_attachment=True)
  except Exception as e:
    return str(e)

@app.route('/return-files-data/')
def return_files_data(): #return decrypted file
  try:
    return send_file('./Output.txt',attachment_filename='Output.txt',as_attachment=True)
  except Exception as e:
    return str(e)


@app.route('/data/', methods=['GET', 'POST'])
def upload_file(): #upload a file
  if request.method == 'POST':
    if 'file' not in request.files: #check if file not uploaded
      return render_template('Nofile.html')
    file = request.files['file']
    if file.filename == '':
      return render_template('Nofile.html') #check if file is empty
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'SecureKey.txt'))
      return start()
       
    return render_template('Invalidformat.html') #else invalid

@app.route('/learn')
def learn():
  return render_template('LearnMore.html')
    
if __name__ == '__main__':
  app.run(debug=True)
