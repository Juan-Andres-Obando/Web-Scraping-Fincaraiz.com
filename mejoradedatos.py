# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:53:04 2023

@author: juan_
"""
import pandas as pd
datos = pd.read_csv('basededatos.csv')
antiguedad = list(datos['Antigüedad'])
for i in list(range(0,len(antiguedad))):
	if antiguedad[i] =="915.0":
		antiguedad[i]="9 a 15 años"
	if antiguedad[i]=="1630.0":
		antiguedad[i]="16 a 30 años"
	if antiguedad[i]=="18.0":
		antiguedad[i]= "1 a 8 años"
	if antiguedad[i]=="1.0":
		antiguedad[i]="menos de 1 año"
	if antiguedad[i]=="30.0":
		antiguedad[i]="más de 30 años"

datos['Antigüedad_1']=antiguedad

links = list(datos["Link"])

tipo_inmueble= list(s.replace("/inmueble/","")[0:s.replace("/inmueble/","").find("-")].title() for s in links)
datos["tipo inmueble"]=tipo_inmueble

datos.to_csv("basemejorada.csv")
