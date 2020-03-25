from flask import Flask, render_template, request, flash
exec(open("roverdriver.py").read())

takePicture('./static/currentView.jpg')

app = Flask(__name__)
app.secret_key = 'uieorwhcjdqwouiersdhdfsjk'
@app.route('/', methods = ['GET','POST'])

def controlRequest():
    if request.method == 'POST':
        camangle = request.form['camangle']
        getToAngle(camangle)
        takePicture('./static/currentView.jpg')
        wheelangle = request.form['wheelangle']
        move = request.form['move']
        message = "angle caméra de " + camangle
        flash(message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
