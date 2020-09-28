import http.client
import urllib
import json


data = {
    'sifra_korisnika': '',
    'kupac': '',
    'posljednja_izmjena': '',
    'posljednja_uplata': '',
    'datum_unosa': '',
    'stanje': ''
}


def fetch(credentials):
    payload = {
        "ime": credentials['name'],
        "sifraKupca": credentials['user_id']
    }

    encoded_query = urllib.parse.urlencode(payload)

    conn = http.client.HTTPSConnection("www.sarajevogas.ba")
    conn.request("POST", '/wp-json/api/v1/provjeraracuna?'+encoded_query)
    res = conn.getresponse().read().decode('utf8')
    res = json.loads(res)

    data['kupac'] =  res[0]['Kupac']
    data['sifra_korisnika'] =  res[0]['Sifra']
    data['posljednja_izmjena'] =  res[0]['OcitanjeDatumRacun']
    data['posljednja_uplata'] =  res[0]['ZadnjaUplata']
    data['datum_unosa'] =  res[0]['DatumUnosa']
    data['stanje'] =  res[0]['Saldo']

    return data

def get_table_row(data):
    tabledata = []
    provider = 'KJKP "Sarajevogas" d.o.o.'

    description = 'Korisnik: '+data['kupac']+ \
        '\nSifra: '+data['sifra_korisnika']+ \
        '\nPosljednja Izmjena: '+data['posljednja_izmjena']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata


if __name__ == '__main__':
    import config
    credentials = config.credentials['sagas']
    data = fetch(credentials)
    print(data)