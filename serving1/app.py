from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn import datasets
from keras.models import load_model
import tensorflow as tf

app = Flask(__name__)

global model
global graph
global target_names

model = load_model('iris_model.h5')
graph = tf.get_default_graph()
target_names = datasets.load_iris().target_names

# e.g.) https://www.naver.com/
# http://localhost:5000/

@app.route("/")
def index():
    #return "index"
    return render_template('index.html')

@app.route("/checkform") # default 값이 get
def checkform():
    return render_template("checkform.html")

@app.route("/check", methods = ['POST']) # host 방식일 때는 메서드를 정해주어야 함
def check():
    sepal_length = request.form['sepal_length']
    sepal_width = request.form['sepal_width']
    petal_length = request.form['petal_length']
    petal_width = request.form['petal_width']
    features = [sepal_length, sepal_width, petal_length, petal_width]
    print("sepal_length:", sepal_length)
    print("sepal_width:", sepal_width)
    print("petal_length:", petal_length)
    print("petal_width:", petal_width)
    print("features:", features)

    features = np.reshape(features, (1, 4))
    with graph.as_default():
        y_pred = model.predict_classes(features)
    idx = y_pred[0]
    spicies = target_names[idx]
    print({'species': spicies})
    return jsonify({'species': spicies})

if __name__ == '__main__':
    app.run(debug = True)