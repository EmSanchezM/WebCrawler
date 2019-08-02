from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from io import open 

class WebCrawler:

  def crawl(self, input_filename):
    """
    Realiza la descarga y el parseo de todas la URL almacenadas en el archivo <input_filename>,
    las URL están separadas por un salto de línea, como ejemplo se adjunta el archivo urls.txt.

    La descarga de la página se realizará usando la librería urllib y el parseo mediante el uso de la librería BeautifulSoup4, de cada página se leerá el nombre del producto y su precio, todo esto se irá añadiendo a un diccionario cuyas claves serán los nombres y sus valores tendrán el precio como el siguiente ejemplo:
    { 
      "Orbea Avant M30 Team-D 19 - Black grey" : "€2,299.00",
      "Cannondale SuperSix EVO Carbon Disc 105 2020 - Red": "€2,799.00",
      "Specialized Pitch 650B - Light blue": "€499.00"
    }
    """
    input_file = open(input_filename, 'r')
    list_urls = input_file.readlines()
    input_file.close()
    #print(list_urls) Funciona
    values = {'User-Agent': 'Mozilla/5.0 (Windows 10 Home) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    
    for i in range(len(list_urls)):
      url1 = list_urls[0]
      url2 = list_urls[1]
      url3 = list_urls[2]
      url4 = list_urls[3]

      req1 = Request(url1,headers=values)
      req2 = Request(url2,headers=values)
      req3 = Request(url3,headers=values)
      req4 = Request(url4,headers=values)

      ruta1 = urlopen(req1).read()
      ruta2 = urlopen(req2).read()
      ruta3 = urlopen(req3).read()
      ruta4 = urlopen(req4).read()

      soup1 = BeautifulSoup(ruta1, 'lxml')
      soup2 = BeautifulSoup(ruta2, 'lxml')
      soup3 = BeautifulSoup(ruta3, 'lxml')
      soup4 = BeautifulSoup(ruta4, 'lxml')

      
    dict_datos = dict()
    list_name = []
    list_price = []
      
    for name in soup1.find('span', class_='base'):
      list_name.append(name)

    for name in soup2.find('span', class_='base'):
      list_name.append(name)
    
    for name in soup3.find('span', class_='base'):
      list_name.append(name)
    
    for name in soup4.find('span', class_='base'):
      list_name.append(name)

    for price in soup1.find('span', class_='price'):
      list_price.append(price)
    
    for price in soup2.find('span', class_='price'):
      list_price.append(price)
    
    for price in soup3.find('span', class_='price'):
      list_price.append(price)
    
    for price in soup4.find('span', class_='price'):
      list_price.append(price)

    dict_datos = {list_name[0]:list_price[0], list_name[1]:list_price[1], list_name[2]:list_price[2], list_name[3]:list_price[3]}  
    
    return dict_datos

web = WebCrawler()
web.crawl('test_urls.txt')



