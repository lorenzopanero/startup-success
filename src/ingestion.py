import pandas as pd
import requests
import json # Open and read the JSON file 

# Funzione import csv
def download_from_drive(csv_name):
    with open("data/file_id.json", "r", encoding="utf-8") as f: 
        data = json.load(f) # Print the data 
    file_id = data[csv_name]
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    with open("file.csv", "wb") as f:
        f.write(response.content)
    return pd.read_csv("file.csv")
