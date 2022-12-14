
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def play(x=3, color="#00FFFF"):
    return render_template('index.html', num=x, color=color)





if __name__ == "__main__":
    app.run(debug=True)