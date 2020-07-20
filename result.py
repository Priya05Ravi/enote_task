import pandas as pd
import pyodbc

sql_conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=ENG-N413;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
cursor = sql_conn.cursor()
cursor.execute("CREATE VIEW  Employee ([amt], [date] ,[account]) AS select sum(transaction_amount),(FORMAT(transaction_date, 'MM/yy')),id_account as transDate from enote_task.TRANSACTION568 where id_account in (345,1234) group by DATEPART(month, transaction_date),id_account,transaction_date")
sql_command="""select account,date as month,sum(amt) as sum_transactions from Employee group by date,account""";
cursor.execute(sql_command);
result = cursor.fetchall() 
print(result)
cursor.close()
sql_conn.close()
