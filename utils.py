import  pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle

class IrisFlowerSpecies():
    #'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLenghtCm,PetalWidthCm):
        self.SepalLenghtCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLenghtCm = PetalLenghtCm
        self.PetalWidhtCm = PetalWidthCm
        return
    def load_model(self):
        with open('artifacts/model_logistic.pickle','rb') as fp:
            self.model = pickle.load(fp)
            #print(self.model)
    def predict_species(self):
        self.load_model()
        test_array = np.zeros(self.model.n_features_in_)
        test_array[0] = self.SepalLenghtCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLenghtCm
        test_array[3] = self.PetalWidhtCm
        pridict_species = self.model.predict([test_array])[0]
        #print(pridict_species)
        return pridict_species

obj = IrisFlowerSpecies(5.6,2.3,6.0,2.4)
obj.load_model()
obj.predict_species()