from bs4 import BeautifulSoup
import requests

get = requests.get("https://www.bmkg.go.id")
bs = BeautifulSoup(get.text, 'html.parser')

main = bs.find('section', id='meteorologi-geofisika')
artikel = main.find_all(class_='carousel-block-table prakicu-kota')
for title in artikel:
    kota = title.find("h2", class_="kota")
    cuaca = title.find("h2", class_="heading-md")
    print(kota.text ,cuaca.text)
