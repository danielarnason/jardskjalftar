import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def make_url():
    """ 
        Makes the URL needed for making the call.
    """

    now = datetime.now().strftime('%Y-%m-%d %H:%M:00')
    yesterday = ( datetime.now() - timedelta(days=1) ).strftime('%Y-%m-%d %H:%M:00')
    base_url = f'http://drifandi.vedur.is/skjalftavefsja/identify.jsp?sEQLonRange=&sEQLatRange=&DateTimeRange=2018-4-26%2014:24:00;{now}&MagnitudeRange=0.0;6.0&DepthRange=0.0;100.0&Coords=&mapPosX=63.2114474630243&mapPosX2=66.5984732651655&mapPosY=-12.652575664186&mapPosY2=-25.1845711321084&orderby=OTIME&desc=true'
    
    return base_url

def get_data_from_url(url):
    """
        Gets the data from the specified URl.
    """
    r = requests.get(url).text
    return r

if __name__ == '__main__':
    url = make_url()
    data = get_data_from_url(url)
