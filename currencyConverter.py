#Enter dollar amount and get converted currency US to Canada
#Uses requests to get currency exchange from Google

import requests
from bs4 import BeautifulSoup


google = ''
t = False

while(t == False):
    google = input('Do you have US or CAD? ')
    if(google == 'US' or 'CAD'):
        t = True


if(google == 'us' or 'US' or 'Us'):
    response = requests.get('https://transferwise.com/us/currency-converter/usd-to-cad-rate')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        soup.prettify()
        usd = soup.find_all(href = "/us/currency-converter/usd-to-cad-rate")

        text = BeautifulSoup(str(usd), 'features="html.parser"')
        #print(text.get_text())


else:
    #CAD to US
    print('cadtous')
