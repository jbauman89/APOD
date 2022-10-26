import requests
import json
import mysql.connector

try:
    
    connection = mysql.connector.connect(host='localhost', 
                                     database='apodlocal',
                                         user='root',
                                         password='')
    
    print("Connection successful...")
except:
    print("No connection!")

def apod():
            
    rawUrlString = r"https://api.nasa.gov/planetary/apod?api_key=[[[APIKEYGOESHERE]]]&count=1"
    data = requests.get(rawUrlString)
    jsonOut = json.loads(data.text)
    
    titlePull = jsonOut[0]["title"]
    datePull = jsonOut[0]["date"]
    explanationPull = jsonOut[0]["explanation"]
    urlPull = jsonOut[0]["url"]
    
    print("Title: " + titlePull)
    print("Date:" + datePull)
    print("Explanation: " + explanationPull)
    print("URL: " + urlPull)
    
    mySql_insert_query = """INSERT INTO apod (idNum, title, date, explanation, url) 
                            VALUES (%(insertNumber)s, %(title)s, %(dateOf)s, %(explanation)s, %(url)s) """
                            
    
    recordInsert = {'insertNumber' : 1,
                  'title' : titlePull,
                  'dateOf' : datePull,
                  'explanation' : explanationPull,
                  'url' : urlPull
            }
        
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query, recordInsert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into APOD table")
    cursor.close()

apod()
