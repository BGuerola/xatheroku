from flask import Flask, request

app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method== "POST":
        return'<h1>Esto es una petición POST</h1>'
    else: 
        return '<h1> Hola mundo<h1>'

@app.route('/otra-ruta')
def otraRuta():
    return '<h1> Hola again<h1>'

if __name__ =="__main__":
    app.run(host ='0.0.0.0', port=4000, debug= True)
