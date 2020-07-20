import pandas as pd
import pyodbc
 
sql_conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ENG-N413;"
                      "Database=master;"
                      "Trusted_Connection=yes;")

 
df = pd.read_csv("BI_assignment_person.csv", delimiter = ',',nrows=19947)
df2 = df.fillna(value="")
cursor = sql_conn.cursor()
cursor.execute("CREATE SCHEMA enote_task")
cursor.execute("CREATE TABLE enote_task.CUSTOMERS(id_person VARCHAR(20) NOT NULL,name VARCHAR(200),surname VARCHAR(250),zip VARCHAR(50),city VARCHAR(100) ,country  VARCHAR(250) ,email  VARCHAR(250),phone_number  VARCHAR(25),birth_date VARCHAR(20),PRIMARY KEY (id_person))")
for index, row in df2.iterrows():
   #print(row)
 #if not df2.empty:
    cursor.execute("INSERT INTO enote_task.CUSTOMERS([id_person],[name],[surname],[zip],[city],[country],[email],[phone_number],[birth_date]) values(?,?,?,?,?,?,?,?,?)", row['id_person'], row['name'], row['surname'], row['zip'],row['city'], row['country'], row['email'], row['phone_number'], row['birth_date'])
 
    sql_conn.commit()
cursor.close()
sql_conn.close()
