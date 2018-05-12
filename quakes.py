import requests
import re
import json
import pandas as pd
from sqlalchemy import create_engine

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

def create_list_from_str(string):
    quake_list = re.findall(r'({.*?})', quakes)
    quake_list = [i.replace("'", '"') for i in quake_list]

    quake_list = [i.replace("new Date(",'"') for i in quake_list]
    quake_list = [i.replace(")",'"') for i in quake_list]
    quake_list = [json.loads(i) for i in quake_list]
    return quake_list

def upload_into_postgres(dataframe):
    engine = create_engine('postgresql://localhost:5432/danielarnason')
    dataframe.to_sql('quakes', engine, if_exists='append')

if __name__ == '__main__':
    site = get_data_from_url(base_url)
    quakes = parse_table(site)

    list_of_quakes = create_list_from_str(quakes)

    dataframe = pd.DataFrame(list_of_quakes)

    upload_into_postgres(dataframe)
