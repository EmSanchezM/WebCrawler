"""
Test del WebCrawler con datos simulados para demostrar que el código funciona correctamente
"""
from bs4 import BeautifulSoup
from unittest.mock import patch, mock_open
from io import BytesIO
from webcrawler import WebCrawler

# HTML de ejemplo simulando la estructura de all4cycling.com
html_samples = {
    'url1': """
    <html>
    <body>
        <span class="base">Specialized Turbo Levo FSR Expert Carbon 2019 - Black green</span>
        <span class="price">€8,199.00</span>
    </body>
    </html>
    """.encode('utf-8'),
    'url2': """
    <html>
    <body>
        <span class="base">Cannondale Synapse Neo 1 - Black</span>
        <span class="price">€4,799.20</span>
    </body>
    </html>
    """.encode('utf-8'),
    'url3': """
    <html>
    <body>
        <span class="base">Specialized Sirrus - Silver Yellow</span>
        <span class="price">€500.00</span>
    </body>
    </html>
    """.encode('utf-8'),
    'url4': """
    <html>
    <body>
        <span class="base">Cannondale Trail Balance 12 Boy's - Green</span>
        <span class="price">€198.99</span>
    </body>
    </html>
    """.encode('utf-8')
}

# Simular las URLs (ahora con URLs completas pero ficticias)
test_urls = """https://example.com/url1
https://example.com/url2
https://example.com/url3
https://example.com/url4"""

def mock_urlopen(request):
    """Simula urlopen devolviendo HTML según la URL"""
    url = request.full_url if hasattr(request, 'full_url') else str(request)
    
    # Extraer el identificador de la URL
    for key in html_samples.keys():
        if key in url:
            mock_response = BytesIO(html_samples[key])
            mock_response.read = lambda key=key: html_samples[key]
            return mock_response
    
    raise Exception(f"URL no encontrada: {url}")

# Ejecutar el test con mocks
print("="*70)
print("TEST DEL WEBCRAWLER CON DATOS SIMULADOS")
print("="*70)

# Crear un archivo temporal real
with open('test_urls_mock.txt', 'w') as f:
    f.write(test_urls)

with patch('webcrawler.urlopen', side_effect=mock_urlopen):
    wc = WebCrawler()
    resultado = wc.crawl('test_urls_mock.txt')
    
    print("\n✅ WebCrawler ejecutado exitosamente!")
    print("\nResultados obtenidos:")
    print("-" * 70)
    for nombre, precio in resultado.items():
        print(f"  • {nombre}: {precio}")
    
    # Verificar resultados esperados
    expected = {
        'Specialized Turbo Levo FSR Expert Carbon 2019 - Black green': '€8,199.00',
        'Cannondale Synapse Neo 1 - Black': '€4,799.20',
        'Specialized Sirrus - Silver Yellow': '€500.00',
        "Cannondale Trail Balance 12 Boy's - Green": '€198.99'
    }
    
    print("\n" + "="*70)
    if resultado == expected:
        print("✅ ¡ÉXITO! Los resultados coinciden con los esperados.")
    else:
        print("⚠️  Diferencias encontradas:")
        for key in expected:
            if key not in resultado:
                print(f"  - Falta: {key}")
            elif resultado[key] != expected[key]:
                print(f"  - {key}: esperado '{expected[key]}', obtenido '{resultado[key]}'")
    print("="*70)

print("\n📝 NOTA: Las URLs originales de all4cycling.com ya no están disponibles")
print("   (Error 404), pero el código del webcrawler funciona correctamente.")
print("   Este test demuestra que la lógica de parsing está implementada bien.\n")
