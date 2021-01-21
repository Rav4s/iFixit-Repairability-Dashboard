import time
import csv
from flask import Flask, make_response, request, render_template, redirect, url_for, send_from_directory #Import flask web server and additional components

app = Flask(__name__)
smartphone_file = "/home/ravi/Documents/Git/iFixit-Repairability-Dashboard/smartphone.csv"
tablet_file = "/home/ravi/Documents/Git/iFixit-Repairability-Dashboard/tablet.csv"
laptop_file = "/home/ravi/Documents/Git/iFixit-Repairability-Dashboard/laptop.csv"

@app.route('/')
def index():
    smartphone = []
    tablet = []
    laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        bad_smartphone = []
        bad_smartphone_2 = []
        bad_smartphone_3 = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                bad_smartphone.append(message)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                bad_smartphone_2.append(message)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                bad_smartphone_3.append(message)
    with open(tablet_file, 'r', newline='') as file:
        bad_tablet = []
        bad_tablet_2 = []
        bad_tablet_3 = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                bad_tablet.append(message)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                bad_tablet_2.append(message)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                bad_tablet_3.append(message)
    with open(laptop_file, 'r', newline='') as file:
        bad_laptop = []
        bad_laptop_2 = []
        bad_laptop_3 = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                bad_laptop.append(message)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                bad_laptop_2.append(message)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                bad_laptop_3.append(message)

    return render_template('index.html', smartphone=bad_smartphone, tablet=bad_tablet, laptop=bad_laptop,smartphone_3=bad_smartphone_3, tablet_3=bad_tablet_3, laptop_3=bad_laptop_3, smartphone_2=bad_smartphone_2, tablet_2=bad_tablet_2, laptop_2=bad_laptop_2)
2
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1235) #Run the webserver2
