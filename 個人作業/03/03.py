from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)

@app.route('/info/')
def info(name=None):
    return render_template('info.html')


if __name__ =="__main__":
    app.run()