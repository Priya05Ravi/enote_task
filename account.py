import pandas as pd
import pyodbc

sql_conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ENG-N413;"
                      "Database=master;"
                      "Trusted_Connection=yes;")

df = pd.read_csv("BI_assignment_account.csv", delimiter = ',')
df2 = df.fillna(value=0)
cursor = sql_conn.cursor()
cursor.execute("CREATE TABLE enote_task.ACCOUNT(id_account VARCHAR(20) PRIMARY KEY,id_person VARCHAR(20) FOREIGN KEY REFERENCES enote_task.CUSTOMERS11(id_person),account_type VARCHAR(20))")
for index, row in df2.iterrows():
   #print(row)
 cursor.execute("INSERT INTO enote_task.ACCOUNT([id_account],[id_person],[account_type]) values(?,?,?)",  row['id_account'], row['id_person'], row['account_type'])
 
 sql_conn.commit()
cursor.close()
sql_conn.close()