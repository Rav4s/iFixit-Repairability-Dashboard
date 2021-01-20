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
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '1':
                message = "The " + row[0] + " " + row[1] + " is a very unrepairable device with a Repairability Score of only 1/10."
                bad_smartphone.append(message)
            print(bad_smartphone)
    with open(tablet_file, 'r', newline='') as file:
        bad_tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '1':
                message = "The " + row[0] + " " + row[1] + " is a very unrepairable device with a Repairability Score of only 1/10."
                bad_tablet.append(message)
            print(bad_tablet)
    with open(laptop_file, 'r', newline='') as file:
        bad_laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '1':
                message = "The " + row[0] + " " + row[1] + " is a very unrepairable device with a Repairability Score of only 1/10."
                bad_laptop.append(message)
            print(bad_laptop)

    return render_template('index.html', smartphone=bad_smartphone, tablet=bad_tablet, laptop=bad_laptop)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1235) #Run the webserver
