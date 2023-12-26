''' This program is to extract the MF holdings in different stocks
Author: Hrisikesh Borthakur
Date: 09-Oct-2022
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == "__main__":
    print("Please choose \n 1) ABSL \n 2) KOTAK \n 3) HDFC")

    user_input = input()
    URL = 'C:/Users/Hrisikesh/Documents/Folio_Holdings/' + user_input + '.html'

    page = open(URL ,encoding="utf8")
    soup = BeautifulSoup(page.read())

    thead = soup.find("table", { "id" : "equityTopSummaryTable" })
    head = []
    table_header = thead.find('thead')
    headers = table_header.find_all('th')
    head = [ele.text.strip() for ele in headers ]


    table = soup.find("table", { "id" : "equityCompleteHoldingTable" })
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    data = [ele for ele in data if ele != ['No group']]
    df = pd.DataFrame(data,columns=head)
    filename = user_input + '.csv'
    df.to_csv(filename, index=True, encoding='utf-8')
    page.close()

    print("Extraction Completed.")

