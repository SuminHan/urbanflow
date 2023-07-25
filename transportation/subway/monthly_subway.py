import pandas as pd
import psycopg2

def load_monthly_subway(line=None, station=None):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='urbanflow',
        user='guest',
        password='guest',
        host='localhost',
        port='5432'
    )
    
    # Define the SQL query to retrieve the data
    query = "SELECT * FROM subway_monthly_data"
    if line or station:
        if line and station:
            qwhere = f" WHERE line_number = '{line}' AND station_name = '{station}'"
        elif line:
            qwhere = f" WHERE line_number = '{line}'"
        elif station:
            qwhere = f" WHERE station_name = '{station}'"
        else:
            qwhere = ''
            
        query += qwhere
    

    # Load data into a GeoDataFrame
    df = pd.read_sql(query, conn)
    
    return df

