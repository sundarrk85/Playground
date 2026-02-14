import pandas as pd
import pyodbc

# local server in my laptop SQL Server
connection_string = """
driver={SQL Server};
server=localhost\SQLEXPRESS;
database={TestDB};
trusted_connection=yes;
"""
connection = pyodbc.connect(connection_string)

cursor = connection.cursor()

query = "SELECT * FROM SYSOBJECTS WHERE xtype = 'U';"

df_existing_tables = pd.read_sql(query, connection)
df_existing_tables