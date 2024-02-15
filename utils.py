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
        