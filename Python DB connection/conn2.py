from sqlalchemy import create_engine
import pandas as pd

server = 'localhost\\SQLEXPRESS'
database = 'TestDB'

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

query = "SELECT * from Employee"

df = pd.read_sql(query, engine)

print(df)
