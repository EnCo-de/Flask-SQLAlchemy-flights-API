import sqlite3
import pandas as pd


df = pd.read_excel('nonscheduled_flights_register.xlsx',
                   sheet_name='flights', # nrows=3,
                   header=0)
conn = sqlite3.connect("nonscheduled_flights_register.sqlite3")
c = conn.cursor()
df.to_sql('flights', conn, if_exists='append', index=False)
conn.close()

# print(df.head(2).T)

'''
import sqlite3
import pandas as pd

db = "nonscheduled_flights_register.sqlite3"
with sqlite3.connect(db) as conn:
    df = pd.read_sql('SELECT * FROM flights LIMIT 5;',
                    conn)
    print(df)
    
with sqlite3.connect(db) as conn:
    df1 = pd.read_sql('SELECT COUNT(arrival_1) FROM flights GROUP BY arrival_1, time(arrival_1_date_time);',
                    conn)
    print(df1)    
    '''