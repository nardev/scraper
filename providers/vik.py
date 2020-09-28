import requests
from lxml import html
from bs4 import BeautifulSoup

data = {
    'korisnik': '',
    'adresa': '',
    'datum_unosa': '',
    'opis': '',
    'stanje': ''
}

def fetch(credentials):
    session_requests = requests.session()
    url = "http://app.viksa.ba/analitikaPotrosaca_e"

    result = session_requests.post(url)
    url = result.url
    soup = BeautifulSoup(result.content, 'html.parser')
    payload = {
        "userName_TextBox": credentials['username'],
        "password_TextBox": credentials['password'],
        "logon_Button": "Prijava",
        "__VIEWSTATE":soup.find(id="__VIEWSTATE")['value'],
        "__VIEWSTATEGENERATOR":soup.find(id="__VIEWSTATEGENERATOR")['value'],
        "__EVENTVALIDATION":soup.find(id="__EVENTVALIDATION")['value']
    }


    result = session_requests.post(url, data = payload)
    soup = BeautifulSoup(result.content, 'html.parser')
    payload = {
        "__VIEWSTATE":soup.find(id="__VIEWSTATE")['value'],
        "__VIEWSTATEGENERATOR":soup.find(id="__VIEWSTATEGENERATOR")['value'],
        "__EVENTVALIDATION":soup.find(id="__EVENTVALIDATION")['value'],
        "MjernaMjesta_GridView$ctl02$idiNa_Button":"Računi / Uplate"
    }
    result = session_requests.post(url, data = payload)

    soup = BeautifulSoup(result.content, 'html.parser')
    data['korisnik'] = soup.body.find(id="NazivPotrosaca_Label").get_text().strip()
    data['adresa'] = soup.body.find(id="Adresa_Label").get_text().strip()
    data['datum_unosa'] = soup.body.find(id="saldoNaDan_Label").get_text().strip()
    data['opis'] = soup.body.find(id="DugPreplata_Label").get_text().strip()
    data['stanje'] = soup.body.find(id="Saldo_Label").get_text().strip()
    
    return data

def get_table_row(data):
    tabledata = []
    provider = 'Vodovod i kanalizacija d.o.o Sarajevo.'

    description = 'Korisnik: '+data['korisnik']+ \
        '\nAdresa: '+data['adresa']+ \
        '\nPosljednja Izmjena: '+data['datum_unosa']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata

if __name__ == '__main__':
    import config
    credentials = config.credentials['vik']
    data = fetch(credentials)
    print(data)