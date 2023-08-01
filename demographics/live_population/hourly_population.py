# import pandas as pd
# import psycopg2
# import datetime

# def load_live_population(areaids=None, start_date = datetime.date(2017, 1, 1), end_date = datetime.date(2017, 1, 1)):
#     # Establish a connection to the PostgreSQL database
#     conn = psycopg2.connect(
#         dbname='urbanflow',
#         user='guest',
#         password='guest',
#         host='localhost',
#         port='5432'
#     )
    
#     # Define the SQL query to retrieve the data
#     query = f"SELECT * FROM lte_population WHERE date >= {start_date} AND date <= {end_date};"

#     # Load data into a GeoDataFrame
#     df = pd.read_sql(query, conn)
    
#     return df

import pandas as pd
import psycopg2

def load_live_population(areaids=None, start_date=20170101, end_date=20170101):
    # Establish a connection to the PostgreSQL database
    conn = psycopg2.connect(
        dbname='urbanflow',
        user='guest',
        password='guest',
        host='localhost',
        port='5432'
    )

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Define the SQL query to retrieve the data with parameter placeholders
    query = "SELECT * FROM lte_population WHERE areaid IN %s AND ymd >= %s AND ymd <= %s;"

    # Execute the SQL query with the parameters
    cursor.execute(query, (tuple(areaids), start_date, end_date))
    columns = [column[0] for column in cursor.description]

    # Fetch the data
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Convert the data to a DataFrame
    #df = pd.DataFrame(data, columns=['id', 'ymd', 'hour', 'dong', 'areaid', 'total', 'm00', 'm10', 'm15', 'm20',
    #   'm25', 'm30', 'm35', 'm40', 'm45', 'm50', 'm55', 'm60', 'm65', 'm70',
    #   'f00', 'f10', 'f15', 'f20', 'f25', 'f30', 'f35', 'f40', 'f45', 'f50',
    #   'f55', 'f60', 'f65', 'f70'])  # Replace column names as needed
    df = pd.DataFrame(data, columns=columns)
    return df