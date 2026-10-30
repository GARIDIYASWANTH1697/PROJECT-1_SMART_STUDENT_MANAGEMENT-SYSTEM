import os
import json
DATABASE_FILE = "database.json"
def load_data():

    if not os.path.exists(DATABASE_FILE):
        return[]
    with open (DATABASE_FILE,"r") as file:
        data = json.load(file)
    return data
def save_data(students):
    with open(DATABASE_FILE,"w") as file:
        json.dump(students,file,indent= 4)