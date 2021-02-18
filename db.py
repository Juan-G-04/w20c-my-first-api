import dbcreds
import mariadb
import sys

connection = None
cursor = None

def connect():
    return mariadb.connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )

def get(command, arguments=[]):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        result = cursor.fetchall()
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()
        return result

def put(command, arguments=[]):
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        connection.commit()
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()

def getAnimals():
    return get("SELECT * FROM Animals")
    
def getAnimal(id):
    return get("SELECT * FROM Animals WHERE Id IN (?)", [id])

def createAnimal(common_name, scientific_name):
    put("INSERT INTO Animals (Common_Name, Scientific_Name) VALUES (?, ?)", [common_name, scientific_name])

def updateAnimal(id, common_name, scientific_name):
    put("UPDATE Animals SET Common_Name = (?), Scientific_Name = (?) WHERE Id = (?)", [common_name, scientific_name, id])

def deleteAnimal(id):
    get("DELETE FROM Animals WHERE Id = (?)", [id])