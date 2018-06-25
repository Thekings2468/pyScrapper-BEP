from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import sqlite3

db = sqlite3.connect("db.sqlite3")
dbc = db.cursor()
dbc.execute('''
    CREATE TABLE IF NOT EXISTS empregos(codigo TEXT PRIMARY KEY, tipo_oferta TEXT, vinculo TEXT,
    carreira TEXT, categoria TEXT, distrito TEXT, organismo TEXT, habilitacoes TEXT, data_limite TEXT)
''')
options = Options()
options.set_headless(headless=True)
browser = webdriver.Firefox(firefox_options=options)
print("Fetching URL...")
browser.get("https://www.bep.gov.pt/pages/oferta/Oferta_Pesquisa_basica.aspx")
searchForm = browser.find_element_by_id("ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_txtValor")
searchForm.send_keys("")
submit = browser.find_element_by_id("ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_ucSearch")
submit.click()
numRows = Select(browser.find_element_by_id("ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_ddlNReg"))
numRows.select_by_value("50")
print("Form Options Sent")
#browser.minimize_window()
dbc.execute("DELETE FROM empregos")
done = False
count = 1
regs = 0
while done == False:
    html = browser.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id='ctl00_ctl00_FormMasterContentPlaceHolder_ContentPlaceHolder1_GvOfertaGestao')
    rows = table.find_all('tr')
    for i in rows:
        cols = i.find_all('td')
        listout = []
        for j in cols:
            listout.append(j.get_text().lstrip().rstrip())
        if listout != []:
            regs += 1
            dbc.execute('''INSERT INTO empregos(codigo, tipo_oferta, vinculo, carreira, categoria, distrito, organismo, habilitacoes, data_limite) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''', (listout[0], listout[1], listout[2], listout[3], listout[4], listout[5], listout[6], listout[7], listout[8]))
    db.commit()
    nextPage = browser.execute_script('''var paginationBar = document.getElementsByClassName('AspNet-GridView-Pagination');
        var paginationItems = paginationBar[0].getElementsByTagName('a');
        for (i=0; i<paginationItems.length; i++) {
            if (paginationItems[i].text == ">") var nextPage = paginationItems[i];
        }
        if (typeof nextPage !== 'undefined') return nextPage; else return 'NULL';
    ''')
    if nextPage == 'NULL':
        done = True
        print("Number of Pages Written: %s\nWritten Rows: %s" % (count,regs))
    else:
        nextPage.click()
        count += 1
browser.quit()