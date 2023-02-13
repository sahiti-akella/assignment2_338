import json 
import random

# load data into read_data
with open("ex2.json", "r") as file:
    read_data = json.load(file)

# reverse read_data
random.shuffle(read_data)
for sublist in read_data:
    random.shuffle(sublist)

# create new file with reversed data
random_json_file = open("ex2_5.json", "w")
json.dump(read_data, random_json_file, indent = 2)

random_json_file.close()
