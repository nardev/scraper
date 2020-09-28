import requests
from lxml import html
from bs4 import BeautifulSoup
import re
import json

# Zamisao je bila da se vraca sledeci json, ali posto je html tako prljav i podlozan cestim izmjenama, onda ce se vracati samo najosnovniji podatci
# potrosnja minuta, sms-ova, data, potrosnaj izvan paketa i neplaceni racuni
# {
#     'paket': 'Extra NET'
#     'opis_paketa': '- Opcija 20.00\n - SIM + asemblirana 24 mj.'
#     'potrosnja_paket': {
#         'pozivi': '100 /100 min',
#         'sms': '27 /100 SMS',
#         'data': '6914 /10240 MB'
#     },
#     'potrosnja_izvan_paketa': '26.56 KM',
#     'preneseni_iznos': '0.00 KM',
#     'neplaceni_racuni': '0.00 KM',
#     'stanje_otplate': {
#         'opis': 'Huawei P30 Lite DS'
#         'iznos_rate': '23.45 KM'
#         'preostale_rate': '12/24'
#     }
# }

# USERNAME - puni broj sa pozivnim drzave
# USERNAME2 - samo broj sa pozivnim, 06...
# PASSWORD - vas login

data = {
    'broj': "",
    'potrosnja_pozivi': "",
    'potrosnja_pozivi_text': "",
    'potrosnja_sms': "",
    'potrosnja_sms_text': "",
    'potrosnja_data': "",
    'potrosnja_data_text': "",
    'potrosnja_izvan_paketa': "",
    'neplaceni_racuni': "",
}

def fetch(credentials):
    username = credentials['username_full']
    username2 = credentials['username_short']
    password = credentials['password']
    
    login_url = "https://moj.bhtelecom.ba/c/portal/login?p_l_id=20129"
    url_auth_form = 'https://prijava.bhtelecom.ba/commonauth'
    url_status_page = 'https://moj.bhtelecom.ba/web/guest/stanje-racuna'


    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.post(login_url)
    soup = BeautifulSoup(result.content,'html5lib')
    sdk1 = soup.find_all('input', {"name":"sessionDataKey"})[0]['value']
    sdk2 = soup.find_all('input', {"name":"sessionDataKey"})[1]['value']
    payload = "username_2="+username2+'&username='+username+'&password='+password+'&sessionDataKey='+sdk1+'&sessionDataKey='+sdk2
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    result = session_requests.post(url_auth_form, data = payload, headers=headers, cookies = dict(result.cookies))
    result = session_requests.get(url_status_page, cookies = dict(result.cookies))
    soup = BeautifulSoup(result.content, 'html5lib')

    rows = soup.find(text="Potrošnja u paketu:").find_parent('div').find_all('div', class_='form-group')
    data['broj'] = soup.body.find_all(text=re.compile('^3876'))[0].strip()

    rows = soup.find(text="Potrošnja u paketu:").find_parent('div').find_all('div', class_='form-group')
    
    minod = rows[0].find('span', class_='mainLabel').get_text().strip()
    mindo = rows[0].find('span', class_='littleLabel').get_text().strip()
    
    data['potrosnja_pozivi'] = minod
    data['potrosnja_pozivi_text'] = minod+mindo

    minod = rows[1].find('span', class_='mainLabel').get_text().strip()
    mindo = rows[1].find('span', class_='littleLabel').get_text().strip()
    
    data['potrosnja_sms'] = minod
    data['potrosnja_sms_text'] = minod+mindo

    minod = rows[2].find('span', class_='mainLabel').get_text().strip()
    mindo = rows[2].find('span', class_='littleLabel').get_text().strip()
    
    data['potrosnja_data'] = minod
    data['potrosnja_data_text'] = minod+mindo
    
    izvan_paketa = soup.find(text=" Potrošnja izvan paketa: ").find_parent('div').find('span', class_='mainLabel').get_text().strip()
    neplaceni = soup.find(text="Neplaćeni računi: ").find_parent('div').find('span', class_='mainLabel').get_text().strip()

    data['potrosnja_izvan_paketa'] = izvan_paketa
    data['neplaceni_racuni'] = neplaceni

    return data

    # make a return here!!!

def get_table_row(data):
    tabledata = []
    provider = 'BH Telecom d.d. Sarajevo - (mobile)'
    description = 'Broj pretplatnika: +'+data['broj'] + '\n' + \
                    'Potrosnja u paketu:' +'\n' + \
                    ' - Minuta: '+data['potrosnja_pozivi_text'] +'\n' + \
                    ' - SMS poruke: '+data['potrosnja_sms_text'] +'\n' + \
                    ' - Data 4G UMTS: '+data['potrosnja_data_text'] +'\n' + \
                    'Potrosnja izvan paketa: '+data['potrosnja_izvan_paketa'] +'\n' + \
                    'Neplaceni iznos: '+data['neplaceni_racuni']
    state = data['neplaceni_racuni']
    tabledata = [provider,description, state]
    return tabledata


if __name__ == '__main__':
    import config
    credentials = config.credentials['bht']
    data = fetch(credentials)
    print(data)