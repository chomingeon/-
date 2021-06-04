from urllib.request import urlopen
from bs4 import BeautifulSoup

url='https://search.shopping.naver.com/catalog/26965594523?NaPm=ct%3Dkphmlpqo%7Cci%3D6835543d6776c4ac63a5cd639a1b8d651a173d54%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D3e52d6885859381c09c5f0e2aab85972d6b3021a'
html=urlopen(url)
bs = BeautifulSoup(html, 'html.parser')

table = bs.select('.lowestPrice_low_price__fByaG')
for tr in table:
    print(tr.get_text())
