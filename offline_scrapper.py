from bs4 import BeautifulSoup
import csv

f = open("offlinetest.html", "r")
html = f.read()
f.close()
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
table = soup.find(id='ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_GvOfertaGestao')
#print(type(table))
rows = table.find_all('tr')
with open("output.csv", "w", newline='') as w:
    wcsv = csv.writer(w, delimiter=';')
    wcsv.writerow(["codigo", "tipo_oferta", "vinculo", "carreira", "categoria", "distrito", "organismo", "habilitacoes_literarias", "data_limite"])
    for i in rows:
        cols = i.find_all('td')
        listout = []
        for j in cols:
            listout.append(j.get_text().lstrip().rstrip())
        if listout != []: wcsv.writerow(listout)