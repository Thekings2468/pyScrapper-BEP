# BEP Scrapper
## Introduction
A script to scrape job offers from [BEP's offer page](https://www.bep.gov.pt/pages/oferta/Oferta_Pesquisa_basica.aspx).
This script uses Selenium to access the webpage, BeautifulSoup to parse the webpage's data and an SQLite3 database to save the data.
The script's RESTful API and front-end use Flask.
## Requirements
### Python packages
Execute the following command to install the required python packages (I recommend installation in a python virtual environment):
```
pip3 install -r requirements.txt
```
### Geckodriver
You also need the [Geckodriver](https://github.com/mozilla/geckodriver/releases) executable in your PATH or the script's working directory to run the scrapper.
## Executing
### Running the scrapper
```
python3 scrapper_selenium.py
```
### Running the front-end and the REST API
```
python3 rest.py
```
The API and the front-end are set to listen in port 5002. The front-end search through category feature is incomplete and may lag some browsers while performing a search.
## Access the front-end
Open your browser and type the following in the address bar: `http://127.0.0.1:5002/index.html`
## Available API methods
Search Type | API method
-- | --
List all the offers in the DB|`/jobs`
Search offers through types|`/search/type/search_query`
Search offers through contract type|`/search/contract/search_query`
Search offers through career|`/search/career/search_query`
Search offers through category|`/search/category/search_query`
Search offers through district|`/search/district/search_query`
Search offers through organization|`/search/org/search_query`
Search offers through academic skills|`/search/skills/search_query`
Search offers through expire date|`/search/expire/search_query`
