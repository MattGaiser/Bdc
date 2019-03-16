from flask import Flask, request, render_template, url_for
from flaskext.mysql import MySQL
import csv
app = Flask(__name__, template_folder='templates/', static_folder='static/')

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'events'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Hack@th0n2019'
app.config['MYSQL_DATABASE_DB'] = 'car_inventory'
app.config['MYSQL_DATABASE_HOST'] = 'http://hackathon-db.bdc.n360.io/'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

class Row:
    def __init__(self, num, q, p, sedan, suv, truck, hatch, coupe):
        self.num = num
        self.q = q
        self.p = p
        self.sedan = int(sedan)
        self.suv = int(suv)
        self.truck = int(truck)
        self.hatch = int(hatch)
        self.coupe = int(coupe)

@app.route('/')
@app.route('/index')
def entry_point():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        listOfRows = []
        for row in csv_reader:
            temp = Row(int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]))
            listOfRows.insert(0,temp)

    return render_template('index.html', data= listOfRows)

@app.route('/result')
def result():
    sedan = request.args.get('sedan')
    suv = request.args.get('suv')
    truck = request.args.get('truck')
    hatchback = request.args.get('hatch')
    coupe = request.args.get('coupe')

    sqlquery = "select * from hackathon.car_inventory where car_id=3620450"
    cursor.execute(sqlquery)

    data = cursor.fetchone()
    return render_template('results.html', data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
    #app.run(debug=True)