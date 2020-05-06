from bs4 import BeautifulSoup
import requests

url = 'https://3g.163.com/news/20/0422/13/FAQRMK7D0001899O.html'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
r = requests.get(url, headers)
if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    s_main= soup.main
    pp = s_main.find_all("p")
    for p in pp:
        print(p.get_text())