import csv 
import googlemaps
import pandas as pd

dfpontos=pd.read_csv('ARQUIVO COM OS ENDEREÇOS.CSV',encoding='ISO-8859-1',sep=';',low_memory=False)

gmaps = googlemaps.Client(key='CHAVE DA API')

with open('ARQUIVO COM OS ENDEREÇOS.CSV') as f:
    reader = csv.reader(f)
    yourlist = list(reader)
    for ponto in yourlist:
        resgeo = gmaps.geocode(ponto)
        if len(resgeo) > 0:
            resgeo = resgeo[0]
            dpontos = dict()
            dpontos['lat'] = resgeo['geometry']['location']['lat']
            dpontos['lng'] = resgeo['geometry']['location']['lng']
            dpontos['address'] = resgeo['formatted_address']
            print('Endereço: {}, Latitude: {}, Longitude: {}'.format(dpontos['address'], dpontos['lat'], dpontos['lng'] ))