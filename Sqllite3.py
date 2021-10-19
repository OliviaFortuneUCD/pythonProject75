# https://www.sqlitetutorial.net/sqlite-sample-database/


# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    con = pd.read_sql_query("SELECT * FROM Employee", engine)
    print(con)