# Proyecto No. 1 Inteligencia Artificial WebCrawler
Rastreador web que descarga y parsea páginas web para extraer información de productos.

## Descripción
Este proyecto implementa un web crawler que lee URLs desde un archivo, descarga las páginas web y extrae información de productos (nombre y precio) utilizando BeautifulSoup4.

## Requisitos Previos
- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- pipenv (opcional, recomendado)

## Instalación

### Opción 1: Usando pipenv (Recomendado)

1. Instalar pipenv si no lo tienes:
```bash
pip install pipenv
```

2. Instalar las dependencias del proyecto:
```bash
pipenv install
```

3. Activar el entorno virtual:
```bash
pipenv shell
```

### Opción 2: Usando pip directamente

1. Crear un entorno virtual (opcional pero recomendado):
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/Mac
# venv\Scripts\activate   # En Windows
```

2. Instalar las dependencias:
```bash
pip install beautifulsoup4 lxml requests
```

## Dependencias
El proyecto utiliza las siguientes librerías:
- **beautifulsoup4**: Para parsear el HTML de las páginas web
- **lxml**: Parser XML/HTML de alto rendimiento
- **requests**: Para realizar peticiones HTTP

## Estructura del Proyecto
```
WebCrawler/
├── webcrawler.py          # Clase principal del web crawler
├── autograder.py          # Script de evaluación automática
├── test_with_mock.py      # Tests con datos simulados
├── urls.txt               # Archivo con URLs a procesar
├── test_urls.txt          # URLs de prueba
├── test_urls_mock.txt     # URLs para tests
├── Pipfile                # Dependencias del proyecto
└── README.md              # Este archivo
```

## Uso

### Ejecución básica
```bash
python webcrawler.py
```

### Ejecutar con el autograder
```bash
python autograder.py
```

### Ejecutar tests
```bash
python test_with_mock.py
```

## Formato del archivo de URLs
El archivo de entrada (por defecto `urls.txt`) debe contener una URL por línea:
```
https://example.com/producto1
https://example.com/producto2
https://example.com/producto3
```

## Salida
El programa genera un diccionario con los productos encontrados:
```python
{
  "Nombre del Producto 1": "€1,299.00",
  "Nombre del Producto 2": "€2,799.00",
  "Nombre del Producto 3": "€499.00"
}
```

## Notas
- El crawler usa un User-Agent personalizado para evitar bloqueos
- Las páginas se parsean usando BeautifulSoup4 con el parser lxml
- Los precios y nombres se extraen según la estructura HTML de cada sitio

## Autor
EmSanchezM