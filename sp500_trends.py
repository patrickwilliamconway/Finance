import csv
from datetime import datetime


count = 0
data = {}
with open('data/sp500.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for line in csv_reader:
        if count > 0:
            weekday = datetime.strptime(line[0], "%Y-%m-%d").weekday()
            if weekday not in data:
                data[weekday] = []
            data[weekday].append((float(line[4])-float(line[1]))/float(line[1]) * 100)
            
        count += 1

days_map = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
}

print("S&P 500 Day Trends:")
for k in days_map:
    print(days_map[k], "- Average Price: ", len(data[k]), "Average Percent Change: ",sum(data[k])/len(data[k]))
