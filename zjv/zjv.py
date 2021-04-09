import pymongo
import requests
from bs4 import BeautifulSoup

Client = pymongo.MongoClient('192.168.9.151', 27017)
Db = Client.zaojv
My_Collection = Db.clause

Url_Init = 'http://zaojv.com/word.html'

Resp = requests.get(Url_Init)
Response_Html = Resp.text
Soup = BeautifulSoup(Response_Html, 'html.parser')

Elements_Page_Number = Soup.find("input", attrs={"id": "pageCountNo"})
Page_Number = int(Elements_Page_Number.get("value"))

for i in range(Page_Number): #Page_Number
    url_item = 'http://zaojv.com/word_' + str(i+1) + '.html'
    Resp = requests.get(url_item)
    Response_Html = Resp.text
    Soup = BeautifulSoup(Response_Html, 'html.parser')
    Elements_Clauses_Part = Soup.find_all("ul", attrs={"class": "c1 ico2"})
    for E_C in Elements_Clauses_Part:
        Elements_Clauses = E_C.find_all("a")
        for Clause_Item in  Elements_Clauses:
            Series = {}
            Clause_Href = "http://zaojv.com" + Clause_Item.get("href")
            Resp_Detail = requests.get(Clause_Href)
            Response_Detail_Html = Resp_Detail.text
            Soup_Detail = BeautifulSoup(Response_Detail_Html, 'html.parser')
            E_T = Soup_Detail.find("h2", attrs={"style": "display:inline;"})
            Clause_Title = E_T.get_text().strip()
            Ele_Clauses = Soup_Detail.find("div", attrs={"id": "all"})
            Ele_Count = 1
            Ele_Clauses_items = Ele_Clauses.find_all("div")
            Clause_List = []
            for Ele_Clauses_item in Ele_Clauses_items:
                C_C = Ele_Clauses_item.get_text().strip()
                print("zaojv"+C_C)
                Clause_List.append(C_C)
                if Ele_Count == 5:
                    break
                Ele_Count += 1
            Series["clause_item"] = Clause_Title
            Series["clauses"] = Clause_List
            My_Collection.save(Series)
