from flask import Flask, render_template

app = Flask(__name__)

# e.g.) https://www.naver.com/
# http://localhost:5000/

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/checkform")
def checkform():
    return render_template("checkform.html")

if __name__ == '__main__':
    app.run(debug = True)