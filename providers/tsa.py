import requests
from lxml import html
import json
from bs4 import BeautifulSoup

data = {
    'sifra_korisnika': '',
    'naziv_korisnika': '',
    'adresa': '',
    'posljednja_izmjena': '',
    'stanje': ''
}

def fetch(credentials):
    session_requests = requests.session()
    url = "http://www.toplanesarajevo.ba/korisnici/stanje-racuna"

    payload = {
        "sifra_korisnika": credentials['user_id']
    }

    result = session_requests.post(url, data = payload)
    soup = BeautifulSoup(result.content, 'html5lib')

    rows = soup.find("table").find('tbody').find_all("tr")

    data['sifra_korisnika'] = rows[0].find_all('td')[1].get_text().strip()
    data['naziv_korisnika'] = rows[1].find_all('td')[1].get_text().strip() 
    data['adresa'] = rows[2].find_all('td')[1].get_text().strip() 
    data['stanje'] = rows[3].find_all('td')[1].get_text().strip() 
    data['posljednja_izmjena'] = rows[4].find_all('td')[1].get_text().strip() 

    return data

def get_table_row(data):
    tabledata = []
    provider = ' KJKP Toplane Sarajevo'

    description = 'Korisnik: '+data['naziv_korisnika']+ \
        '\nAdresa: '+data['adresa']+ \
        '\nPosljednja Izmjena: '+data['posljednja_izmjena']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata

if __name__ == '__main__':
    import config
    credentials = config.credentials['tsa']
    data = fetch(credentials)
