import pandas as pd
import csv

df = pd.read_csv("merged_dataset.csv")

del df["No.1"]
del df["Distance1"]
del df["Star_name1"]
del df["Mass1"]
del df["Radius1"]

data = df.rename({
    "Luminosity": "Brightness",
    "Star_name": "Stars",
    "Distance": "Star_Distance",
    "Mass": "Star_Mass",
    "Radius": "Star_Radius"
}, 
axis = "columns")

data.to_csv("cleaned.csv")