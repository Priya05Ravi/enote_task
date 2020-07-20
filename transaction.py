import pandas as pd
import pyodbc
sql_conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ENG-N413;"
                      "Database=master;"
                      "Trusted_Connection=yes;")

 
df = pd.read_csv("BI_assignment_transaction.csv", delimiter = ',')
df2 = df.fillna(value=0)
cursor = sql_conn.cursor()

cursor.execute("CREATE TABLE enote_task.TRANSACTION(id_transaction VARCHAR(10),id_account VARCHAR(20) FOREIGN KEY REFERENCES ACCOUNT(id_account),transaction_type VARCHAR(20),transaction_date DATE,transaction_amount float(20))")
for index, row in df2.iterrows():
   #print(row)
 cursor.execute("INSERT INTO enote_task.TRANSACTION([id_transaction],[id_account],[transaction_type],[transaction_date],[transaction_amount]) values(?,?,?,?,?)", row['id_transaction'], row['id_account'], row['transaction_type'], row['transaction_date'],row['transaction_amount'])
 
 sql_conn.commit()
cursor.close()
sql_conn.close()
