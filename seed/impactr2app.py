import sys

fields = ["date", "time", "a_x", "a_y", "a_z", "roll", "pitch", "yaw", "ug_x", "ug_y", "ug_z", "o2", "hyd", "bpm", "other1", "other2", "other3", "other4"]

import csv

f = open(sys.argv[1])


dialect = csv.Sniffer().sniff(f.read(), delimiters=' ')


f.seek(0)

reader = csv.reader(f, dialect)

rows = []

obj = {}




float_fields = {'a_x', 'a_y', 'a_z', 'roll', 'pitch', 'yaw', 'ug_x', 'ug_y', 'ug_z'}
int_fields = {'o2', 'hyd', 'bpm', 'other1', 'other2', 'other3', 'other4'}
for row in reader:
    obj = {} # moved inside loop
    obj["username"] = "topila28"
    obj["date"] = str(row[0])
    obj["time"] = str(row[1])
    obj["a_x"] = float(row[2])
    obj["a_y"] = float(row[3])
    obj["a_z"] = float(row[4])
    obj["roll"] = float(row[5])
    obj["pitch"] = float(row[6])
    obj["yaw"] = float(row[7])
    obj["ug_x"] = float(row[8])
    obj["ug_y"] = float(row[9])
    obj["ug_z"] = float(row[10])
    obj["o2"] = int(row[11])
    obj["hyd"] = int(row[12])
    obj["bpm"] = int(row[13])
    obj["other1"] = int(row[14])
    obj["other2"] = int(row[15])
    obj["other3"] = int(row[16])
    obj["other4"] = int(row[17])
    #obj["other5"] = row[18]
    # for item, fieldname in zip(row, fields):
    #     if fieldname in float_fields:
    #         obj[fieldname] = float(item)
    #     elif fieldname in int_fields:
    #         obj[fieldname] = int(item)
    #     else:
    #         obj[fieldname] = str(item) 
    rows.append(obj)



import requests
requests.get("http://localhost:5000/api/players")


for obj in rows:
    requests.post("http://localhost:5000/api/impact", json=obj)

    #to run use python3 impactr2app.py














# for row in reader:
#   print("In first loop ")
#   for i, field in enumerate(fields):
#       obj[field] = row[i]
#       print("Object Field " + obj[field])
#       #print("Object Field Type " + str(type(row[i])))
#       if field == "a_x":
#           obj[field] = float(row[i])
#           b= obj[field]
#           print("Object Field Type " + str(isinstance(b, float)))
#       elif field == "a_y":
#           obj[field] = float(row[i])
#       elif field == "a_z":
#           obj[field] = float(row[i])
#       elif field == "roll":
#           obj[field] = float(row[i])
#       elif field == "pitch":
#           obj[field] = float(row[i])
#       elif field == "yaw":
#           obj[field] = float(row[i])
#       elif field == "ug_x":
#           obj[field] = float(row[i])
#       elif field == "ug_y":
#           obj[field] = float(row[i])
#       elif field == "ug_z":
#           obj[field] = float(row[i])
#       elif field == "o2":
#           obj[field] = int(row[i])
#           b= obj[field]
#           print("Object Field Type " + str(isinstance(b, int)))
#       elif field == "hyd":
#           obj[field] = int(row[i])
#       elif field == "bpm":
#           obj[field] = int(row[i])
#       else:
#           obj[field] = str(row[i])
#   rows.append(obj)
