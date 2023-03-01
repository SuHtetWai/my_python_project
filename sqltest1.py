import mysql.connector as connector
# from mysql import connector
dbConnection = connector.connect(
    host="localhost",
    user = "root",
    passwd = "rathart@281000"

)
print(dbConnection)