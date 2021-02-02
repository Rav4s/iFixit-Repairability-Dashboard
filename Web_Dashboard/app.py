import time
import csv
from flask import Flask, make_response, request, render_template, redirect, url_for, send_from_directory #Import flask web server and additional components

app = Flask(__name__)
smartphone_file = "../smartphone.csv"
tablet_file = "../tablet.csv"
laptop_file = "../laptop.csv"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/worst-offenders')
def worst_offenders():
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

    return render_template('worst-offenders.html', smartphone=bad_smartphone, tablet=bad_tablet, laptop=bad_laptop,smartphone_3=bad_smartphone_3, tablet_3=bad_tablet_3, laptop_3=bad_laptop_3, smartphone_2=bad_smartphone_2, tablet_2=bad_tablet_2, laptop_2=bad_laptop_2)

@app.route('/most-repairable')
def most_repairable():
    smartphone = []
    tablet = []
    laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        good_smartphone = []
        good_smartphone_2 = []
        good_smartphone_3 = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                good_smartphone.append(message)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                good_smartphone_2.append(message)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                good_smartphone_3.append(message)
    with open(tablet_file, 'r', newline='') as file:
        good_tablet = []
        good_tablet_2 = []
        good_tablet_3 = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                good_tablet.append(message)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                good_tablet_2.append(message)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                good_tablet_3.append(message)
    with open(laptop_file, 'r', newline='') as file:
        good_laptop = []
        good_laptop_2 = []
        good_laptop_3 = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                good_laptop.append(message)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                good_laptop_2.append(message)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                good_laptop_3.append(message)

    return render_template('most-repairable.html', smartphone=good_smartphone, tablet=good_tablet, laptop=good_laptop,smartphone_3=good_smartphone_3, tablet_3=good_tablet_3, laptop_3=good_laptop_3, smartphone_2=good_smartphone_2, tablet_2=good_tablet_2, laptop_2=good_laptop_2)

@app.route('/one')
def one():
    one_smartphone = []
    one_tablet = []
    one_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                one_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                one_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '1':
                message = row[0] + " " + row[1]
                one_laptop.append(message)

    return render_template('one.html', smartphone=one_smartphone, tablet=one_tablet, laptop=one_laptop)

@app.route('/two')
def two():
    two_smartphone = []
    two_tablet = []
    two_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                two_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                two_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '2':
                message = row[0] + " " + row[1]
                two_laptop.append(message)

    return render_template('two.html', smartphone=two_smartphone, tablet=two_tablet, laptop=two_laptop)

@app.route('/three')
def three():
    three_smartphone = []
    three_tablet = []
    three_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                three_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                three_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '3':
                message = row[0] + " " + row[1]
                three_laptop.append(message)

    return render_template('three.html', smartphone=three_smartphone, tablet=three_tablet, laptop=three_laptop)

@app.route('/four')
def four():
    four_smartphone = []
    four_tablet = []
    four_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '4':
                message = row[0] + " " + row[1]
                four_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '4':
                message = row[0] + " " + row[1]
                four_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '4':
                message = row[0] + " " + row[1]
                four_laptop.append(message)

    return render_template('four.html', smartphone=four_smartphone, tablet=four_tablet, laptop=four_laptop)

@app.route('/five')
def five():
    five_smartphone = []
    five_tablet = []
    five_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '5':
                message = row[0] + " " + row[1]
                five_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '5':
                message = row[0] + " " + row[1]
                five_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '5':
                message = row[0] + " " + row[1]
                five_laptop.append(message)

    return render_template('five.html', smartphone=five_smartphone, tablet=five_tablet, laptop=five_laptop)

@app.route('/six')
def six():
    six_smartphone = []
    six_tablet = []
    six_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '6':
                message = row[0] + " " + row[1]
                six_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '6':
                message = row[0] + " " + row[1]
                six_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '6':
                message = row[0] + " " + row[1]
                six_laptop.append(message)

    return render_template('six.html', smartphone=six_smartphone, tablet=six_tablet, laptop=six_laptop)

@app.route('/seven')
def seven():
    seven_smartphone = []
    seven_tablet = []
    seven_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '7':
                message = row[0] + " " + row[1]
                seven_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '7':
                message = row[0] + " " + row[1]
                seven_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '7':
                message = row[0] + " " + row[1]
                seven_laptop.append(message)

    return render_template('seven.html', smartphone=seven_smartphone, tablet=seven_tablet, laptop=seven_laptop)

@app.route('/eight')
def eight():
    eight_smartphone = []
    eight_tablet = []
    eight_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                eight_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                eight_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '8':
                message = row[0] + " " + row[1]
                eight_laptop.append(message)

    return render_template('eight.html', smartphone=eight_smartphone, tablet=eight_tablet, laptop=eight_laptop)

@app.route('/nine')
def nine():
    nine_smartphone = []
    nine_tablet = []
    nine_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                nine_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                nine_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '9':
                message = row[0] + " " + row[1]
                nine_laptop.append(message)

    return render_template('nine.html', smartphone=nine_smartphone, tablet=nine_tablet, laptop=nine_laptop)

@app.route('/ten')
def ten():
    ten_smartphone = []
    ten_tablet = []
    ten_laptop = []
    with open(smartphone_file, 'r', newline='') as file:
        smartphone = []
        reader = csv.reader(file)
        for row in reader:
            smartphone.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                ten_smartphone.append(message)
    with open(tablet_file, 'r', newline='') as file:
        tablet = []
        reader = csv.reader(file)
        for row in reader:
            tablet.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                ten_tablet.append(message)
    with open(laptop_file, 'r', newline='') as file:
        laptop = []
        reader = csv.reader(file)
        for row in reader:
            laptop.append(row)
            if row[2] == '10':
                message = row[0] + " " + row[1]
                ten_laptop.append(message)

    return render_template('ten.html', smartphone=ten_smartphone, tablet=ten_tablet, laptop=ten_laptop)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=1235)