import pandas as pd
import numpy as np
import pickle
import json
import pymongo
import config

class Titanic():
    def __init__(self,Area,MajorAxisLength,MinorAxisLength,Eccentricity,ConvexArea,EquivDiameter,Extent,Perimeter,Roundness,AspectRation):
        self.Area = Area
        self.MajorAxisLength = MajorAxisLength
        self.MinorAxisLength = MinorAxisLength
        self.Eccentricity = Eccentricity
        self.ConvexArea = ConvexArea
        self.EquivDiameter = EquivDiameter
        self.Extent = Extent
        self.Perimeter = Perimeter
        self.Roundness = Roundness
        self.AspectRation = AspectRation

    def load_saved_files(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
           self.model =  pickle.load(f)

        # with open(config.JSON_FILE_PATH,'r') as f:
        #     self.project_data = json.load(f)

    def predict_model(self):
        self.load_saved_files()

        # Embarked = 'Embarked_' + self.Embarked
        # index = self.project_data['Columns'].index(Embarked)

        columns = 10
        test_array = np.zeros(columns)

        test_array[0] = self.Area
        test_array[1] = self.MajorAxisLength
        test_array[2] = self.MinorAxisLength
        test_array[3] = self.Eccentricity
        test_array[4] = self.ConvexArea
        test_array[5] = self.EquivDiameter
        test_array[6] = self.Extent
        test_array[7] = self.Perimeter
        test_array[8] = self.Roundness
        test_array[9] = self.AspectRation

        print(test_array)

        predict_value = self.model.predict([test_array])[0]
        print("The Prediction is:",predict_value)

        return predict_value

if __name__ == "__main__":
    obj = Titanic
    obj
        


