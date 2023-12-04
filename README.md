

# Web Scraping de Propiedades Inmobiliarias en Colombia

Este proyecto es únicamente con fines educativos y realiza web scraping en el sitio web fincaraiz.com.co para recopilar información sobre propiedades inmobiliarias en Colombia. Se compone de dos scripts: `extraerlinks.py` que recopila enlaces a propiedades y `extraerinfo.py` que extrae información detallada de cada propiedad a través de los enlaces almacenados.

## Contenido

1. [Requisitos](#requisitos)
2. [Configuración del Entorno](#configuración-del-entorno)
3. [Ejecución del Web Scraping de Enlaces](#ejecución-del-web-scraping-de-enlaces)
4. [Ejecución del Web Scraping Detallado](#ejecución-del-web-scraping-detallado)
5. [Datos Recopilados](#datos-recopilados)
6. [Notas](#notas)

## Requisitos

Asegúrate de tener instalados los siguientes paquetes:

- Python 3
- pip

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
Además, necesitarás tener configurado el navegador web en undetected_chromedriver. Sigue las instrucciones en la documentación de undetected_chromedriver.

## Configuración del Entorno
Antes de ejecutar los scripts, configura el navegador web según las instrucciones proporcionadas.

## Ejecución del Web Scraping de Enlaces
Ejecuta el script extraerlinks.py para recopilar enlaces de propiedades:

```bash
python extraerlinks.py
```
Los enlaces se almacenarán en un archivo CSV llamado links.csv.

## Ejecución del Web Scraping Detallado

Ejecuta el script extraerinfo.py para realizar la extracción detallada de información:

```bash
python extraerinfo.py
```

Este script utiliza los enlaces almacenados en links.csv para acceder a cada propiedad, extraer información específica y guardar los resultados en dos archivos CSV: basededatos.csv que contiene los detalles de las propiedades, y linkshasta.csv que guarda los enlaces procesados.

## Datos Recopilados
Los datos extraídos incluyen diversas características de las propiedades, como el número de habitaciones, baños, área construida y privada, estrato, antigüedad, entre otros. Estos datos se almacenan en basededatos.csv. Además, se guarda un registro de los enlaces procesados en linkshasta.csv.

## Notas
1. Asegúrate de cumplir con los términos de servicio del sitio web fincaraiz.com.co.
2. Estos scripts se proporcionan como referencia y no deben utilizarse para actividades ilegales o violatorias de la ética.

Este proyecto es una herramienta útil para obtener información detallada sobre propiedades inmobiliarias en Bogotá, Colombia. Recuerda ser respetuoso con los términos de servicio del sitio web y utilizar estos scripts de manera ética.
