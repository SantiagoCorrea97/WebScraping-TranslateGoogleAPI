from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas

url = 'https://www.classcentral.com/'
webdriver = webdriver.Chrome()
webdriver.get(url)
soup = BeautifulSoup(webdriver.page_source,'html.parser')

# Links dentro de la página
links = ['https://www.classcentral.com/']

for link in soup.find_all('a'):
    links.append(link.get('href'))

# Agregamos el url del principio a los que les falta
flinks = []
a = 'https://www.classcentral.com/'

for html in links:
    if re.match('(http|https)\:\/\/', html):
        flinks.append(html)
    else: 
        html = html[1:]  
        a += html
        flinks.append(a) 
    a = 'https://www.classcentral.com/'


# Removiendo los repetido
result = [] 
[result.append(x) for x in flinks if x not in result] 
flinks = result

# Removiendo las páginas de redes sociales y vainas que no van
flinks.pop(270)
flinks.pop(270)
flinks.pop(270)
flinks.pop(270)
flinks = flinks[:-3]

#Organizado en una tabla 
pd = pandas.DataFrame({"Links": flinks}, index=list(range(1,len(flinks)+1)))
print(pd.to_string())