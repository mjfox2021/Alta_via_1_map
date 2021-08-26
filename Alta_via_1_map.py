##-*- coding: utf-8 -*-
"""
Created on 4/6/2021

@author: mjf2

Uses folium to generate an interactive map of the 2010NZNSHM fault model. User can click
on a fault to know its name, mechanism, characterisic magnitude, and return period
    
"""
#%%Import modules and generate map-----------------------------------------------
import folium
import webbrowser

m = folium.Map(location = [46.5, 12.034], tiles="Stamen Terrain",zoom_start = 9)

#%%Load fault data and plot fault surface traces--------------------------------

rifugi = [["Fanes",[46.612, 12.014]],
          ["Lagazuoi",[46.52790895234828, 12.006634970066306]],
          ["Nuvolau",[46.495503291312566, 12.043700227050941]],
          ["Venezia",[46.41567195669621, 12.157135859167365]],
          ["Carestiato",[46.32136503928845, 12.071322847783737]],
          ["Pian di Fontana",[46.26195860035523, 12.17707508340776]]]

stages = [[[46.698998736440565, 12.084373754161398],[46.612, 12.014]],
          [[46.612, 12.014],[46.52790895234828, 12.006634970066306]],
          [[46.52790895234828, 12.006634970066306],[46.495503291312566, 12.043700227050941]],
          [[46.495503291312566, 12.043700227050941],[46.41567195669621, 12.157135859167365]],
          [[46.41567195669621, 12.157135859167365],[46.32136503928845, 12.071322847783737]],
          [[46.32136503928845, 12.071322847783737],[46.26195860035523, 12.17707508340776]],
          [[46.26195860035523, 12.17707508340776],[46.18292016797855, 12.195700997500213]]]

sd = [[	20	,	1465	,	890	,	8	],
[	11	,	1070	,	375	,	5	],
[	15	,	635	,	810	,	5.5	],
[	23	,	840	,	1905	,	10	],
[	22	,	1400	,	1080	,	10	],
[	19	,	990	,	1190	,	8	],
[	15	,	930	,	1765	,	9	],
]

for i in range(len(rifugi)):
    folium.Marker(rifugi[i][1],popup="<i>"+rifugi[i][0]+"</i>", icon=folium.Icon(color='blue', icon='home')).add_to(m)
    
folium.Marker([46.698998736440565, 12.084373754161398],popup="<i>Lago di Braies</i>",icon=folium.Icon(color='green', icon='play')).add_to(m)
folium.Marker([46.18292016797855, 12.195700997500213],popup="<i>Pra de Luni</i>",icon=folium.Icon(color='red', icon='stop')).add_to(m)
    
for i in range(len(stages)):
    folium.PolyLine(stages[i],color="blue",popup="<i>Distance "+str(sd[i][0])+"	Climb "+str(sd[i][1])+"	Descent "+str(sd[i][2])+"	Time "+str(sd[i][3])+"</i>",weight=3,opacity=0.8).add_to(m)

#%%Save map and open in browser-------------------------------------------------
m.save("map.html")
webbrowser.open_new_tab("map.html")