import os
import json
import pickle
import numpy as np
import Project_H
import config


class Happiness():
    def __init__(self,Overall_rank,Year,GDP_per_capital,Social_support,Healthy_life_expectancy,
                Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption):
        self.Overall_rank=Overall_rank
        self.Year=Year
        self.GDP_per_capital=GDP_per_capital
        self.Social_support=Social_support
        self.Healthy_life_expectancy=Healthy_life_expectancy
        self.Freedom_to_make_life_choices=Freedom_to_make_life_choices
        self.Generosity=Generosity
        self.Perceptions_of_corruption=Perceptions_of_corruption
    
    def load_path(self):
        with open (config.model,"rb") as file:
            self.model=pickle.load(file)
        with open (config.project_data,"r")as file:
            self.data=json.load(file)
    
    def Get_Happiness_Index(self):
        self.load_path()

        test_array=np.zeros(len(self.data["columns"]))
        test_array[0]=self.Overall_rank
        test_array[1]=self.Year
        test_array[2]=self.GDP_per_capital
        test_array[3]=self.Social_support
        test_array[4]=self.Healthy_life_expectancy
        test_array[5]=self.Freedom_to_make_life_choices
        test_array[6]=self.Generosity
        test_array[7]=self.Perceptions_of_corruption

        print(test_array)

        result = self.model.predict([test_array])
        return result



        
        


