from flask import Flask, render_template, request
import pickle
import numpy as np
model = pickle.load(open('insurance.pkl', 'rb'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def newpage():
    return render_template('main.html')

@app.route('/recommend',methods=['POST'])
def helloworld():
    return render_template('index.html')

@app.route('/insurance_predict',methods=['POST'])
def insurance():
    age=request.form['age']
    gender=request.form['Gender']
    bmi=request.form['bmi']
    children=request.form['children']
    smoker=request.form['smoker']
    


    arr = np.array([[age,gender,bmi,children,smoker]])

    pred = model.predict(arr)

    return render_template('insurance_predict.html', data=pred)



if __name__=='__main__':
    app.run(port=3000,debug=True)