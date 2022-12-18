from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils import Titanic

app = Flask(__name__)

@app.route('/')
def home():
    print("Going To Home Page...!")
    return render_template("home.html")

@app.route('/titanic', methods = ['GET','POST'])
def get_predict_titanic():
    if request.method == 'GET':

        Area               = eval(request.args.get('Area'))
        MajorAxisLength    = eval(request.args.get('MajorAxisLength'))
        MinorAxisLength    = eval(request.args.get('MinorAxisLength'))
        Eccentricity       = eval(request.args.get('Eccentricity'))
        ConvexArea         = eval(request.args.get('ConvexArea')) 
        EquivDiameter      = eval(request.args.get('EquivDiameter'))
        Extent             = eval(request.args.get('Extent'))
        Perimeter          = eval(request.args.get('Perimeter'))
        Roundness          = eval(request.args.get('Roundness'))
        AspectRation       = eval(request.args.get('AspectRation'))

        print("Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation\n",
              Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation)

        titanic = Titanic(Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation)
        predict = titanic.predict_model()
        # return jsonify({"Prediction:":int(predict)})
        return render_template("home.html",prediction = int(predict))


if __name__  == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)