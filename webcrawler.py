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
      url = list_urls[i]
      req = Request(url,headers=values)
      ruta = urlopen(req).read()

      soup = BeautifulSoup(ruta, 'lxml')
      
      dict_datos = dict()
      
      for name in soup.find('span', class_='base'):
        for price in soup.find('span', class_='price'):
          dict_datos[name] = price
      
      diccionario = {}
      k = dict_datos.keys()
      v = dict_datos.values()
      
      for k,v in dict_datos.items():
        diccionario[k] = v

      print(diccionario)

web = WebCrawler()
web.crawl('test_urls.txt')



