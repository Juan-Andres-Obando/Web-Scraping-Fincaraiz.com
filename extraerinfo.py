# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 09:49:01 2023

@author: juan_
"""
#Se cargan librerías
from bs4 import BeautifulSoup as bs
import random
import time
import pandas as pd
import undetected_chromedriver as uc
import regex as re
#Se define la función que extrae número de html
def extraernumero(cadena):
	lista = re.findall(r'-?\d+\.?\d*',cadena.replace(".","").replace(",","."))
	respuesta = cadena
	if lista != []:
		
		respuesta = float("".join(lista))
	return respuesta
	#return float(lista[0]+"."+lista[1])

#se leen los links del csv
datos = pd.read_csv('links.csv')
#se ponen los links en una lista
links = list(datos.iloc[:,1])
#Se crean dos listas vacías para dividir los links por proyectos e inmuebles en venta
links_proyectos=[]
links_inmuebles=[]
#Se dividen los links
for link in links: 
	if link.find("proyecto")==-1:
		links_inmuebles.append(link)
	else:
		links_proyectos.append(link)

Habitaciones = []
Baños = []
Parqueaderos = []
Area_Cons = []
Area_Priv = []
Estrato = []
Antiguedad = []
Piso= []
Administracion= []
Precio_Metro= []
Transaccion= []
Precio= []
Barrio = []
Ciudad= []
tipo_apartamento = []
Estado = []
links_d = []

#Se crea el diccionario
dicc = {'Habitaciones': Habitaciones,
 'Baños': Baños,
 'Parqueaderos': Parqueaderos,
 'Área construída': Area_Cons,
 'Área privada': Area_Priv,
 'Estrato': Estrato,
 'Antigüedad': Antiguedad,
 'Piso N°': Piso,
 'Administración': Administracion,
 'Precio m²': Precio_Metro,
 'Transacción': Transaccion,
 'Precio': Precio,
 'Barrio': Barrio,
 'Ciudad': Ciudad,
 'Tipo de apartamento':tipo_apartamento,
 'Estado':Estado,
 'Link': links_d}

#links_inmuebles = links_inmuebles[118:119]
#Se abre el browser
contador=0
browser = uc.Chrome()
links_inmuebles=links_inmuebles[1245:]
for link in links_inmuebles:
	contador=contador+1
	#Se abre finca raiz
	browser.get(f"https://fincaraiz.com.co{link}")
	time.sleep(random.random()*3)
	#Se obtiene el htm
	html = browser.page_source
	#el html se convierte en obejto soup
	soup = bs(html, 'lxml')
	if soup.find(string="This page could not be found")==None:
		#Se extraen todas las características
		todos = soup.find_all("div", id="general")[0].find_all("div")[0].find_all("p")
		#Se dejan las importantes
		todos = todos[4:-1]
		#Se inician todas listas vacías que guardarán las caracterísitcas de todos los inmuebles
		for i in range(0,len(todos),2):
			dicc[todos[i].text].append(extraernumero(todos[i+1].text))
			
		if link.find("venta") !=-1:
			 dicc["Transacción"].append("Venta")
			 dicc["Barrio"].append(link[link.find("venta/")+6:link.find("/",link.find("venta/")+6)].replace("-", " "))
		elif link.find("arriendo") !=-1:
			dicc["Transacción"].append("Arriendo")
			dicc["Barrio"].append(link[link.find("arriendo/")+9:link.find("/",link.find("arriendo/")+9)].replace("-", " "))
		
		dicc["Precio"].append(extraernumero(soup.find("aside").find_all("p")[1].text))

		dicc["Ciudad"].append("Bogotá")
		dicc['Link'].append(link)
		
		for i in list(dicc.keys()):
			if len(dicc[i])!=len(dicc["Ciudad"]):
				dicc[i].append("No definida")
		

dicc2 = {"linkss": links_inmuebles}
dicc2=pd.DataFrame(dicc2)
dicc2.to_csv("linkshasta.csv")

basedatos= pd.DataFrame(dicc)
basedatos.to_csv("basededatos.csv")
