"""
Training function
"""
from model import gp_model
import pandas as pd

if __name__ == "__main__":

    # read in data
    data_type = ["max_precipitation", "mean_precipitation", "max_temperature", "min_temperature"]
    for data_name in data_type:
        
        print("Training {}".format(data_name))
        
        # read in data
        data_csv = pd.read_csv("./data/{}.csv".format(data_name), sep = "\t")

        # only take parts of the data to train
        data_csv = data_csv[data_csv["Year"] > 2015]

        # parse data name for model reading
        data_name = data_name.split("_")
        data_name = "".join(data_name)
        
        
        X = data_csv.iloc[:, [1,2]]
        y = data_csv.iloc[:, [3]]

        # using default jitter
        gp_model.train_gp_model(X, y, data_name)

    



