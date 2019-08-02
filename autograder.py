grade = 100

def end_and_print_grade():
  print('='*79)
  if grade == 100:
    print('¡Felicidades no se detectó ningún error!')
  print('Su nota asignada es: NOTA<<{0}>>'.format(grade if grade >= 0 else 0))
  exit()

def print_error_and_exception(error, exception):
  print(error)
  print("La excepcion recibida fue: \n\n{0}\n\n".format(e))

# Import module
try:
  import webcrawler
except Exception as e:
  print_error_and_exception('No se pudo importar el modulo webcrawler.py', e)
  grade = 0
  end_and_print_grade()

# Create object
try:
  wc = webcrawler.WebCrawler()
except Exception as e:
  print_error_and_exception('Error al crear un objeto de tipo WebCrawler', e)
  grade = 0
  end_and_print_grade()

try:
  with open("test_urls.txt", "w") as f:
    for url in [ "https://www.all4cycling.com/en/bicycles/e-bike/specialized-turbo-levo-fsr-expert-carbon-2019-black-green-188468.html", "https://www.all4cycling.com/en/bicycles/e-bike/cannondale-synapse-neo-1-black-173004.html","https://www.all4cycling.com/en/bicycles/fitness-and-urban/specialized-sirrus-silver-yellow-124759.html", "https://www.all4cycling.com/en/bicycles/kids/cannondale-trail-balance-12-boy-s-green-171058.html"] :
      print(url, file=f)
except Exception as e:
  print_error_and_exception('Error al crear el archivo "test_urls.txt" en el directorio actual', e)
  grade = 0
  end_and_print_grade()

# Crawl
try:
  result = wc.crawl("test_urls.txt")
except Exception as e:
  print_error_and_exception('Error al invocar al método crawl', e)
  grade = 0
  end_and_print_grade()


# Compare results
if result != {
  'Specialized Turbo Levo FSR Expert Carbon 2019 - Black green': '€8,199.00', 
  'Cannondale Synapse Neo 1 - Black': '€4,799.20', 
  'Specialized Sirrus - Silver Yellow': '€500.00', 
  "Cannondale Trail Balance 12 Boy's - Green": '€198.99' } :

  print('Error los resultados del método crawl no coinciden con los resultados esperados')
  grade = 0


end_and_print_grade()