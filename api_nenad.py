import requests
import json
import pandas as pd

response = requests.get(url="http://api.open-notify.org/astros.json")
print(response.status_code)
if response.status_code == 200:
    print("Requestot e uspesen")
    resp_dict = json.loads(response.text)
    list_of_astronauts = resp_dict["people"]
    df_astronauts = pd.DataFrame(list_of_astronauts)
    df_astronauts.to_csv("astronauts.csv", index=False, encoding="utf-8")
    print(df_astronauts.head())
    print("Fajlot e zapisan")


    #for astronaut in list_of_astronauts:
    #    print(f"Name: {astronaut['name']}, craft: {astronaut['craft']}")
else:
    print("Nastana greska")