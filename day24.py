import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempreture = []
    for row in data:
        if row[1]!="temp":
            tempreture.append(row[1])
    print(tempreture)
