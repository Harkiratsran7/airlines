from flask import Flask,render_template, request
import mysql.connector
import datetime
# import pandas as pd

app = Flask(__name__)

'''mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "#Itsall4u",
    database='udemy_business'
)'''

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="#Itsall4u",
  database="udemy_business",
  auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor(buffered=True)
mycursor2 = mydb.cursor(buffered=True)

@app.route('/')
def index():
    data = '123'
    print('insnide index')
    return render_template('index.html', data=data)


@app.route('/charts')
def charts():
    mycursor.execute('select published_airline from flight_dataset.sample_data')
    data = (mycursor.fetchall())
    new_subscribers = []
    for all in data:
        new_subscribers.append(all[0])
    print(new_subscribers)
      
    return render_template('chartjs.html', data=new_subscribers)



@app.route('/chartsapi')
def chartsapi():
    mycursor.execute('select published_airline from flight_dataset.sample_data')
    data = (mycursor.fetchall())
    new_subscribers = []
    for all in data:
        new_subscribers.append(all[0])
    print(new_subscribers)
      
    return new_subscribers

if __name__ == '__main__':
    app.run(host='localhost', port=9874)



'''
CREATE TABLE some__other (
id varchar(255),
activity_period varchar(255),
operating_airline varchar(255),
operating_airline_iata_code varchar(255),
published_airline varchar(255),
published_airline_iata_code varchar(255),
geo_summary varchar(255),
geo_region varchar(255),
activity_type_code varchar(255),
price_category_code varchar(255),
terminal varchar(255),
boarding_area varchar(255),
passenger_count varchar(255),
adjusted_activity_type_code varchar(255),
adjusted_passenger_count varchar(255),
year varchar(255),
month varchar(255)
); '''




