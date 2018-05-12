import requests
import re
import json

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

    quake_list = [json.loads(i) for i in quake_list]

    return quake_list

if __name__ == '__main__':
    site = get_data_from_url(base_url)
    quakes = parse_table(site)

    print(create_list_from_str(quakes))
