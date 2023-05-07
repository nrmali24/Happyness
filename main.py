import numpy as np
import os
import Project_H
import config
import pickle
import json

from flask import Flask,jsonify,render_template,request


app=Flask(__name__)

with open (config.model,"rb") as file:
    model=pickle.load(file)

with open (config.project_data,"r") as file:
    project_data=json.load(file)

@app.route("/")
def Homee():
    return render_template("start12.html",)

@app.route("/Predict",methods=["GET","POST"])
def pred():
    data=request.form
    test_array=np.zeros(len(project_data["columns"]))
    test_array[0]=eval(data["Overall_rank"])
    test_array[1]=eval(data["Year"])
    test_array[2]=eval(data["GDP_per_capital"])
    test_array[3]=eval(data["Social_support"])
    test_array[4]=eval(data["Healthy_life_expectancy"])
    test_array[5]=eval(data["Freedom_to_make_life_choices"])
    test_array[6]=eval(data["Generosity"])
    test_array[7]=eval(data["Perceptions_of_corruption"])

    Happiness=model.predict([test_array])
    
    return render_template("end.html",Happiness=Happiness)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.port_number)