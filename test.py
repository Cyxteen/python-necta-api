# imports
from bs4 import BeautifulSoup
import requests

url = 'https://onlinesys.necta.go.tz/results/2019/acsee/results/s0133.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

try:
    division_one = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
except AttributeError:
    print('no')  

# if division_one:
#     print('yes')
# else:
#     print('no')