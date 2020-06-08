import pyodbc
server = 'localhost'
database = 'tweeter'
username = 'sa'
password = 'reallyStrongPwd123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#accounts = cursor.execute('select * from [dbo].[UserAccount]').fetchall()
#print(accounts)
