from flask import Flask,jsonify,render_template,request
from Project_H.utils import Happiness
import config


app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("start12.html")

@app.route("/GHI",methods=["GET","POST"])
def get_prediction():
    data=request.form 

    Overall_rank=eval(data["Overall_rank"])
    Year=eval(data["Year"])
    GDP_per_capital=eval(data["GDP_per_capital"])
    Social_support=eval(data["Social_support"])
    Healthy_life_expectancy=eval(data["Healthy_life_expectancy"])
    Freedom_to_make_life_choices=eval(data["Freedom_to_make_life_choices"])
    Generosity=eval(data["Generosity"])
    Perceptions_of_corruption=eval(data["Perceptions_of_corruption"])

    obj=Happiness(Overall_rank,Year,GDP_per_capital, Social_support,Healthy_life_expectancy,
                Freedom_to_make_life_choices, Generosity,Perceptions_of_corruption)
    Happy_Index=obj.Get_Happiness_Index()
    
    return render_template("end.html",result=Happy_Index)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.port_number)