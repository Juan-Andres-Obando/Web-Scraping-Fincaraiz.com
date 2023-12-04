# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 23:59:28 2023

@author: Juan-Andres-Obando
"""

from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import undetected_chromedriver as uc

#Inicializar el navegador
browser = uc.Chrome()

#Configuración de parámetros de búsqueda
##Ejemplos de Ciudades
###ciudad = ["/bogota", "/medellin", "/cali", "/barranquilla", "/santa-marta"]
ciudad = ["/bogota"]
##Ejemplos de tipo de inmuebles
###tipo_inmueble = ["/apartamentos", "/apartaestudios", "/casas"]
tipo_inmueble = [""]
##Tipos de trato
#tipo_trato= ["/venta", "/arriendos"]
tipo_trato= ["/venta", "/arriendos"]
pagina = list(range(1,41))

#Lista para almacenar los enlaces
links = []

#Bucle de búsqueda
## Itera tipo de inmueble
for i in tipo_inmueble:
  ## Itera tipo de trato
	for j in tipo_trato:
    ## Itera la ciudad
		for k in ciudad:
      ## Itera las páginas de la búsqueda
			for l in pagina:
        #Espera aleatoria antes de cada cambio de página
				time.sleep(random.random()*4)
        #Construir URL de búsqueda
				url = f"https://fincaraiz.com.co/finca-raiz{i}{j}{k}?pagina={l}"
        #Abrir URL en el navegador
				browser.get(url)
        #Obtener código fuente de la pagina
				html = browser.page_source
        #Analizar el código HTML 
				soup = bs(html, 'lxml')
        #Encontrar todos los enlaces de propiedades en la página
				for a in soup.find('div', id="listingContainer").find_all('a', href=True): links.append(a['href'])


# Crear un DataFrame con los enlaces recolectados
dict = {'compl links': links}
df = pd.DataFrame(dict)
#Exportar el DataFrame a un archivo CSV
df.to_csv('links.csv')
