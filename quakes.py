import requests
import re
import json
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

base_url = 'http://en.vedur.is/earthquakes-and-volcanism/earthquakes/#view=table' 

def get_data_from_url(url):
    """
        Gets the data from the specified URl.
    """
    r = requests.get(url).text
    return r

def parse_table(html):
    quakeinfo = re.findall(r'VI\.quakeInfo = \[(.*)\]', html)
    return quakeinfo[0]

def parse_js_var(string):
    quake_list = re.findall(r'({.*?})', string)
    quake_list = [i.replace("'", '"') for i in quake_list]

    quake_list = [i.replace("new Date(",'"') for i in quake_list]
    quake_list = [i.replace(")",'"') for i in quake_list]
    quake_list = [json.loads(i) for i in quake_list]
    
    quake_list = parse_date(quake_list)

    return quake_list

def create_db_engine(db_url):
    return create_engine(db_url)

def upload_into_postgres(list_of_quakes, db_engine):
    dataframe = pd.DataFrame(list_of_quakes)
    dataframe['id'] = range(1, len(dataframe) + 1)
    dataframe.to_sql('quakes', db_engine, if_exists='append', index=False)

def remove_db_duplicates(sql_statement, db_engine):
    df = pd.read_sql_query(sql_statement, con=db_engine)
    df = df.drop_duplicates(subset='t')
    df.to_sql('quakes', db_engine, if_exists='replace', index=False)

def parse_date(lst):
    for quake in lst:
        time = quake['t']
        time = time.split(',')
        time[1] = time[1][:-2]
        time = ','.join(time)
        quake['t'] = datetime.strptime(time, '%Y,%m,%d,%H,%M,%S')
    return lst

if __name__ == '__main__':
    site = get_data_from_url(base_url)
    quakes_str = parse_table(site)

    list_of_quakes = parse_js_var(quakes_str)
    engine = create_db_engine('postgresql://localhost:5432/danielarnason')
    upload_into_postgres(list_of_quakes, engine)
    remove_db_duplicates('SELECT * FROM quakes;', engine)
