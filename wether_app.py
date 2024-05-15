import requests
from bs4 import beautifulSoup


place = input("Enter the place which wether you want to know:\n")
search = f"wether in {place}"
url = f'https://www.google.com/search?&q={search}'

r = requests.get(url)

s = beautifulSoup(r.text,'html.parser')

update = s.find('div', class_='BNE awe').text

print(update)