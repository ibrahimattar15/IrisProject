from flask import Flask,request,render_template,jsonify
from utils import IrisFlowerSpecies
from config import PORT_NO
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/iris/species/prediction',methods = ['GET','POST'])
def prediction():
    if request.method=='POST':
        data = request.form.get
        SepalLenghtCm = eval(data('SepalLenghtCm'))
        SepalWidthCm = eval(data('SepalWidthCm'))
        PetalLenghtCm = eval(data('PetalLenghtCm'))
        PetalWidthCm = eval(data('PetalWidthCm'))
        model_pred = IrisFlowerSpecies(SepalLenghtCm,SepalWidthCm, PetalLenghtCm, PetalWidthCm)
        model_result = model_pred.predict_species()
        return render_template('index.html',Prediction = model_result)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=PORT_NO,debug=True)
