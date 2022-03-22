from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
app = Flask(__name__)
DB_conf = { 'user': 'root', 'password': 'root', 'host': 'db',
            'port': '3306', 'database': 'geography' }
def test_table():
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM countries')
   results = [c for c in cursor]
   cursor.close()
   connection.close()
   return results

def add_item(nation, capital, population, area):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"INSERT INTO countries (nation, capital, population, area) VALUES ('{nation}', '{capital}','{population}', '{area}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

def delete_items(nation):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"DELETE FROM countries WHERE nation = ('{nation}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

@app.route('/add')
def add():
   nation = request.args.get("nation", "", str)
   capital = request.args.get("capital", "", str)
   population = request.args.get("population", "", str)
   area = request.args.get("area", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Added a capital</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Added a capital</h1>\n"
   if nation != "" and capital != "" and population != "" and area != "":
      S += add_item(nation, capital, population, area)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/delete')
def delete():
   nation = request.args.get("nation", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Removed a nation from the list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Removed a nation from the list</h1>\n"
   if nation != "" :
      S += delete_items(nation)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/test')
def index_test():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Nation cities list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Nation cities list</h1>\n"
   S += "      <table>\n"
   for (nation, capital, population, area) in test_table():
      S += f"          <tr><td> <div> <input type="radio"</div> {nation}: {capital}: {population}: {area} </td></tr>\n"
   S += "      </table>\n"
   S += "      <p><a href='/addform'>Add new nation</a></p>\n"
   S += "      <p><a href='/deleteform'>Delete a nation</a></p>\n"
   S += "      <form action='/delete'>\n"
   S += "      <input type='submit' value='Delete'/>\n"
   S += "      </form>\n"
   S += "      <form action='/add'>\n"
   S += "      <input type='text' name='nation' value=''/>\n"
   S += "      <input type='text' name='capital' value=''/>\n"
   S += "      <input type='text' name='population' value=''/>\n"
   S += "      <input type='text' name='area' value=''/>\n"
   S += "      <input type='submit' value='Add'/>\n"
   S += "      </form>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/')
def index():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += "      <title>Nation cities list</title>\n"
   S += style()
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Nation cities list</h1>\n"
   S += "      <ul>\n"
   for (nation, capital, population, area) in test_table():
      S += f"         <li>{nation}: {capital}: {population}: {area}</li>\n"
   S += "      </ul>\n"
   S += "      <p><a href='/addform'>Add new nation</a></p>\n"
   S += "      <p><a href='/deleteform'>Delete a nation</a></p>\n"
   S += "      <form action='/delete'>\n"
   S += "      <input type='submit' value='Delete'/>\n"
   S += "      </form>\n"
   S += "      <form action='/add'>\n"
   S += "      <input type='text' name='nation' value=''/>\n"
   S += "      <input type='text' name='capital' value=''/>\n"
   S += "      <input type='text' name='population' value=''/>\n"
   S += "      <input type='text' name='area' value=''/>\n"
   S += "      <input type='submit' value='Add'/>\n"
   S += "      </form>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S

@app.route('/addform')
def addform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <head>\n"
    S += " <title>Entering a value</title>\n"
    S += style()
    S += " </head>\n"
    S += " <body>\n"
    S += " <h1>Entering a value</h1>\n"
    S += " <form action='/add'>\n"
    S += " <input type='text' name='nation' value=''/>\n"
    S += " <input type='text' name='capital' value=''/>\n"
    S += " <input type='text' name='population' value=''/>\n"
    S += " <input type='text' name='area' value=''/>\n"
    S += " <input type='submit' value='Submit'/>\n"
    S += " </form>\n"
    S += " </body>\n"
    S += "</html>\n"
    return S

@app.route('/deleteform')
def deleteform():
    S = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += " <head>\n"
    S += " <title>Deleting a nation</title>\n"
    S += style()
    S += " </head>\n"
    S += " <body>\n"
    S += " <h1>Deleting a nation</h1>\n"
    S += " <form action='/delete'>\n"
    S += " <input type='text' name='nation' value=''/>\n"
    S += " <input type='submit' value='Submit'/>\n"
    S += " </form>\n"
    S += " </body>\n"
    S += "</html>\n"
    return S

def style():
    S = "<style>\n"
    S += " body {background-color: #FFEEDD; }\n"
    S += "</style>\n"
    return S

if __name__ == '__main__':
   app.run(host='0.0.0.0')
  