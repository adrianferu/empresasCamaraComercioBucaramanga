#Aquí también debemos importar todas las librerías

import random
import pandas as pd
from tqdm import tqdm
from cred_here_Template import * #Aquí está consuimiendo la API de HERE. Si no la importas, NO te arrojará resultados
import json
import requests
import ast

# Tools

import folium
from shapely.geometry import Polygon
import numpy as np
import geojson
import folium
import geopandas as gpd
from shapely.geometry import Polygon
import shapely.wkt
from haversine import haversine, Unit
import random
import time
from pyproj import Geod
#from polygon_geohasher.polygon_geohasher import geohash_to_polygon

from shapely import wkt
from geopandas import datasets, GeoDataFrame, read_file, points_from_xy
from geopandas.tools import overlay
from geopandas.tools import sjoin

from folium.plugins import MeasureControl
from folium.plugins import MarkerCluster

import time



#Función para extraer coordenadas

def get_coord (address, YOUR_API_KEY):
    url = f'https://geocode.search.hereapi.com/v1/geocode?q={address}&apiKey={YOUR_API_KEY}'
    
    try:
        response = requests.get(url).json() #Transformacion de la peticion a Json
        dirLimpia = response['items'][0]['title'].upper()#Indexing del json para extraer la direccion
        lat = response['items'][0]['position']['lat'] #Indexing del json para extraer la latitud
        lng = response['items'][0]['position']['lng'] #Indexing del json para extraer la longitud
        
        results = [dirLimpia, lat, lng] #Creamos una lista a partir de los valores d elas 3 variables
        
    except:
        results = ['Not Found', 'NA','NA']
        
    return results
        