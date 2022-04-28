
import requests
from bs4 import BeautifulSoup

url = "https://www.kabum.com.br/"

headers = {
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
placas = soup. find_all('div' , class_='sc-eGAhfa iVjBPP')

placa = placas[0]
marca = placas.find('span', class_='sc-csvncw gASsfm sc-jGprRt eAtvC nameCard')
