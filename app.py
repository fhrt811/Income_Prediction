from flask import Flask, render_template, jsonify, request

app=Flask(__name__)

app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def prediction():
    if request.method=='GET':
        return render_template('form.html')
    else:
        data = CustomData(
            age
        )