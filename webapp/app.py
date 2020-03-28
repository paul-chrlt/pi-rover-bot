from flask import Flask, render_template, request, flash
import random
exec(open("roverdriver.py").read())

takePicture('./static/currentView.jpg')
currentViewPlace = './static/currentView.jpg?'+str(random.getrandbits(111))

app = Flask(__name__)
app.secret_key = 'uieorwhcjdqwouiersdhdfsjk'
@app.route('/', methods = ['GET','POST'])

def controlRequest():
    if request.method == 'POST':
        camangle = request.form['camangle']
        getToAngle(camangle)
        takePicture('./static/currentView.jpg')
        wheelangle = request.form['wheelangle']
        getToDirection(wheelangle)
        move = request.form['move']
        moveTo(move)
        #message = "angle caméra de " + camangle
        #flash(message)
    return render_template('index.html',currentViewPlace = './static/currentView.jpg?'+str(random.getrandbits(111)))

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
