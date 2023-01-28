from flask import Flask,request,jsonify
import re
app = Flask(__name__)

@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/otro')
def say_hello():
  return 'Hello from Server'
  

@app.route('/ordenamiento', methods=['POST'])
def ordenamiento():
  try:
    print(request.get_json())
    data = request.get_json()
    numeros = data['numeros']
    print(numeros)
    numerosOrdenados = sorted(numeros)
    return jsonify({
    "inicial": numeros,
    "ordenados": numerosOrdenados}), 200
  except ValueError as err:
    return jsonify(err.message), 404
    


# Buscando utilizando expresiones regulares
@app.route('/file', methods=['POST'])
def mayusFile(): 
  print("hola")
  file = request.files['file']
  textfile = file.read()
  content = str(textfile, 'utf-8')
  countTitle = len(re.findall(r'[A-Z]',file.filename))
  countText = len(re.findall(r'[A-Z]',content))
  
  return jsonify({
      "cantida de mayus dentro del txt": countText,
     "cantida de mayus en el titulo del archivo": countTitle
  }), 200