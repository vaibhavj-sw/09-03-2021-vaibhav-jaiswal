import json
import csv

JSON_file='sample.json'

def get_json(file_name):
    with open(file_name) as f:
        return(json.load(f))

json_data = get_json(JSON_file)
user_list = list(map(lambda x, y: ([x,x.update({'bmi':(x['WeightKg']/(y['HeightCm']/100))})]), json_data,json_data))
with open('t1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    t1=[]
    for row in csv_reader:
        t1.append(row)
        with open('output.csv', mode='a') as employee_file:
            writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            [[writer.writerow(list(i[0].values())+[row['category'],row['health']])] for i in filter(lambda sub: int(sub[0]['bmi']) >= float(row['lower_limit']) and int(sub[0]['bmi']) <= float(row['upper_limit']), user_list)]
        line_count += 1
