"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """
    Inicializa el catálogo de las obras. Crea una lista vacia para guardar
    todos los obras, adicionalmente, crea una lista vacia para los artistas.
    """
    catalog = {'artworks': None,
               'artists': None}

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList()

    return catalog

# Funciones para agregar informacion al catalogo
def addArtworks(catalog, artworks):
    lt.addLast(catalog['artworks'], artworks)
    artworks = newArtwork(artworks['ObjectID'], artworks['ConstituentID'], artworks ['Title'], artworks['Date'], artworks['Medium'], artworks['Dimensions'], artworks['CreditLine'], artworks['AccessionNumber'], artworks['Classification'],artworks['Department'], artworks['DateAcquired'], artworks['Cataloged'], artworks['URL'], artworks['Circumference (cm)'], artworks['Depth (cm)'], artworks['Diameter (cm)']
    ,artworks['Height (cm)'], artworks['Length (cm)'], artworks['Weight (kg)'], artworks['Width (cm)'], artworks['Seat Height (cm)'], artworks['Duration (sec.)'])
    

def addArtist(catalog, artists):
    lt.addLast(catalog['artists'], artists)
    artists = newArtist(artists['ConstituentID'], artists['DisplayName'],  artists['ArtistBio'],  artists['Nationality'],  artists['Gender'],  artists['BeginDate'],  artists['EndDate'],  artists['Wiki QID'],  artists['ULAN'])


# Funciones para creacion de datos
def newArtist(constituentid, displayname, artistbio, nationality, gender, begindate, enddate, wikiqid, ulan):
    
    artists = {'constituentid': "", 'displayname': '' , 'artistbio': '', 'nationality': '', 'gender': '', 'begindate': '', 'enddate': '', 'wikiqid': '', 'ulan': ''}
    
    artists['constituentid'] = constituentid
    artists['displayname'] = displayname
    artists['artistbio'] = artistbio
    artists['nationality'] = nationality
    artists['gender'] = gender
    artists['begindate'] = begindate
    artists['enddate'] = enddate
    artists['wikiqid'] = wikiqid   
    artists['ulan'] = ulan
    artists['artworks'] = lt.newList('ARRAY_LIST')
    return artists


def newArtwork(objectid, constituentid, title,  date, medium, dimensions, creditline, accessionnumber, classification, department, dateacquired, cataloged, url, circumference, depth, diameter, height, length, weight, width, seatheight, duration):

    artworks = {'constituentid': "",'date': "",'medium': "",'dimensions': "",'creditline': "",'accessionnumber': "",'classification': "",'department': "",'dateacquired': "",'cataloged': "",'objectid': "",'url': "",'circumference': "",'depth': "",'diameter': "",'height': "",'lenght': "",'weight': "",'width': "",'seatheight': "",'duration': "",}
   
    artworks['objectid']= objectid
    artworks['constituentid']= constituentid
    artworks['title']= title
    artworks['date']= date
    artworks['medium']= medium
    artworks['dimensions']= dimensions
    artworks['creditline']= creditline
    artworks['accessionnumber']= accessionnumber
    artworks['classification']= classification
    artworks['department']=  department
    artworks['dateacquired']= dateacquired
    artworks['cataloged']= cataloged
    artworks['url']= url
    artworks['circumference']= circumference
    artworks['depth']= depth
    artworks['diameter']= diameter
    artworks['height']= height
    artworks['length']= length
    artworks['weight']= weight
    artworks['width']= width
    artworks['seatheight']= seatheight
    artworks['duration']= duration
    artworks['artists'] = lt.newList('ARRAY_LIST')


    return artworks

#REQ. 1: listar cronológicamente los artistas (Grupal)   

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento