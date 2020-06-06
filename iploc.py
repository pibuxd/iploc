import requests, bs4, os
import pandas as pd

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

os.system("cls")
ip = input('{}Enter IP you want to spy: {}'.format(GREEN, END))
page_url = 'https://tools.keycdn.com/geo?host='+ip
print()
res = requests.get(page_url)

soup = bs4.BeautifulSoup(res.text, 'lxml')

info = soup.find_all("dl", {'class':'row mb-0'})
comp_info = pd.DataFrame()
cleaned_id_text = []

for i in info[0].find_all('dt'):
    cleaned_id_text.append(i.text)

cleaned_id__attrb_text = []

for i in info[0].find_all('dd'):
    cleaned_id__attrb_text.append(i.text)

comp_info['Id'] = cleaned_id_text
comp_info['Attribute'] = cleaned_id__attrb_text
print(comp_info)
