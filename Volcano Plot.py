# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 15:47:50 2020

@author: Matt.Currie
"""

import pandas
import folium

def parseVolcanoeData():
    listOfVolcanoes = []
    #Reads file in as a df
    volcanoesDataFrame = pandas.read_csv("Volcanoes.txt")
    #Selects only desired columns of df
    volcanoesDataFrame = volcanoesDataFrame[["NAME", "LAT", "LON"]]
    #creates a list of tuples containing the importatn data, there may
    #be a better way to extract this data than using iloc
    for index in range(len(volcanoesDataFrame)):
        name = str(volcanoesDataFrame.iloc[index, 0 ])
        lat = float(volcanoesDataFrame.iloc[index, 1 ])
        lon = float(volcanoesDataFrame.iloc[index, 2 ])
        listOfVolcanoes.append((name, lat,lon))
    return listOfVolcanoes
    
            
            
    
    
    

def plotVolcanoes():
    #uses folium to generate a map object
    map = folium.Map(location=[45, -120], tiles="Stamen Terrain" )
    #gets a list of volcanoes in the western US
    volcanoes = parseVolcanoeData()
    #creates a feature group for easy organization of multiple volcanoes
    featureGroup = folium.FeatureGroup(name="Various Volcanoes")
    
    for volcanoe in volcanoes:
        #adds a marker with volcanoe coordinates and name to the feature groups
        featureGroup.add_child(folium.Marker(location=(volcanoe[1], volcanoe[2]), popup=volcanoe[0], icon=folium.Icon(color="red")))
        
    #adds feature group to map  
    map.add_child(featureGroup)
    #saves map
    map.save("VolcanoeMap.html")
    print('hi')

plotVolcanoes()
