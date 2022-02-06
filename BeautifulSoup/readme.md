1. Buka aplikasi **pycharm**
2. Buat nama project **contoh : beautyfulSoup4**
3. Klik Terminal, Install **request** dengan perintah ```pip install requests```
   Kemudian install **beautifulsoup4** dengan perintah ```pip install beautifulsoup4```,
   Maka hasilnya akan seperti gambar dibawah ini.
   
   ![https://git-scm.com](https://github.com/Tior3turn/UAS-1/blob/main/BeautifulSoup/Image/Bs4.png?raw=true)
   
4. klik **python packages** atau **View->Tool Windows->Python Packages** dan pilih **beautifulsoup4** 
   Maka hasilnya akan seperti gambar dibawah ini.
   
      ![https://git-scm.com](https://github.com/Tior3turn/UAS-1/blob/main/BeautifulSoup/Image/Bs5.png?raw=true)

5. Disini saya mencoba scraping dari website **BMKG**
6. Masukkan Kode program :
   ```
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
   ```
   Seperti gambar dibawah ini.
   
   ![https://git-scm.com](https://github.com/Tior3turn/UAS-1/blob/main/BeautifulSoup/Image/Bs6.png?raw=true)
 
 6. Klik **run**, Maka Hasil scraping dari website **https://www.bmkg.go.id** akan ditampilkan seperti gambar dibawah ini.
   ![https://git-scm.com](https://github.com/Tior3turn/UAS-1/blob/main/BeautifulSoup/Image/Bs7.png?raw=true)
   
   ![https://git-scm.com](https://github.com/Tior3turn/UAS-1/blob/main/BeautifulSoup/Image/Bs8.png?raw=true)


