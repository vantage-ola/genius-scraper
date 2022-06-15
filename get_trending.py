from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = "https://genius.com/"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()
page = webpage.decode("utf-8")
soup = BeautifulSoup(page, "html.parser")

script = (soup.find_all("script"))
data = ((script[15].string))
